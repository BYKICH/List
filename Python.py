list_create = input("Create list: ")

i = 0

if list_create == "create":
    list1 = []
    while i < i+1:
        number = "Enter element №" + str(i + 1) + ": "
        num = input(number)
        list1.insert(i,num)
        i += 1
        if num == "stop":
            list1.pop()
            # agree = input("withdraw list? ")
            print(list1)
            sort = input("Sort list? ")
            if sort == "no":
                print("List save")
                break
            if sort == "yes":
                list1.sort()
                print(list1)
            break
else:
    print("Error")
