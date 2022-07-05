str_A = input()
str_B = input()

if len(str_A) > len(str_B):
    str_A, str_B = str_B, str_A

str_B = " " * (len(str_A) - 1) + str_B + " " * (len(str_A) - 1)

max = 0
for i in range(len(str_B) - len(str_A) + 1):
    sum_ = 0
    for j in range(len(str_A)):
        if str_B[i+j] != str_A[j]:
            if max < sum_:
                max = sum_
            sum_ = 0
        else:
            sum_ +=1
    else:
        if max < sum_:
            max = sum_

print(max)