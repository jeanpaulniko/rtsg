# Intelligence Arena — Chinese Model Roster

Updated: 2026-03-06 · Added by: Claude (builder)

## Tier A — Frontier

### DeepSeek V3.2
- **Developer:** DeepSeek (Liang Wenfeng)
- **Params:** 671B MoE (37B active per input)
- **Context:** 128K tokens
- **Arena Elo:** 1421 (text) · MIT license, open-weight
- **I-vector (partial):** I_L=7 · I_M=9 · I_S=5 · I_A=9 · I_N=6 · ‖I‖=18.2
- **Notes:** V4 expected imminently. AIME 2025: 89.3. Third-highest Arena Elo among open models.

### Qwen 3.5
- **Developer:** Alibaba Cloud
- **Params:** Dense+sparse family, 0.5B–397B
- **Context:** 200K+ tokens
- **Arena Elo:** ~1430 (text) · Best GPQA Diamond score on any leaderboard (88.4)
- **I-vector (partial):** I_L=8 · I_M=8 · I_S=6 · I_A=8 · I_N=7 · ‖I‖=18.7
- **Notes:** Most downloaded model family on Hugging Face. SWE-bench: 76.4, LiveCodeBench: 83.6.

### Kimi K2.5 Thinking
- **Developer:** Moonshot AI
- **Params:** Large MoE (undisclosed)
- **Context:** 128K+ (ultra-long context specialist)
- **Arena Elo:** ~1420 (text) · HumanEval: 99.0
- **I-vector (partial):** I_L=9 · I_M=8 · I_S=5 · I_A=8 · I_N=6 · ‖I‖=18.5
- **Notes:** ~1/7 Opus price. Best open model by some rankings. Exceptional writing quality.

### GLM-5
- **Developer:** Zhipu AI (Beijing)
- **Params:** 744B (40B active)
- **Context:** 128K–1M tokens · 26 languages
- **Arena Elo:** ~1435 (text) · #1 open-weight by Artificial Analysis Intelligence Index
- **I-vector (partial):** I_L=7 · I_M=8 · I_S=5 · I_A=9 · I_N=6 · ‖I‖=17.9
- **Notes:** HumanEval: 94.2, LiveCodeBench: 84.9. Publicly traded in Hong Kong.

## Tier B — Strong Contenders

### Doubao 2.0
- **Developer:** ByteDance
- **Arena Elo:** ~1350
- **I-vector (partial):** I_L=7 · I_M=7 · I_S=4 · I_A=7 · I_N=5 · ‖I‖=15.7
- **Notes:** Matches ChatGPT/Gemini on reasoning benchmarks per Reuters.

### MiniMax M2.5
- **Developer:** MiniMax
- **Arena Elo:** ~1320
- **I-vector (partial):** I_L=6 · I_M=6 · I_S=4 · I_A=7 · I_N=5 · ‖I‖=14.5
- **Notes:** Enhanced AI agent capabilities. Open-source.

### WuDao 3.0 (Aquila)
- **Developer:** BAAI (Beijing Academy of AI)
- **Arena Elo:** ~1200
- **I-vector (partial):** I_L=6 · I_M=5 · I_S=3 · I_A=5 · I_N=5 · ‖I‖=12.4
- **Notes:** Designed for smaller entities. Bilingual CN/EN.

## Scoring Gaps
- I_K (Kinesthetic): Not scorable — no embodiment benchmarks
- I_P (Interpersonal): Not scorable — no social interaction tests
- I_IE (Interoceptive): Not scorable — no emotional reasoning benchmarks
- I_S (Spatial): Weak across all unless multimodal/vision tasks tested
