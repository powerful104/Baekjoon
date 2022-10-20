sci = []
soc = []

for _ in range(4):
    sci.append(int(input()))
for _ in range(2):
    soc.append(int(input()))

print(sum(sci) - min(sci) + max(soc))