def buzzfizz(n):
    if n%3 == 0:
        print("fizz")
    elif n%5==0:
        print("buzz")
    else:
        print(n)

for i in range(1,100):
    buzzfizz(i)
