import os

root = r"D:\my_file\知识库\羽毛球笔记\李宇轩"
reorg = os.path.join(root, "_reorg")
os.makedirs(reorg, exist_ok=True)

missing = []
orphan = []
stats = []
for course in sorted(os.listdir(root)):
    cdir = os.path.join(root, course)
    if not os.path.isdir(cdir) or course.startswith("_"):
        continue
    src = os.path.join(cdir, "1-原始转录")
    dst = os.path.join(cdir, "2-整理稿")
    if not os.path.isdir(src):
        continue
    srcs = {}
    for f in sorted(os.listdir(src)):
        p = os.path.join(src, f)
        if os.path.isfile(p):
            if f.lower().endswith(".txt"):
                srcs[os.path.splitext(f)[0]] = p
            else:
                print("非txt源文件:", p)
        else:
            print("子目录:", p)
    outs = set()
    if os.path.isdir(dst):
        for f in sorted(os.listdir(dst)):
            p = os.path.join(dst, f)
            if os.path.isfile(p):
                if f.endswith(".md"):
                    outs.add(os.path.splitext(f)[0])
                else:
                    print("非md产物:", p)
            else:
                print("产物里的子目录:", p)
    miss_here = [srcs[k] for k in srcs if k not in outs]
    missing.extend(miss_here)
    orphan.extend(os.path.join(dst, k + ".md") for k in (outs - set(srcs)))
    stats.append((course, len(srcs), len(outs), len(miss_here)))

print("\n=== 各课统计 (课程 | 源txt | 已产出 | 缺失) ===")
for c, s, o, m in stats:
    print(f"{c}: {s} | {o} | {m}")
print(f"\n源txt总数: {sum(x[1] for x in stats)}, 已产出: {sum(x[2] for x in stats)}, 缺失: {len(missing)}, 孤儿产物: {len(orphan)}")

missing.sort()
with open(os.path.join(reorg, "missing_all.txt"), "w", encoding="utf-8") as fh:
    for p in missing:
        fh.write(p.replace("\\", "/") + "\n")

# 切分为每 20 个一份的补漏工单
CH = 20
i = 0
k = 0
while k < len(missing):
    i += 1
    with open(os.path.join(reorg, f"r{i:02d}.list"), "w", encoding="utf-8") as fh:
        for p in missing[k:k + CH]:
            fh.write(p.replace("\\", "/") + "\n")
    k += CH
print(f"生成补漏工单数: {i}")
for n in range(1, i + 1):
    p = os.path.join(reorg, f"r{n:02d}.list")
    print(f"  r{n:02d}: {sum(1 for _ in open(p, encoding='utf-8'))} 篇")
if orphan:
    print("\n孤儿产物样例:", orphan[:5])
