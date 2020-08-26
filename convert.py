# Import Functions
from hash import hash
from alpha import test_alpha

# Keep prompting till valid input
while (True):

    ask = input("Enter Word: ")

    check = test_alpha(ask)

    if check == True:
        break

    print("\nEnter Correct Word!\n")

# Iterate through each character
for i in range(len(ask)):

    # Get Hash key
    key = hash(ask[i])

    # Convert it to string
    arr = str(key + 1)

    # Access last digit of string
    digit = int(arr[len(arr) - 1])

    # If Even
    if digit % 2 == 0:

        print("0", end="")

    # If Odd
    if (digit + 1) % 2 == 0:

        print("1", end="")

# Print New-line, Exit the program
print()
exit(0)