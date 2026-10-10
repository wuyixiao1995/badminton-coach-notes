import os

root = r"D:\my_file\知识库\羽毛球笔记\李宇轩"
reorg = os.path.join(root, "_reorg")
files = []
for course in sorted(os.listdir(root)):
    cdir = os.path.join(root, course)
    if not os.path.isdir(cdir) or course.startswith("_"):
        continue
    dst = os.path.join(cdir, "2-整理稿")
    if not os.path.isdir(dst):
        continue
    for f in sorted(os.listdir(dst)):
        p = os.path.join(dst, f)
        if os.path.isfile(p) and f.endswith(".md") and os.path.getsize(p) > 0:
            files.append(p)
print("整理稿总数:", len(files))
CH = 30
i = 0
k = 0
while k < len(files):
    i += 1
    with open(os.path.join(reorg, f"c{i:02d}.list"), "w", encoding="utf-8") as fh:
        for p in files[k:k + CH]:
            fh.write(p.replace("\\", "/") + "\n")
    k += CH
print("清理工单数:", i)
