import os, re

base = "D:/my_file/知识库/羽毛球笔记/李宇轩/【致命吊球1-45节】/1-原始转录"
out = "D:/my_file/知识库/羽毛球笔记/李宇轩/_reorg/_work08_combined.txt"

files = [
    "01.通告.txt",
    "02.吊球基本功（介绍&握拍）.txt",
    "03.吊球基本2（挥拍）.txt",
    "04.吊球基本功3（转身动作）.txt",
    "05.简单吊球（动作&节奏&空间）.txt",
    "06.简单吊球（训练计划）.txt",
    "07.正手劈吊对角1（劈球落点）.txt",
    "08.正手劈吊对角2（切球方法）.txt",
    "09.正手劈吊对角3（劈球挥拍方法）.txt",
    "10.正手劈对角4（转身动作）.txt",
    "11.正手劈吊对角5（训练计划）.txt",
    "12.正手劈对角6（怎么吊得隐蔽）.txt",
    "13.正手劈对角7（不同握拍怎么劈）.txt",
    "14.正手劈对角（不转身劈吊）.txt",
    "15.头顶劈吊直线1.txt",
    "16.头顶劈吊直线2（空间感+顶腰）.txt",
    "17.头顶劈吊直线3（各种要点和示范）.txt",
    "18.头顶劈吊直线4（训练计划）.txt",
    "19.头顶滑板吊对角1.txt",
    "20.头顶滑板吊对角2（挥拍细节）.txt",
    "21.头顶滑板吊对角3（切球细节动作）.txt",
    "22._头顶滑板吊对角4（节奏&空间感）.txt",
    "23._头顶滑板吊对角5（重要点与示范）.txt",
    "24._头顶滑板吊对角6（不同握法怎么滑板）.txt",
    "25._头顶滑板吊对角7（训练计划）.txt",
]

MAX = 1700
break_re = re.compile(r'[\s，。！？、；：,.!?;:\n（）()""\'\']')

def chunk(text):
    lines = []
    buf = ""
    for ch in text:
        buf += ch
        if len(buf) >= MAX:
            # try to break at a nearby boundary going backwards
            cut = len(buf)
            for i in range(len(buf)-1, max(len(buf)-120, -1), -1):
                if break_re.match(buf[i]):
                    cut = i+1
                    break
            lines.append(buf[:cut])
            buf = buf[cut:]
    if buf:
        lines.append(buf)
    return lines

with open(out, "w", encoding="utf-8") as fo:
    for f in files:
        fo.write("\n\n==========FILE " + f + "==========\n\n")
        with open(os.path.join(base, f), "r", encoding="utf-8") as fi:
            text = fi.read()
        for ln in chunk(text):
            fo.write(ln + "\n")

print("done", len(files))
print("out lines:")
print(sum(1 for _ in open(out, encoding="utf-8")))
