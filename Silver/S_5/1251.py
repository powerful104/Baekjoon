s = input()

li = []

for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        li.append(s[:i+1][::-1]+s[i+1:j+1][::-1]+s[j+1:][::-1])

print(sorted(li)[0])