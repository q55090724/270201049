x = int(input("How Many Fibonacci Numbers : "))
a = 1
b = 1
if x % 2 == 0:
    for i in range(int(x / 2)):
        print(a)
        print(b)
        a,b =(a+b),(a + (2 * b))
elif x % 2 == 1:
    for i in range(int(x // 2)):
        print(a)
        print(b)
        a,b =(a+b),(a + (2 * b))
    print(a)

