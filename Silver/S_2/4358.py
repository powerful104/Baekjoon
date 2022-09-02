import sys

species = dict()
nums = 0

while True:
    spe = sys.stdin.readline().rstrip()
    if not spe:
        break
    
    nums += 1
    
    if species.get(spe) == None:
        species[spe] = 1
    else:
        species[spe] += 1

for i in sorted(species.keys()):
    print("%s %.4f" % (i, species[i]/nums*100))