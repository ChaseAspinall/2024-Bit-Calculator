def int_check(question, low):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# main routine goes here
for item in range(0, 2):
    integer = int_check("Integer: ", 0)
    print(integer)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)
