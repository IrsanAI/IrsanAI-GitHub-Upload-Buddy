# IrsanAI 2030 Stack — FINAL v1.0.0

**Datum:** 2026-09-07
**Status:** Beide Repos verifiziert, Build grün, Tag v1.0.0 gepusht
**Methode:** Root-Ascent v0.4 + Claude Verifikation + DAD
**Zieljahr:** 2030 — code4future

## Repos im Stack

### IrsanAI-LiveShare v1.0.0 final — Produkt
- Pfad: ~/github/IrsanAI/IrsanAI-LiveShare
- Tag: v1.0.0 (04e8336)
- Vorgänger: v0.5.3 docs verifiziert, v0.5.2 CLEAN MERGE verifiziert von Claude
- Stack: RoutingService (Haversine), Host domain, TransportPort (InMemory/BroadcastChannel/WebSocket), FileSystemSessionRepository, MapPort TextMap/Leaflet/Google stub, LiveViewModel, McpServer, BYOK Ladder Ollama+OpenRouter, AuditTrail JSONL hashPrev chain + EU AI Act Art.53
- Verifikation Claude: HTTP Host/Viewer echt getestet, Photon Suche live, trust-proxy Tunnel Fix, Build grün ohne ts-nocheck
- v1.0.0 Cleanup: package.json 0.1.0->0.5.3 synced, cockpits raus nach ~/storage/downloads/cockpits/,.gitignore *.html

### IrsanAI-GitHub-Upload-Buddy v1.0.0 final — Werkzeug
- Pfad: ~/github/IrsanAI/IrsanAI-GitHub-Upload-Buddy
- Tag: v1.0.0 (16dced4)
- v3.0: AndroidProof (Samsung /proc/version übersprungen), dedupliziert 60 Tage,.zip+.html, Cockpit ~/irsa_cockpit.html
- v3.1 repo-aware: alias irsa='python ~/irsa_metabuddy.py' ohne cd ~, läuft IM Repo
- Build Gate: python -m py_compile grün

## 2030 Pattern — Template (nicht kopieren, neu anwenden)

1. Session First: Draft->Ready->Active->Paused->Completed, illegale Transition wirft Fehler
2. Ports statt Provider: MapPort, TransportPort, StoragePort, LlmPort, AuditPort — Provider austauschbar
3. Build+Demo Gate: npm run build + npm run demo MUSS grün bevor "fertig", py_compile MUSS grün
4. Keine Scaffolds kopieren — Pattern neu anwenden (Claude Hinweis)

DAD: demütig anständig diszipliniert — Mensch Supervisor + Agent Executor

## Aliases v3.1 repo-aware

alias irsa='python ~/irsa_metabuddy.py'
alias irsa-live='cd ~/github/IrsanAI/IrsanAI-LiveShare && python ~/irsa_metabuddy.py'
alias live='cd ~/github/IrsanAI/IrsanAI-LiveShare && npm run build && node dist/interfaces/http/server.js'
alias live-demo='cd ~/github/IrsanAI/IrsanAI-LiveShare && npm run demo'

## Verifikation Checkliste

- [x] LiveShare v0.5.2 CLEAN MERGE verifiziert von Claude
- [x] v0.5.3 docs — 17 Pfade existieren
- [x] v1.0.0 final — Build + Demo grün
- [x] Buddy v3.1 repo-aware, py_compile grün, v1.0.0 final
- [x] Beide HEAD = v1.0.0, origin up to date
- [x] cockpits cleanup,.gitignore

## Lessons Learned

Samsung PermissionError -> AndroidProof, Doppel-Download Bug -> dedupliziert nach real path, v0.5.1 falsches GAP CLOSED -> Build Gate, cd ~ im Alias -> repo-aware v3.1

Sign-off: 2026-09-07 Termux AndroidProof, beide v1.0.0 final, Build grün, verifiziert von Claude, repo-aware irsa v3.1
