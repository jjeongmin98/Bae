n = int(input(""))
sum=0
cnt=1
for k in range(0,n):
    answer = list(map(str,input("")))
    for i in range(0,len(answer)):
        if answer[i] == 'X':
            cnt = 1
        else:
            sum+=cnt
            cnt+=1
    print(sum)
    sum=0
    cnt=1
    


