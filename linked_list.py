'''
A Python program to create a linked list and perform operatios on the list
'''

# a linked list that stores a group of string
# create an empty linked list

ll = []     
# ll = linked list

# add some string type element to ll 
ll.append("America")
ll.append("Japan")
ll.append("India")

#display the list
print("The existing list : " , ll)

# display menu
choice = 0
while choice < 5:
    print("Linked List Operations")
    print("1: Add element")
    print("2: Remove element")
    print("3: Replace element")
    print("4: Search for elemnt")
    print("5: Exit")

    choice = int(input("Enter Your Choice:- "))

    # perform a task depending on users choice 
    if choice == 1:
        element = input("Enter element: ")
        pos = int(input("At what position? : "))
        ll.insert(pos, element)
    
    elif choice == 2:
        try:
            element = input("Enter element: ")
            ll.remove(element)
        except ValueError:
            print("Element not Found..! ")

    elif choice == 3:
        element = input("Enter new element: ")
        pos = int(input("At what position? : "))
        ll.pop(pos)
        ll.insert(pos, element)

    elif choice == 4:
        element = input("Enter element: ")
        try: 
            pos = ll.index(element)
            print("Element found at position: ", pos)
        except ValueError:
            print("Element Not found")

    else:
        break

    # Display the list element
    print("List = ", ll)    
