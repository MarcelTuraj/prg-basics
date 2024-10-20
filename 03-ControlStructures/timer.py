###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0 :
    print(countdown)
    countdown -= 1
    time.sleep(1)  # Wait for 1 second
    if countdown == 5 :
        break
print("Five")
time.sleep(1)
print("Four")
time.sleep(1)
print("Three")
time.sleep(1)
print("Two")
time.sleep(1)
print("One")
time.sleep(1)
print("Time's up")