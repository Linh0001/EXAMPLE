#Chương trình viết hàm x mũ n
x=float(input("Nhập giá trị x = "))
n=int(input("Nhập giá trị n = "))
def f_mu_n(x,n):
    i=int(1)
    temp=1
    while i<=n:
        temp*=x
        i+=1
    return temp
print("Giá trị",x,"^",n,"=",f_mu_n(x,n))    