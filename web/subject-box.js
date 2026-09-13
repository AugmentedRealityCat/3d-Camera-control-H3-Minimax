import { app } from '../../scripts/app.js';
import { api } from '../../scripts/api.js';
import { resolveLinkedImage } from './linked-image.js';

// PT: Painel de arraste que escreve nos quatro widgets numericos do node.
// EN: Drag panel that writes into the four numeric widgets of the node.
function build(node) {
  const root = document.createElement('div');
  root.style.cssText = 'font:12px system-ui;color:#c9bfe0;padding:6px 0';
  const stage = document.createElement('div');
  stage.style.cssText = 'position:relative;width:100%;aspect-ratio:16/9;background:#1c1a24;border:1px solid #34313f;' +
    'border-radius:8px;overflow:hidden;cursor:crosshair;touch-action:none';
  const picture = document.createElement('img');
  picture.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;object-fit:contain;pointer-events:none';
  const frame = document.createElement('div');
  frame.style.cssText = 'position:absolute;border:2px solid #19c7a7;background:#19c7a71a;pointer-events:none';
  const hint = document.createElement('div');
  hint.style.cssText = 'padding-top:6px;font-size:11px;color:#8d85a0';
  stage.append(picture, frame);
  root.append(stage, hint);

  const widget = name => node.widgets.find(w => w.name === name);
  const read = () => ['left', 'top', 'width', 'height'].map(n => Number(widget(n)?.value ?? 0));
  const write = (l, t, w, h) => {
    // Mantem a caixa dentro do quadro: o prompt le as quatro fracoes como do quadro inteiro.
    const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));
    const values = { left: clamp(l, 0, 1), top: clamp(t, 0, 1) };
    values.width = clamp(w, 0.001, 1 - values.left);
    values.height = clamp(h, 0.001, 1 - values.top);
    for (const [name, value] of Object.entries(values)) {
      const target = widget(name);
      if (target) { target.value = Math.round(value * 1000) / 1000; target.callback?.(target.value); }
    }
    node.setDirtyCanvas(true, true);
    paint();
  };

  function paint() {
    const [l, t, w, h] = read();
    frame.style.left = `${l * 100}%`; frame.style.top = `${t * 100}%`;
    frame.style.width = `${w * 100}%`; frame.style.height = `${h * 100}%`;
    hint.textContent = `[L=${l.toFixed(3)}, T=${t.toFixed(3)}, W=${w.toFixed(3)}, H=${h.toFixed(3)}]`;
  }

  let source = '';
  function refresh() {
    let found = '';
    try { found = resolveLinkedImage(app.graph, node, q => api.apiURL(q)); } catch { found = ''; }
    if (found === source) return;
    source = found;
    picture.style.display = found ? '' : 'none';
    if (found) picture.src = found;
    hint.title = found ? '' : 'PT: Ligue uma imagem em reference_image. EN: Connect an image to reference_image.';
  }

  let drag = null;
  const at = event => {
    const box = stage.getBoundingClientRect();
    return [(event.clientX - box.left) / box.width, (event.clientY - box.top) / box.height];
  };
  stage.addEventListener('pointerdown', event => {
    drag = at(event); stage.setPointerCapture(event.pointerId);
  });
  stage.addEventListener('pointermove', event => {
    if (!drag) return;
    const [x, y] = at(event);
    write(Math.min(drag[0], x), Math.min(drag[1], y), Math.abs(x - drag[0]), Math.abs(y - drag[1]));
  });
  stage.addEventListener('pointerup', () => { drag = null; });

  paint();
  refresh();
  const timer = setInterval(refresh, 1200);
  return { element: root, paint, destroy: () => clearInterval(timer) };
}

app.registerExtension({
  name: 'bruxosdovfx.h3.subject_box',
  async beforeRegisterNodeDef(nodeType, nodeData) {
    if (nodeData.name !== 'BruxosH3SubjectBox') return;
    const created = nodeType.prototype.onNodeCreated;
    nodeType.prototype.onNodeCreated = function () {
      const result = created?.apply(this, arguments);
      const picker = build(this);
      const widget = this.addDOMWidget('subject_box_picker', 'H3_SUBJECT_BOX', picker.element, { serialize: false });
      widget.computeSize = () => [320, 240];
      for (const name of ['left', 'top', 'width', 'height']) {
        const target = this.widgets.find(w => w.name === name);
        if (!target) continue;
        const previous = target.callback;
        target.callback = function () { const r = previous?.apply(this, arguments); picker.paint(); return r; };
      }
      const removed = this.onRemoved;
      this.onRemoved = function () { picker.destroy(); return removed?.apply(this, arguments); };
      this.setSize([340, Math.max(this.size[1], 430)]);
      return result;
    };
  },
});
