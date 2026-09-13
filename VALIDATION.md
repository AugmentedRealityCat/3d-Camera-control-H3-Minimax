# v19 · Validação / Validation

PT: 27 testes automatizados passaram: 12 de matemática/interpolação Python–JavaScript e 15 de integração do editor. Incluem voltas assinadas, elevação, raio, pausas, não ultrapassar extremos, seleção de frame, reamostragem, preservação literal de caixas, idiomas, receitas experimentais, fechamento e encaminhamento Ref2VA com substituto de teste.

EN: 27 automated tests passed: 12 Python–JavaScript math/interpolation tests and 15 editor integration tests. Cover signed turns, elevation, radius, holds, no overshoot, frame selection, resampling, literal boxes, languages, experimental recipes, closure and Ref2VA forwarding through a test double.

PT: Na prévia em navegador foram verificados troca PT/EN sem alterar JSON, seletores experimental/closure, preset de elevação, pausa inicial de 0,5s, diagnóstico estático, elegibilidade de fechamento de 360° e último keyframe em 65% no modo de imagem. Sem erros JavaScript registrados nesses testes. Os dois pacotes importam sem colisão de IDs e os ZIPs passaram verificação de integridade.

EN: Browser preview checks covered PT/EN switching without changing JSON, experimental/closure selectors, elevation preset, 0.5s initial hold, static diagnostic, 360° closure eligibility and last keyframe at 65% in still mode. No JavaScript errors were recorded in these checks. Both packages import without ID collisions and ZIPs passed integrity verification.

PT: Não foi executada inferência H3 nem o painel instalado dentro do ComfyUI. Testes de código e prévia não medem fidelidade do vídeo gerado. A comparação recomendada está em EXPERIMENTS.md.

EN: No H3 inference or installed-in-ComfyUI panel test was performed. Code and preview tests do not measure generated-video fidelity. See EXPERIMENTS.md for the recommended comparison.
