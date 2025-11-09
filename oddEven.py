n = input("Enter a number : ")
n = int(n)

if n % 2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")

print("Number is even") if n % 2 == 0 else print("Number is odd")

