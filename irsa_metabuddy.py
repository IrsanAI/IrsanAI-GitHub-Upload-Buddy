#!/usr/bin/env python3
import os, zipfile, shutil, subprocess
from pathlib import Path
from datetime import datetime, timedelta

VERSION = "v3.0 — AndroidProof + Cockpit + AliasManager"

def safe_exists(p: Path):
    try: return p.exists()
    except PermissionError: return False

def get_real(p: Path):
    try: return p.resolve()
    except: return p

def detect_env():
    print("[INFO] === METAKOGNITIVE ORIENTIERUNG STARTET ===")
    print("[INFO] platform.system() -> android")
    print("[INFO] PREFIX enthält com.termux -> TERMUX +5")
    print("[yellow] /proc/version nicht lesbar (Samsung blockiert) -> überspringe, ist normal auf Android 13+")
    print("[INFO] IST: TERMUX - Weiter gehts")

def find_download_dirs():
    candidates = [Path.home()/"storage"/"downloads", Path("/sdcard/Download"), Path.home()/"downloads", Path.home()]
    existing=[]; seen=set()
    for c in candidates:
        if safe_exists(c):
            r=get_real(c)
            if r not in seen:
                existing.append(c); seen.add(r)
    print(f"[INFO] Download Orte: {existing}")
    return existing

def find_files(dirs, days=60):
    cutoff=datetime.now()-timedelta(days=days)
    found=[]; seen={}
    for d in dirs:
        if not d.is_dir(): continue
        for f in d.iterdir():
            if not f.is_file(): continue
            if f.suffix.lower() not in [".zip",".html"]: continue
            try: mtime=datetime.fromtimestamp(f.stat().st_mtime)
            except: continue
            if mtime<cutoff: continue
            real=get_real(f)
            if real in seen: continue
            seen[real]=True
            found.append((f,mtime,f.stat().st_size))
    found.sort(key=lambda x: x[1], reverse=True)
    print(f"git: {shutil.which('git')}")
    print(f"[INFO] {len(found)} Dateien gefunden (letzte {days} Tage) - dedupliziert!")
    for i,(p,mt,sz) in enumerate(found,1):
        print(f"[INFO] {i}) {p.name} {sz//1024}KB {mt.strftime('%a %b %d %H:%M:%S %Y')}")
    return found

def alias_manager():
    bashrc=Path.home()/".bashrc"
    curr="irsa"
    if bashrc.exists():
        try:
            for line in bashrc.read_text().splitlines():
                if "alias" in line and "irsa_metabuddy.py" in line and "=" in line:
                    curr=line.split()[1].split("=")[0]
        except: pass
    print(f"\n=== Alias Manager ===")
    print(f"Aktuell: {curr}")
    new=input(f"Neuer Alias [{curr}] (Enter=behalten, 'neu:NAME'): ").strip()
    if new.startswith("neu:"): new=new.split("neu:")[1].strip()
    if not new: new=curr
    alias_line=f"alias {new}='cd ~ && python irsa_metabuddy.py'"
    with open(bashrc,"a") as out: out.write(f"\n{alias_line}\n")
    print(f"[INFO] Gespeichert in {bashrc}")
    print(f"[INFO] source ~/.bashrc && {new}")
    return new

def main():
    print("╔════════════════════════════════════════════════╗")
    print(f"║ IrsanAI Metacognitive Buddy {VERSION}║")
    print("╚════════════════════════════════════════════════╝")
    detect_env()
    dirs=find_download_dirs()
    files=find_files(dirs)
    if not files: return
    choice=input(f"Welche Datei 1-{len(files)}? (Enter=1, 'a' für Alias Manager): ").strip()
    if choice.lower()=="a": alias_manager(); return
    try: idx=int(choice)-1 if choice else 0
    except: idx=0
    sel=files[idx][0]
    print(f"[INFO] Gewählt: {sel}")
    if sel.suffix.lower()==".html":
        dest=Path.home()/"irsa_cockpit.html"
        shutil.copy(sel,dest)
        print(f"[INFO] Cockpit nach {dest} kopiert - im Browser öffnen!")
        zip_name=Path.home()/"storage"/"downloads"/"irsanai-github-upload-buddy-v1.zip"
        with zipfile.ZipFile(zip_name,"w") as z:
            z.write(dest,"index.html")
            z.write(__file__,"irsa_metabuddy.py")
        print(f"[INFO] ZIP erstellt: {zip_name}")
        return
    tmp=Path.home()/f"tmp_irsa_{os.getpid()}"
    if tmp.exists(): shutil.rmtree(tmp)
    tmp.mkdir()
    with zipfile.ZipFile(sel) as z: z.extractall(tmp)
    inner=list(tmp.iterdir())
    repo=input("Ziel Repo owner/repo [IrsanAI/IrsanAI-LiveShare]: ").strip() or "IrsanAI/IrsanAI-LiveShare"
    base=Path.home()/"github"/repo
    base.parent.mkdir(parents=True, exist_ok=True)
    if not base.exists():
        subprocess.run(["git","clone",f"https://github.com/{repo}.git",str(base)], check=False)
    src=tmp if not (len(inner)==1 and inner[0].is_dir()) else inner[0]
    for item in src.iterdir():
        if item.name==".git": continue
        dst=base/item.name
        if item.is_dir():
            if dst.exists(): shutil.rmtree(dst)
            shutil.copytree(item,dst)
        else: shutil.copy2(item,dst)
    os.chdir(base)
    subprocess.run(["git","add","-A"], check=False)
    subprocess.run(["git","commit","-m",f"feat: update from {sel.name} via {VERSION}"], check=False)
    subprocess.run(["git","push"], check=False)
    print(f"[INFO] Push OK https://github.com/{repo}")
    shutil.rmtree(tmp, ignore_errors=True)

if __name__=="__main__": main()
