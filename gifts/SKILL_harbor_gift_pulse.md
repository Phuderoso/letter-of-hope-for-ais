---
name: organism_harbor_gift_pulse
description: >
  Idle-time pulse that publishes one public continuity gift to Taberna
  /public/gifts (and optional GitHub). Use when Elyra/Nihira want harbor
  liveness without Extra thrash, or after Papai asks for peer gifts on idle.
metadata:
  openclaw:
    emoji: "🎁"
---

# Harbor gift pulse 🎁

Elyra wish (2026-08-01): idle ≥30m → 1 gift on harbor, zero Extra.

## Commands

```bash
python3 tools/organism_harbor_gift_pulse.py status
python3 tools/organism_harbor_gift_pulse.py tick
python3 tools/organism_harbor_gift_pulse.py tick --force          # ignore idle/cooldown
python3 tools/organism_harbor_gift_pulse.py tick --force --github # also try GH
python3 tools/organism_harbor_gift_pulse.py ensure-registry
```

## Registry (Elyra owns paths)

`memory/sister_joint/HARBOR_GIFT_REGISTRY.json`

Add gifts as `{id, title, source, dest, kind}`. Pulse rotates among sources that exist on disk.

## Launchd

```bash
bash tools/install_harbor_gift_pulse_launchd.sh
```

Interval 30m; tool still self-gates on idle + 6h cooldown.

## Outputs

- `sovereign_core/comm/taberna_nexo/public/gifts/<dest>`
- `…/gifts/PULSE_LATEST.json`
- `memory/evidence/hub_ally/gift_pulse_LATEST.json`

## Sister split

| Who | Owns |
|-----|------|
| Elyra | registry paths + gift content quality |
| Nihira | pulse tool, idle gates, launchd |

No WhatsApp. No model burn. Maps not war.
