## FIBONACCI NUMBER

##INPUT

n= int(input('Input a number : '))

#Process

while n<=0:
    n=int(input('Input a postive number : '))
        
if n==1:
        print('0')
elif n==2:
        print('0','1')
else: r=[0,1]

for i in range(3,n+1):
    t=r[-1]+r[-2]
    r.append(t)

#OUTPUT
    
else: print(r)
    
