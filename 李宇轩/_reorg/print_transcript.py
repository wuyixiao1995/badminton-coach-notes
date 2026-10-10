import sys
p = sys.argv[1]
with open(p, encoding='utf-8') as f:
    sys.stdout.write(f.read())
