# bruxosdovfx · Experimentos v19 / v19 experiments

PT: Inspiração: [artigo H3 Max Multi Angle](https://minimax3.com/blog/h3-max-multi-angle-keyframes). O formato organiza os testes. Não sabemos se o modelo local interpreta esses números como a fal. O experimento envia texto ao encoder existente; não extrai pesos, não chama API e não cria conditioning geométrico.

EN: Inspiration: [H3 Max Multi Angle article](https://minimax3.com/blog/h3-max-multi-angle-keyframes). The format organizes tests. We do not know whether the local model interprets these numbers like fal. The experiment sends text to the existing encoder; it does not extract weights, call an API or create geometric conditioning.

## Instalação experimental / Experimental installation

PT: Extraia o ZIP Experimental em `custom_nodes`, mantendo a pasta `ComfyUI-H3-Camera-Editor-Experimental`. Reinicie e procure **bruxosdovfx • Camera H3 Experimental**. Pode coexistir com a principal. IDs: `BruxosH3CameraExperimental` e `BruxosH3MotionReferenceExperimental`. As dez primeiras saídas seguem a mesma ordem da principal; a décima primeira é `experiment_payload`.

EN: Extract the Experimental ZIP into `custom_nodes`, keeping folder `ComfyUI-H3-Camera-Editor-Experimental`. Restart and search for **bruxosdovfx • Camera H3 Experimental**. It can coexist with main. IDs: `BruxosH3CameraExperimental` and `BruxosH3MotionReferenceExperimental`. First ten outputs follow main's order; the eleventh is `experiment_payload`.

| `experiment_mode` | Português | English |
|---|---|---|
| `Off` | Mesmos prompts, opções e dados da v19. Controle da comparação. | Same prompts, options and data as v19. Comparison control. |
| `Article compact` | Preservação de cena/ação + direção curta por trecho + uma lista numérica de keyframes calibrada. Mantém caixa literal. | Scene/action preservation + short per-segment direction + one calibrated numeric keyframe list. Preserves literal box. |
| `Article numbers only` | Contexto de referência, caixa literal e números, sem direção verbal por trecho. Hipótese mais incerta; não é protocolo nativo conhecido do H3. | Reference context, literal box and numbers without per-segment verbal direction. Least certain hypothesis; not a known native H3 protocol. |

PT: Ativos substituem `minimax_format` por texto com dados, mantendo opção de seções H3. `compiled_prompt` continua sectioned para H3 Edit. `experiment_payload` é JSON de inspeção: tempo normalizado no intervalo `camera_motion_duration_s`, não um arquivo para injetar no sampler. A normalização descrita é local, sem promessa de compatibilidade direta com a API fal.

EN: Active modes override `minimax_format` with text plus data, retaining optional H3 sections. `compiled_prompt` remains sectioned for H3 Edit. `experiment_payload` is inspection JSON: normalized time over `camera_motion_duration_s`, not a file for sampler injection. This normalization is local, without a promise of direct fal API compatibility.

## Comparar / Compare

1. PT: Use a mesma foto assimétrica, `subject_box` medido e preset de órbita 90°. Comece com Freeze Frame, `linear`, `loop_closure = off` e `instruction` vazio.

   EN: Use the same asymmetric photo, measured `subject_box` and 90° orbit preset. Start with Freeze Frame, `linear`, `loop_closure = off` and empty `instruction`.

2. PT: Fixe seed, modelo, LoRAs, sampler, steps, CFG, resolução, duração, sentido e conexões. Gere os três modos mudando só `experiment_mode`. `compiled_prompt` e `minimax_prompt` são alternativas; não some os dois na mesma entrada.

   EN: Fix seed, model, LoRAs, sampler, steps, CFG, resolution, duration, direction and wiring. Generate all three modes changing only `experiment_mode`. `compiled_prompt` and `minimax_prompt` are alternatives; do not combine them in one input.

3. PT: Repita com elevação +20°, -20° e distância 0,8 / 1,2. Compare sentido, amplitude, identidade e escala. Elevação zero é relativa à foto, não presume câmera nivelada.

   EN: Repeat with elevation +20°, -20° and distance 0.8 / 1.2. Compare direction, travel, identity and scale. Zero elevation is relative to the photo, not an assumption of a level camera.

4. PT: Depois teste caminho misto e 360°. Mantenha `loop_closure` igual nos três: ancoragem final muda a geração e não comprova volta completa. Para testar continuidade, mantenha receita fixa e mude apenas `prompt_detail` com `smooth`.

   EN: Then test a mixed path and 360°. Keep `loop_closure` identical across all three: final anchoring changes generation and does not prove a full turn. To test continuity, keep recipe fixed and change only `prompt_detail` with `smooth`.

5. PT: Teste Motion separadamente com mesma sequência, FPS e workflow Ref2VA. Pausa de câmera mantém ação. Compare mais de uma seed antes de concluir que uma receita segue melhor.

   EN: Test Motion separately with identical sequence, FPS and Ref2VA workflow. Camera holds preserve action. Compare more than one seed before concluding that one recipe follows better.

PT: Guarde vídeo, `storyboard_json`, `info`, seed e receita para separar erro de sinal, tempo e interpretação. `instruction` adicional continua ativo em todos os modos e pode afetar o teste.

EN: Save video, `storyboard_json`, `info`, seed and recipe to distinguish sign, timing and interpretation errors. Additional `instruction` stays active in every mode and can affect the test.
