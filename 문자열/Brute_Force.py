string = "This is a book"
pattern = "is"

s, p = 0, 0

while p < len(pattern) and s < len(string):
    print(s, p)
    if string[s] != pattern[p]:
        s -= p
        p -= 1

    # else?
    s += 1
    p += 1

print(f'END = {s, p}')
if p == len(pattern):
    print(s - len(pattern))
else:
    print(-1)
