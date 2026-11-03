def porty(user):
   test = user.split(" ")
   print("The following ports are: ")
   for i in test:
       print(i)




if __name__ == "__main__":
    print("Ports should be entered with spaces inbetween them!!")
    user = input("Please enter ports: ")
    porty(user)