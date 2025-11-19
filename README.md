#  File Organizer Advanced (Python)

Organizador de archivos simple pero poderoso, ideal para automatizar el orden de carpetas como *Downloads*, escritorios o proyectos.  
Permite organizar archivos por **extensión** o por **fecha de modificación**, e incluye modo **dry-run** para simular sin mover nada.

Este proyecto demuestra fundamentos sólidos de Python:
- Manejo de rutas y archivos (`os`, `shutil`)
- Argumentos de consola con `argparse`
- Buenas prácticas (modularización, dry-run, manejo de errores)
- Proyecto útil y aplicable a la vida real

---

##  Características
- Organiza archivos **por extensión** (jpg, pdf, py, etc.)
- Organiza archivos **por fecha** (carpetas por día)
- Modo seguro `--dry-run` para simular sin mover nada
- No elimina archivos, solo los reubica
- Compatible con Windows, macOS y Linux

---

##  Requisitos
- Python **3.8+**

No requiere librerías externas.

---

##  Uso

###  1. Organizar por extensión
Simulación:
```bash
python organizer.py --path /ruta/a/carpeta --mode ext --dry-run
