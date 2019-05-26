a,b = input().split()
x=int(a)
y=int(b)
x,y = (x^y)^((x^y)^y),(x^y)^y
print(x,y)
