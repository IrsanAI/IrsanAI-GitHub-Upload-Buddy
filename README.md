# IrsanAI-GitHub-Upload-Buddy v1.0.0 final — AndroidProof + Cockpit + AliasManager v3.1

AndroidProof Upload Buddy — immersive Termux cockpit, device-adaptive self-resolution, alias manager, Root-Ascent Method 2030-ready.

## Was ist neu v3.1 repo-aware (final)

- **v3.0**: AndroidProof, dedupliziert Downloads (60 Tage), findet .zip + .html, Cockpit nach ~/irsa_cockpit.html, ZIP Builder
- **v3.1 repo-aware**: Alias `irsa='python ~/irsa_metabuddy.py'` ohne `cd ~` — läuft jetzt IM aktuellen Repo
- **Aliases**: `irsa`, `irsa-live`, `live`, `live-demo` — alle in ~/.bashrc
- **2030 Pattern**: Session First (Dateiauswahl -> Ziel Repo -> Clone/Push), Ports statt hardcoded Pfade (find_download_dirs prüft mehrere Orte), Build+Demo Gate (py_compile)

## Usage

```bash
irsa                # im aktuellen Repo, zeigt letzte 60 Tage ZIPs/HTMLs
irsa-live           # direkt ins LiveShare + Buddy
live                # LiveShare HTTP Server starten
live-demo           # LiveShare Demo
# Im Buddy Menü: 1-10 Datei wählen, a -> Alias Manager (neu:NAME)
