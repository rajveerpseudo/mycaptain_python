a=0
b=1
limit=int(input("Enter limit of fibonacci"))
print(a)
for number in range(limit):
    c=a+b;
    a=b
    b=c
    c=a
    print(c)
