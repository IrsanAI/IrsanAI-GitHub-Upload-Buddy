# IrsanAI 2030 Stack — FINAL v1.0.4 (server.ts grep-verifiziert)

**Datum:** 2026-09-07
**Source of Truth:** src/interfaces/http/server.ts head -n 40 — nur was dort importiert wird = Produkt

## IrsanAI-LiveShare — Produkt vs Scaffold (exakt nach server.ts)

**A) Produkt (live getestet, wirklich in server.ts verdrahtet — head -n 40 bestätigt):**
- Application: SessionApplicationService, TrackingApplicationService, SharingApplicationService, ViewerApplicationService
- Infrastructure: InMemorySessionRepository, InMemoryTrackingRepository, InMemoryShareRepository, InMemoryEventBus, CryptoTokenGenerator, SystemClock, PhotonPlaceSearchProvider (Photon live Suche verifiziert)
- Domain: Position, Session First Draft->Ready->Active->Paused->Completed, IllegalTransitionError, InvalidOrExpiredTokenError
- UI: renderHostPage, renderViewerPage, renderLandingPage, toViewerJson, PersonalityTheme getCopy
- HTTP: Express mit trust-proxy, PORT 3000, LINK_TTL 6h, live Netzwerk getestet
- Build: tsc -p . exit 0 grün

**B) 2030 Scaffold (experimental, nicht verdrahtet — grep null Treffer in server.ts):**
- RoutingService Haversine + Host domain + HostApplicationService + InMemoryHostRepository — nur von Scaffold importiert, nie von server.ts
- TransportPort InMemory/BroadcastChannel/WebSocket — nie von server.ts
- FileSystemSessionRepository (und andere FileSystem* Repos) — existiert, nie von server.ts (server.ts nutzt nur InMemory)
- MapPort TextMap/Leaflet/Google stub + MapApplicationService — null Treffer in server.ts
- McpServer + tools create_session/add_position — Scaffold
- BYOK Ladder LlmPort OllamaProvider + OpenRouterProvider — null Treffer
- AuditTrail FileSystemAuditRepository JSONL hashPrev + EU AI Act Art.53 — null Treffer
- UI Scaffold: LiveViewModel + VanillaRenderer + LiveView.tsx — importieren nur sich selbst (VanillaRenderer + LiveView importieren LiveViewModel, sonst niemand), null Treffer in server.ts, ui/host, ui/viewer, ui/landing

**Beweis:**
grep "RoutingService|HostApplicationService|LiveViewModel|VanillaRenderer|FileSystemSessionRepository|TransportPort|MapPort|McpServer|AuditTrail|OllamaProvider" src/interfaces/http/server.ts => leer
head -n 40 zeigt nur Session/Tracking/Sharing/Viewer + 3 InMemory Repos + Photon + renderHost/Viewer/Landing

**Historie:**
- v1.0.2: Rückfall 1 — FileSystem/Transport/Map/MCP/BYOK/Audit als Produkt
- v1.0.3: Rückfall 1 gefixt, aber Rückfall 2 — Routing/Host/UI falsch in Produkt
- v1.0.4: HIER — nach head -n 40 server.ts exakt getrennt, Produkt nur was wirklich importiert wird

Sign-off: v1.0.4 grep-verifiziert, Build grün, DAD
