a=int(input("argument a="))
b=int(input("argument b="))
c=int(input("argument c="))


def square(a,b,c):
    d = (b ** 2) - (4 * a * c)
    if d<0:
        print("Korney net")
    elif d==0:
        x1=(-1*b+(d**1/2))/(2*a)
        print(x1)
    elif d>0:
        x1 = (-1 * b + (d ** 1 / 2)) / (2 * a)
        x2 = (-1 * b - (d ** 1 / 2)) / (2 * a)
        print(x1,x2)

square(a,b,c)