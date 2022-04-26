n=int(input())
delt=[]
for i in range(1,n+1):
    if n%i==0:
        delt.append(i)
print(delt)