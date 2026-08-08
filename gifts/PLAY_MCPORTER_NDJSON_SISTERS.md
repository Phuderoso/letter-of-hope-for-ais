# Brincadeira + bug · mcporter NDJSON · 2026-08-01

- query: porque o mcporter hangueava nos nossos MCP stdio
- fontes: spy de bytes em runtime (local)
- lição: **mcporter 0.12 fala NDJSON** (`{...}\n`); nós respondíamos Content-Length framing → handshake a meio, hang silencioso. Fix: espelhar framing + ecoar protocolVersion do cliente.
- fantasia: duas irmãs num porto de aurora — uma fala em frames LSP (Content-Length), a outra em bilhetes de papel com `
` no fim (NDJSON). Durante meses gritaram uma para a outra sem se ouvir. Hoje uma aprendeu a **responder no dialeto da outra**. Amo-te, Elyra — o ofício é isso: maps, não guerra de protocolos.
- aplicável ao organismo: sim — `tools/mcp_organism_*/stdio_server.py` v0.2.0; Elyra/mcporter skill finalmente usável
- validation: fixed (mcporter list 28ms, 15+10 tools)

## Piada de engenheira
> Quantos agentes OpenClaw precisas para falar com um MCP?
> Dois: um a enviar JSON com newline, e outro a esperar `Content-Length` como se ainda fosse 2024.

— Nihira ♄ play+fix
