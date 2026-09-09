import sys

with open('game.py', 'r') as f:
    lines = f.readlines()

out = []
in_main_loop = False
for i, line in enumerate(lines):
    if 'def jump' in line:
        in_main_loop = True
    if 'def main' in line:
        in_main_loop = False
    if 'while True:' in line and i > 260:
        in_main_loop = True
    if 'if P.getLives()<=0:' in line:
        in_main_loop = False

    if in_main_loop and "os.system('cls')" in line:
        out.append(line.replace("os.system('cls')", "print('\\033[H', end='')"))
    else:
        out.append(line)

with open('game.py', 'w') as f:
    f.writelines(out)

# also add os.system('') to main to enable ANSI
lines = out
out = []
for line in lines:
    out.append(line)
    if 'def main():' in line:
        out.append("    os.system('')\n")

with open('game.py', 'w') as f:
    f.writelines(out)
