import requests
s = 0
n1 = input().replace('stepic.org','stepik.org')
n2 = input().replace('stepic.org','stepik.org')
if (n1 != None or n1 != "") or (n2 != None or n2 != ""):
    while s <= 1:
        r = requests.get(n1)
        # print(r)
        r = r.text
        # print(r)
        r = r.split('"')
        for n in r:
            if n.startswith("https"):
                n1 = n.replace('stepic.org','stepik.org')
                n1 = n1.replace(" ", '')
                if requests.get(n1).status_code == 200:
                    s += 1
                else:
                    continue
    if n1 == n2:
        print("Yes")
    else:
        print("No")
else:
    print("No")
