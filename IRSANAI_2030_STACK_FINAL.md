# IrsanAI 2030 Stack — FINAL v1.0.2 (korrigiert)

**Produkt (live getestet, verdrahtet in server.ts):**
- Session First Draft->Ready->Active->Paused->Completed
- Domain: RoutingService Haversine, Host domain
- Storage: InMemorySessionRepository (echt benutzt in server.ts) — NICHT FileSystemSessionRepository
- HTTP: Host/Viewer echtes Netzwerk, Photon live, trust-proxy Tunnel Fix
- UI: LiveViewModel + VanillaRenderer + React LiveView

**2030 Scaffold (experimental, nicht verdrahtet — wie README.md):**
- FileSystemSessionRepository existiert aber NICHT in server.ts verdrahtet
- TransportPort InMemory/BroadcastChannel/WebSocket — nur von MapApplicationService, TransportApplicationService, HostApplicationService importiert, nie von server.ts
- MapPort TextMap/Leaflet/Google stub + MapApplicationService — eigenes Modell, unverdrahtet
- McpServer create_session/add_position — Scaffold nicht im HTTP Server
- BYOK Ladder LlmPort Ollama+OpenRouter — existiert unverdrahtet
- AuditTrail FileSystemAuditRepository JSONL hashPrev + EU AI Act Art.53 — Scaffold unverdrahtet

Sign-off: v1.0.3 fix Produkt vs Scaffold getrennt, server.ts nutzt InMemorySessionRepository
