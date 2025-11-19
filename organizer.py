#!/usr/bin/env python3
"""
Organizador de archivos por extensión o por fecha.
Uso:
  python organizer.py --path /ruta/a/carpeta [--mode ext|date] [--dry-run]

Ejemplos:
  python organizer.py --path ~/Downloads --mode ext --dry-run
  python organizer.py --path /home/ed/Downloads --mode date
"""
import argparse
import os
import shutil
from datetime import datetime

def by_extension(directory, dry_run=False):
    moved = 0
    for fname in os.listdir(directory):
        fpath = os.path.join(directory, fname)
        if os.path.isfile(fpath):
            parts = fname.rsplit(".", 1)
            ext = parts[1].lower() if len(parts) > 1 else "no_extension"
            target_dir = os.path.join(directory, ext)
            os.makedirs(target_dir, exist_ok=True)
            dest = os.path.join(target_dir, fname)
            if dry_run:
                print(f"[DRY] Mover: {fpath} -> {dest}")
            else:
                try:
                    shutil.move(fpath, dest)
                except Exception as e:
                    print(f"[ERROR] al mover {fpath}: {e}")
            moved += 1
    return moved

def by_date(directory, dry_run=False, date_format="%Y-%m-%d"):
    moved = 0
    for fname in os.listdir(directory):
        fpath = os.path.join(directory, fname)
        if os.path.isfile(fpath):
            mtime = os.path.getmtime(fpath)
            folder = datetime.fromtimestamp(mtime).strftime(date_format)
            target_dir = os.path.join(directory, folder)
            os.makedirs(target_dir, exist_ok=True)
            dest = os.path.join(target_dir, fname)
            if dry_run:
                print(f"[DRY] Mover: {fpath} -> {dest}")
            else:
                try:
                    shutil.move(fpath, dest)
                except Exception as e:
                    print(f"[ERROR] al mover {fpath}: {e}")
            moved += 1
    return moved

def parse_args():
    p = argparse.ArgumentParser(description="Organiza archivos por extensión o por fecha.")
    p.add_argument("--path", required=True, help="Ruta de la carpeta a organizar")
    p.add_argument("--mode", choices=["ext", "date"], default="ext", help="Modo: ext (por extensión) o date (por fecha de modificación)")
    p.add_argument("--dry-run", action="store_true", help="Simular cambios sin mover archivos")
    return p.parse_args()

def main():
    args = parse_args()
    directory = os.path.abspath(args.path)
    if not os.path.isdir(directory):
        print("Error: la ruta no existe o no es carpeta:", directory)
        return
    if args.mode == "ext":
        moved = by_extension(directory, dry_run=args.dry_run)
    else:
        moved = by_date(directory, dry_run=args.dry_run)
    print(f"Operación finalizada. Archivos procesados: {moved}")

if __name__ == "__main__":
    main()
