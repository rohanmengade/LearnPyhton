india = {"Mumbai","Delhi","Pune"}
Germany = {"Frankfurt","Berlin","Dusseldorf"}
Japan = {"Tokyo","Osaka"}

city = input("Enter the City: ")

if city in india:
    print("Indian City")
elif city in Germany:
    print("German City")
elif city in Japan:
    print("Japanese City")
else:
    print("City not found")