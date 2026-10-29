import sys
def add(li):
    element_add = input("Please enter the item: ")
    li.append(element_add)
def delete(li):
    element_del = input("Please enter the item to delete: ")
    if element_del in li:
        li.remove(element_del)
    else:
        print("Item was not in list")
    print()
def item_list(li):
    print(".......................")
    print("TODO Items:")
    for i in li:
        print("-->",i)
    print(".......................")
    print()



if "__main__" == __name__:
    li = []
    while True:
        print("_______TODO_APP:________")
        print()
        print("------------------------")
        print("1 => add an element")
        print("2 => delete an element")
        print("3 => show elements")
        print("0 => exit program")
        print("------------------------")
        print()
        ui = input("Please enter a number above: ")
        print()
        if ui == "0":
            print("Goodbye!!")
            print()
            sys.exit()
        elif ui == "1":
            add(li)
        elif ui == "2":
            delete(li)
        elif ui == "3":
            item_list(li)
        else:
            print("Please choose one of the following from list!!")
            print()

