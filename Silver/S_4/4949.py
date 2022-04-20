while True:
    s = input()
    if s == ".":
        break
    st=""
    
    for i in list(s):
        if i == "(":
            st+=i
        elif i == ")":
            st+=i
        elif i == "[":
            st+=i
        elif i == "]":
            st+=i
    s=str(st)
    while "()" in s or "[]" in s:
        if "()" in s:
            a = s[:s.find("()")]
            b = s[s.find("()") + len("()"):]
            s = a + b
        if "[]" in s:
            a = s[:s.find("[]")]
            b = s[s.find("[]") + len("[]"):]
            s = a + b
    if len(s)!=0:
        print("no")
    else:
        print("yes")