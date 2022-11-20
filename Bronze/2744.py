def change(c):
    if c.isupper():
        c = c.lower()
    else:
        c = c.upper()
    return c

s = input()

for c in s:
    print(change(c), end = '')