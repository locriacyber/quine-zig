import sys

s = sys.stdin.read()

print("const st = [_]u8{")
for c in s:
    if c == "\n":
        c = "\\n"
    if c == "'":
        c = "\\'"
    if c == "\\":
        c = "\\\\"
    print(f"'{c}',", end="")
print()
print("};")