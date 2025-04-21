#Dict
"""Dict Identify by {}

    Dict is a set of Key and Value pair.
    is is Unorded, (B.coz of No index value asosciated with it.)
    Key is Unique and Value Can be repeated. 
    it is Mutable."""

# D1 = dict()
# print(type(D1))

# D2 ={
#     "Name": "Rupesh",
#     "Sname": "Desai"
# }
# A = D2.items()
# print(A)


# _______________________________________________________

D3 = {
    "Rupesh" : "01",
    "Sandesh" : "02",
    "Aniket" : "03",
    "Mayur" : "04"

}

"""########################################################################"""



Ph = {
    "Gangadhar": "12",
    "Mayur": "34",
    "Sonu": "56",
    "IPV" : "122"
}

while True:
    print("\nMenu:")
    print("A. Look up number")
    print("B. Add new contact")
    print("C. Edit number")
    print("D. Delete contact")
    print("E. Show all contacts")
    print("F. Quit")

    choice = input("Enter choice (A-F): ").upper()

    if choice == "A":
        name = input("Enter name: ")
        if name in Ph:
            print("Number:", Ph[name])
        else:
            print("Not found")

    elif choice == "B":
        name = input("Enter new name: ")
        number = input("Enter number: ")
        Ph[name] = number
        print("Contact added")

    elif choice == "C":
        name = input("Enter name to edit: ")
        if name in Ph:
            number = input("Enter new number: ")
            Ph[name] = number
            print("Number updated")
        else:
            print("Name not found")

    elif choice == "D":
        name = input("Enter name to delete: ")
        if name in Ph:
            del Ph[name]
            print("Contact deleted")
        else:
            print("Name not found")

    elif choice == "E":
        for name in sorted(Ph):
            print(name, ":", Ph[name])

    elif choice == "F":
        print("Goodbye..!")
        break

    else:
        print("Invalid choice")
