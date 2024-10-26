import counter
sequence = str(input("Enter a sequence : "))
object = str(input("Enter a desired letter : "))
print(f"{sequence}")
print(f"The number of '{object}': {counter.counter(sequence, object)}")