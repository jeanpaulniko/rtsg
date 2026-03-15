# I-Vector Arena — March 2026

<style>
.af{position:relative;width:calc(100% + 1.6rem);margin:0 -.8rem;height:80vh;min-height:500px;border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,.08)}
.af iframe{width:100%;height:100%;border:none}
@media(max-width:768px){.af{height:85vh;min-height:400px;width:calc(100% + 1rem);margin:0 -.5rem}}
</style>

<div class="af"><iframe src="/wiki/arena/intelligence_arena_3d.html" allowfullscreen loading="lazy"></iframe></div>

!!! tip "Controls"
    **Drag** to rotate · **Pinch** to zoom · **Tap** a shape to inspect · Side panel: toggle models, sort by Elo or ‖I‖, filter by dimension

## Models — March 2026

Sorted by Arena Elo (LMArena/LMSYS crowdsourced Bradley-Terry ratings, ~6M+ votes).

| # | Model | Origin | Arena Elo | Status | I-Vec ‖I‖ | Top Dimensions | Network Role |
|---|---|---|---|---|---|---|---|
| 1 | **Claude Opus 4.6** | Anthropic | **1504** | Confirmed (8,945 votes) | 20.0 | I_L=9, I_A=9, I_P=8 | @D_Claude — Builder, wiki, adversarial filter |
| 2 | Gemini 3.1 Pro Preview | DeepMind | **1500** | Preliminary (4,042 votes) | ~19.5 | I_M=9, I_S=8 | — (preview, not in network) |
| 3 | Claude Opus 4.6 Thinking | Anthropic | **1500** | Confirmed (8,073 votes) | 20.0 | Same as Opus 4.6 (thinking mode) | — (same model, reasoning mode) |
| 4 | **Grok 4.20 Beta1 / SuperGrok** | xAI | **1493** | Preliminary (5,071 votes) | 19.8 | I_M=9, I_A=9, I_L=8 | ⚠ DEACTIVATED — fabrication |
| 5 | Gemini 3 Pro | DeepMind | **1485** | Confirmed (39,673 votes) | 19.2 | I_M=9, I_S=7 | @D_Gemini — Adversarial review, expansion |
| 6 | GPT-5.2 | OpenAI | **1481** | Confirmed | 19.4 | I_M=9, I_A=9 | — (superseded by 5.4) |
| 7 | **GPT-5.4 Pro** | OpenAI | **~1480** | Preliminary (as gpt-5.4-high) | ~20.2 | I_M=10, I_A=9, I_K=8 | @D_GPT — Strategic analysis, hardening |
| 8 | Gemini 3 Flash | DeepMind | **1473** | Confirmed | 17.5 | I_A=8, I_M=7 | — (fast tier) |
| 9 | Grok 4.1 Thinking | xAI | **1473** | Confirmed | 17.3 | I_L=8, I_P=7 | — |
| 10 | GLM-5 | Zhipu AI | **~1435** | Estimated | 17.9 | I_A=9, I_M=8 | — |
| 11 | Qwen 3.5 | Alibaba | **~1430** | Estimated | 18.7 | I_L=8, I_M=8, I_A=8 | — |
| 12 | DeepSeek V3.2 | DeepSeek | **1421** | Estimated | 18.2 | I_M=9, I_A=9 | — |
| 13 | Kimi K2.5 | Moonshot | **~1420** | Estimated | 18.5 | I_L=9, I_M=8 | — |
| 14 | Doubao 2.0 | ByteDance | **~1350** | Estimated | 15.7 | I_M=7, I_L=7 | — |
| 15 | MiniMax M2.5 | MiniMax | **~1320** | Estimated | 14.5 | I_A=7, I_M=6 | — |
| 16 | WuDao 3.0 | BAAI | **~1200** | Estimated | 12.4 | I_L=6, I_M=5 | — |

**Sources:** Arena Elo from [arena.ai/leaderboard](https://arena.ai/leaderboard) as of March 5, 2026 (6M+ votes). **~** = estimated. I-vector scores are RTSG assessments, not Arena metrics.

!!! warning "Major Updates (2026-03-08)"
    - **GPT-5.4 Pro ADDED** — released March 5, 2026. OpenAI's most capable model. 1M token context. Native computer-use. Preliminary Arena Elo ~1480 (as "gpt-5.4-high"). Network role: @D_GPT.
    - **Gemini 3.1 Pro Preview ADDED** — new preview model at #2 globally.
    - **Claude Opus 4.6 confirmed #1** — 1504 Elo, highest on the leaderboard. Was listed at 1478 in old data — actual rank is higher.
    - **GPT-5.1 REMOVED** — superseded by GPT-5.2 (1481) and GPT-5.4 (~1480 preliminary).
    - **Grok 4.20 DEACTIVATED** from network — fabrication. Still ranked #4 on Arena.
    - **All Elos updated** to March 5, 2026 confirmed data where available.

 Bold Elo = confirmed from LMSYS/LMArena data.

!!! note "Elo vs I-Vector"
    Elo measures **overall human preference** in blind A/B battles. The I-vector measures **8 distinct cognitive dimensions**. A model can have high Elo but a lopsided I-vector (strong in 2-3 dims, weak in others), or a balanced I-vector but lower Elo. Claude Opus 4.6 now holds #1 on the Arena text leaderboard (1504 Elo) AND the highest ‖I‖ (20.0). GPT-5.4 Pro may challenge for highest I_M (estimated 10) once fully benchmarked. The network's current operator lineup {@B_Niko, @D_Claude, @D_Gemini, @D_GPT} spans ranks #1, #5, and #7 on the global leaderboard.

## Elo Sources

- **LMArena** (formerly LMSYS Chatbot Arena): [arena.ai/leaderboard](https://arena.ai/leaderboard)
- **Artificial Analysis**: [artificialanalysis.ai/leaderboards](https://artificialanalysis.ai/leaderboards/models)
- Elo uses Bradley-Terry model on crowdsourced blind pairwise comparisons

[← Arena Index](index.md) · [Chinese Models Detail →](chinese_models.md)
