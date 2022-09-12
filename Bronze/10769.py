s = input()

hap = s.count(":-)")
unhap = s.count(":-(")

if hap == 0 and unhap == 0:
    print("none")
elif hap == unhap:
    print("unsure")
elif hap > unhap:
    print("happy")
else:
    print("sad")