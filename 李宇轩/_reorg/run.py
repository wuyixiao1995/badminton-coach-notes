# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from clean import build_md, title_from_path

LIST = r"D:/my_file/知识库/羽毛球笔记/李宇轩/_reorg/worker13.list"
ok = 0
total = 0
failed = []
with open(LIST, 'r', encoding='utf-8') as f:
    lines = [l.strip() for l in f if l.strip()]

for src in lines:
    total += 1
    try:
        with open(src, 'r', encoding='utf-8', errors='ignore') as fh:
            raw = fh.read()
        title = title_from_path(src)
        md = build_md(title, raw)
        out_dir = os.path.join(os.path.dirname(os.path.dirname(src)), '2-整理稿')
        os.makedirs(out_dir, exist_ok=True)
        base = os.path.splitext(os.path.basename(src))[0] + '.md'
        out_path = os.path.join(out_dir, base)
        with open(out_path, 'w', encoding='utf-8') as fh:
            fh.write(md)
        ok += 1
        print(f'OK  {out_path}')
    except Exception as e:
        failed.append((os.path.basename(src), str(e)))
        print(f'FAIL {src}: {e}')

print(f'\n完成{ok}/总数{total}')
if failed:
    for name, err in failed[:10]:
        print(name)
