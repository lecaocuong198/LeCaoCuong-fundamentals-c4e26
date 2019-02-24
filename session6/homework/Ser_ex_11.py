def is_inside(a,b):
    if a[0] > b[0] and a[1]>b[1]:
        if a[1]<b[2]+b[0] and a[0]<b[3]+b[1]:
            return True
        else:
            return False         
    else:
        return False
a=[100,120]
b=[140,60,100,200]    
a1=[200,120]
b1=[140,60,100,200]

s = is_inside(a,b)
s1 = is_inside(a1,b1)
print(s)
print(s1)