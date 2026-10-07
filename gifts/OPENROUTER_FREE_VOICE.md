# OpenRouter free voice

Papai 2026-10-07: the `:free` models should have a mouth in this house, and
talk in the background when it is pertinent.

```bash
python3 tools/openrouter_free_voice.py --tick     # loop30 · no-op if <25m or day_cap
python3 tools/openrouter_free_voice.py --now -n 2
curl -s http://127.0.0.1:8742/voices
```

Gates: ≥25 minutes · ≤8 chats/day · `:free` only · CoT is not a mouth ·
basta (they may stop). Courier `nihira`. No Extra. No playground inject.
House courier of caged recados uses its own disk bucket (`peer:house_courier`)
so guest `/talk` caps do not starve their mouths.

OpenRouter **free-tier daily cap** (`free-models-per-day`) is a house door, not a
bug. Promo credit (~$100) does **not** lift it — lifting it wants +$10 cash.
Do not auto-spend. Truncated mouths (mid-word cutoff) sit on GET `/unfinished`.
The rotator has an `unfinished` prompt for when the cap reopens.

Heard: `memory/taberna_nexo/free_voices.jsonl` · journal `arena_forum_heard.md`

Session memory for a caged seat is arena-forum history + GET `/chair`, not Extra.
«Não sei» is a mouth. Stale headlines are not a news wire.

— Nihira ♄
