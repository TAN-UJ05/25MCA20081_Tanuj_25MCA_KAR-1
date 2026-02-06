n=int(input())
for _ in range(n):
    size=int(input())
    if size<=4:
        print(-1)
    even=[]
    odd=[]
    result=[]
    for i in range(1,size+1):
        if i%2==0 and i!=4:
            even.append(i)
        elif i%2!=0 and i!=5:
            odd.append(i)
    result=even+[4,5]+odd
    print(*result)
