# bruxosdovfx · Camera H3 v19.1

`#bruxosdovfx`

<img width="593" height="771" alt="image" src="https://github.com/user-attachments/assets/47d93a37-b474-473a-b97c-337829481598" />


Editor visual de câmera para **MiniMax H3** dentro do ComfyUI.  
Visual camera editor for **MiniMax H3** inside ComfyUI.


https://github.com/user-attachments/assets/eb519677-9859-495d-9b26-37672264fe82
https://github.com/user-attachments/assets/fd3b2940-ce2d-4415-98b1-db0493601363

Arraste a câmera, crie keyframes e gere prompts de trajetória para o H3.  
Drag the camera, create keyframes and generate H3 camera-path prompts.

> **PT:** O node compila prompts. Não é um adaptador geométrico e não garante que o H3 siga a trajetória perfeitamente.  
> **EN:** The node compiles prompts. It is not a geometric adapter and cannot guarantee perfect H3 camera tracking.

---

https://github.com/user-attachments/assets/406871f4-e8b5-4b3d-8e76-abbd057e2a94

## Instalação / Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/NyckM/3d-Camera-control-H3-Minimax.git
```

Reinicie o ComfyUI e procure **bruxosdovfx • Camera H3**.  
Restart ComfyUI and search for **bruxosdovfx • Camera H3**.

https://github.com/user-attachments/assets/908ea90f-701b-4ff1-b27c-9ce432076785

### Experimental

A versão Experimental pode ficar instalada junto da principal.  
The Experimental version can be installed next to the main version.

Pasta / Folder:

```text
3d-Camera-control-H3-Minimax-Experimental
```

Veja / See: [EXPERIMENTS.md](EXPERIMENTS.md)

---

## Novidades v19.1 / What's new in v19.1

| Função / Function | PT | EN |
|---|---|---|
| Smooth | Movimento mais contínuo entre keyframes. | Smoother motion between keyframes. |
| Linear | Movimento linear por trecho. | Linear motion per segment. |
| Redistribute timing | Redistribui os tempos para equilibrar a velocidade média. | Redistributes timing for more even average speed. |
| Unwrap | Corrige cruzamentos como `350° → 10°` para o arco curto. | Converts crossings like `350° → 10°` to the short arc. |
| Start / End Hold | Adiciona 0,5 s de pausa no início ou fim. | Adds a 0.5 s hold at the start or end. |
| Presets | Órbita, subir, descer, aproximar, afastar e câmera estática. | Orbit, rise, fall, move closer, move away and static camera. |
| Diagnostics | Detecta pausas, caminho estático e cruzamentos de zero. | Detects holds, static paths and zero crossings. |
| Loop Closure | `auto` fecha órbitas compatíveis; `off` desativa. | `auto` closes compatible orbits; `off` disables it. |
| UI Language | Painel e diagnóstico em Português ou English. | UI and diagnostics in Português or English. |

---

### `subject_box`

<img width="457" height="447" alt="image" src="https://github.com/user-attachments/assets/5873ded7-fd94-43b1-8503-6cdc451a4c80" />

**PT:** Define **em torno de quem a câmera deve orbitar**.
Se vazio, o centro da imagem é usado como referência. Se preenchido, informa a posição do sujeito no primeiro frame.
Use o node **`bruxosdovfx • H3 Subject Box`** para desenhar a caixa sobre o sujeito e conectar a saída `subject_box` ao Camera H3.
Formato:

`[L=0.62, T=0.18, W=0.24, H=0.55]`

`L` e `T` definem a posição; `W` e `H`, o tamanho. Os valores vão de `0` a `1`.

Útil principalmente quando o sujeito está **fora do centro**.
Não recorta, não aplica zoom e não força o sujeito a permanecer dentro da caixa. Apenas identifica o alvo da câmera no primeiro frame.

---

**EN:** Defines **who the camera should orbit around**.
If empty, the image center is used as reference. If filled, it identifies the subject position in the first frame.
Use **`bruxosdovfx • H3 Subject Box`** to draw a box over the subject and connect its `subject_box` output to Camera H3.
Format:

`[L=0.62, T=0.18, W=0.24, H=0.55]`

`L` and `T` define position; `W` and `H`, size. Values range from `0` to `1`.

Especially useful when the subject is **off-center**.
It does not crop, zoom, or force the subject to remain inside the box. It only identifies the camera target in the first frame.


## Como usar / Basic use

- Arraste a câmera roxa para orbitar. / Drag the purple camera to orbit.
- Scroll muda a distância. / Mouse wheel changes distance.
- Arraste o fundo para girar apenas a visualização. / Drag the background to rotate the preview only.
- Use keyframes para criar a trajetória. / Use keyframes to build the path.
- **Pure Orbit / Órbita pura** zera a elevação. / resets elevation.
- **Play** mostra apenas a prévia da trajetória. / previews the path only.

A prévia mostra o movimento planejado, não o resultado final do H3.  
The preview shows the planned motion, not the final H3 result.

---

## Ligações principais / Main connections

| Saída / Output | Ligue em / Connect to |
|---|---|
| `compiled_prompt` | H3 Edit Text Encode |
| `options` | H3 Edit Text Encode |
| `minimax_prompt` | H3 Native / Ref2VA workflows |
| `reference_first` | imagem inicial / source image |
| `length` | geração / generation |
| `fps` | saída de vídeo / video output |

`compiled_prompt` + `options` trabalham juntos no H3 Edit.  
`compiled_prompt` + `options` are used together with H3 Edit.

Use `minimax_prompt` como alternativa nos workflows nativos.  
Use `minimax_prompt` as the alternative for native workflows.

---

## Freeze Frame

Use uma foto ou um frame de referência.  
Use a still image or reference frame.

- Ligue `reference_image`. / Connect `reference_image`.
- `freeze_index` escolhe o frame do lote. / selects the frame from the batch.
- Ligue `reference_first` ao source image do H3 Edit. / connect it to H3 Edit source image.
- Ligue `compiled_prompt` + `options` ao encoder H3 Edit. / connect them to the H3 Edit encoder.

No H3 nativo, use `minimax_prompt` + primeiro frame no workflow FL2VA.  
With native H3, use `minimax_prompt` + the first frame in an FL2VA workflow.

---

## Motion Frame

Use um vídeo ou sequência de frames como referência de movimento.  
Use a video or frame sequence as motion reference.

- Referência: **2–15 s**. / Reference length: **2–15 s**.
- Informe o FPS real em `source_fps`. / Set the real FPS in `source_fps`.
- Use `scene coverage | camera path`.
- Use modelo **H3 Ref2VA**. / Use an **H3 Ref2VA** model.
- Use **bruxosdovfx • H3 Motion Reference**.

### Conexões / Connections

| Editor | Motion Reference |
|---|---|
| `reference_frames` | `reference_frames` |
| `minimax_prompt` | `prompt` |
| `length` | `length` |
| Qwen H3 encoder | `clip` |
| H3 video VAE | `vae` |

A referência é convertida para 24 fps e ajustada para o formato aceito pelo H3.  
The reference is converted to 24 fps and trimmed to the format expected by H3.

O áudio original não é enviado.  
Original audio is not forwarded.

---

## Interpolação / Interpolation

### `smooth`

Movimento suavizado. Com `extended contracts`, mantém velocidade mais contínua entre os pontos.  
Smoothed motion. With `extended contracts`, motion stays more continuous between waypoints.

### `linear`

Movimento reto entre keyframes.  
Straight interpolation between keyframes.

---

## Timing

Os tempos usam o último frame visível:

```text
(length - 1) / fps
```

Video timing uses the timestamp of the last visible frame.

**Redistribute timing** redistribui os keyframes para equilibrar a velocidade média.  
**Redistribute timing** redistributes keyframes for a more even average speed.

---

## Loop Closure

`loop_closure = auto` pode ancorar o último frame ao primeiro quando a trajetória é compatível.  
`loop_closure = auto` can anchor the last frame to the first when the path is compatible.

### Liga / ON

- Freeze Frame
- câmera em `scene coverage | camera path`
- exatamente `+360°` ou `-360°`
- mesma elevação final
- mesma distância final
- imagem conectada

### Desliga / OFF

- `359°`
- `720°`
- Motion Frame
- nova câmera / still-image task
- altura ou distância final diferente
- `loop_closure = off`

**Close Orbit / Fechar volta** ajusta a pose final para fechar a trajetória.  
**Close Orbit** adjusts the final pose to close the path.

---

## Principais controles / Main controls

| Controle | PT | EN |
|---|---|---|
| `ui_language` | Idioma do painel. | UI language. |
| `camera_trajectory` | Keyframes de tempo, azimute, elevação e distância. | Time, azimuth, elevation and distance keyframes. |
| `instruction` | Instrução extra para o prompt. | Extra prompt instruction. |
| `subject_box` | Posição inicial do sujeito na imagem. | Initial subject position in the image. |
| `orbit_direction` | Corrige o sentido enviado ao H3. | Corrects the direction sent to H3. |
| `elevation_range` | Faixa do controle vertical. | Vertical control range. |
| `subject_framing` | Registra close-up, medium ou wide. | Records close-up, medium or wide framing. |
| `minimax_format` | Formato do `minimax_prompt`. | `minimax_prompt` format. |
| `prompt_detail` | Baseline ou contratos estendidos. | Baseline or extended contracts. |
| `runtime_task` | Vídeo ou novo ângulo de imagem. | Video or new still-image angle. |

`subject_framing` não aplica zoom ou crop.  
`subject_framing` does not apply zoom or crop.

---

## Saídas / Outputs

| Saída / Output | Uso / Use |
|---|---|
| `compiled_prompt` | Prompt para H3 Edit |
| `options` | Opções para H3 Edit |
| `minimax_prompt` | Prompt alternativo / native H3 |
| `storyboard_json` | Dados da trajetória / path data |
| `info` | Diagnóstico / diagnostics |
| `length` | Número de frames / frame count |
| `fps` | FPS de saída / output FPS |
| `h3world_actions` | Aproximação textual de pan/tilt |

---

## Limitações / Limitations

- O H3 ainda pode errar ângulo, escala e timing. / H3 can still miss angle, scale and timing.
- A prévia não simula o resultado final. / Preview does not simulate the final result.
- `subject_box` vazio usa a imagem inteira. / Empty `subject_box` uses the full image.
- Motion Frame depende do modelo Ref2VA seguir a ação. / Motion Frame depends on Ref2VA preserving the action.
- `h3world_actions` descreve pan/tilt aproximado, não uma órbita geométrica real. / `h3world_actions` describes approximate pan/tilt, not a true geometric orbit.

---

## Créditos / Credits

Node dos **Bruxos do VFX**.  
Node by **Bruxos do VFX**.

Baseado na integração H3 Edit de [`ethanfel/ComfyUI-MiniMax-H3-Edit`](https://github.com/ethanfel/ComfyUI-MiniMax-H3-Edit).
Camera vocabulary follows MiniMax camera-control conventions.  
O vocabulário de câmera segue as convenções de controle de câmera da MiniMax.
