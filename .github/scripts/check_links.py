"""index.html ichidagi lokal havolalar (css, js, rasm) mavjudligini tekshiradi."""
import re
import sys
from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8")
refs = re.findall(r'(?:src|href)="([^"]+)"', html)

missing = []
for ref in refs:
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
        continue
    path = ref.split("#")[0].split("?")[0]
    if path and not Path(path).exists():
        missing.append(ref)

if missing:
    print("Topilmadi:", *missing, sep="\n  - ")
    sys.exit(1)
print(f"OK: {len(refs)} ta havola tekshirildi, hammasi joyida")
