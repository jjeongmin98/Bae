num, snum = map(int,input("").split())
lst = list(map(int,input("").split()))
alist=[]
for i in range (0,len(lst)):
    if lst[i] < snum:
        alist.append(lst[i])
for k in alist:
    print(k,"",end='')