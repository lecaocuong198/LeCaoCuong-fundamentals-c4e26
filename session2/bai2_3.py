n = int(input("Nhap vao 1 so ngau nhien: "))
check = 0
i = 1
for i in range(1,n):
    if ( n%i == 0 ):
        check +=1
        
if (check == 1):
    print(n," la so nguyen to")
else:
    print(n,"khong la so nguyen to")  


