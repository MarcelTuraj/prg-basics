###
# Name reader
#
name = input("Enter name: ")

if name.endswith("a") :
    print(f"{name} --> polish female name")
elif name == "Bonawentura" :
    print("An exception. ")
else :
    print("It's not female name. ")
