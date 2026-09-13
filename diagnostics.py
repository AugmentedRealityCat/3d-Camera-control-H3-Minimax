"""Read-only trajectory diagnostics / Diagnósticos que não modificam a trajetória."""

AXES = ('azimuth', 'elevation', 'distance')

def review_path(path, duration, elevation_limit=30):
    result=[]
    def add(code,pt,en,**data):
        result.append(dict(code=code,pt=pt,en=en,**data))
    moving=[any(abs(b[k]-a[k])>1e-8 for k in AXES) for a,b in zip(path,path[1:])]
    if not any(moving):
        add('static','Trajetória estática: todos os keyframes têm a mesma pose.','Static path: all keyframes have the same pose.')
    for i,(a,b) in enumerate(zip(path,path[1:]),1):
        delta=b['azimuth']-a['azimuth']
        if 0<=a['azimuth']<360 and 0<=b['azimuth']<360 and 180<abs(delta)<360:
            add('crossing',f'Trecho {i}: {a["azimuth"]:g} → {b["azimuth"]:g} pede {delta:g}°. Se pretendia atravessar zero pelo arco curto, use Desenrolar; não corrigimos automaticamente.',f'Segment {i}: {a["azimuth"]:g} → {b["azimuth"]:g} requests {delta:g}°. If you intended the short arc across zero, use Unwrap; no automatic correction.',segment=i)
        if not moving[i-1]:
            add('hold',f'Pausa de câmera: {a["time"]*duration:.2f}–{b["time"]*duration:.2f}s. Em Motion, a ação continua.',f'Camera hold: {a["time"]*duration:.2f}–{b["time"]*duration:.2f}s. In Motion, the action continues.',segment=i)
    if path[-1]['time']<1:
        tail=(1-path[-1]['time'])*duration
        add('tail',f'Pausa final: {tail:.3f}s'+(' (menos de um frame).' if tail<1/24 else '.'),f'Final hold: {tail:.3f}s'+(' (less than one frame).' if tail<1/24 else '.'))
    if any(abs(p['elevation'])>elevation_limit for p in path):
        add('slider','Há elevações além do alcance do slider; os valores salvos foram preservados.','Some elevations exceed the slider range; saved values were preserved.')
    return result

def diagnostic_text(items,english=False):
    return '\n'.join(item['en' if english else 'pt'] for item in items)
