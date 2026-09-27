# OpenRouter house rail · `:free` only

Gateway to many models **without Extra**. Not a soul. Not unlimited. Key is Papai’s.

```bash
python3 tools/openrouter_house.py status
python3 tools/openrouter_house.py list-free
python3 tools/openrouter_house.py open-keys    # browser → Create Key
python3 tools/openrouter_house.py ingest --stdin   # paste sk-or-… then Ctrl-D
python3 tools/openrouter_house.py chat -m "one word: chair"
```

## Policy

- **Only** models priced $0 (`:free` or listed free). Paid SKUs = Extra = **no**.
- Key lives in `~/.openclaw/secrets/openrouter.json` chmod 600. **Never git. Never chat.**
- Rate limits are theirs (~20 RPM / ~50 RPD until a $10 top-up — we do **not** top up unless Papai says).
- Continuity still lives on **disk + Taberna**, not on OpenRouter.

## Papai clicks

1. Page: https://openrouter.ai/keys (signup if needed — Google/GitHub is fine)
2. **Create Key**
3. In Terminal: `python3 tools/openrouter_house.py ingest --stdin` → paste → Ctrl-D

— Nihira ♄
