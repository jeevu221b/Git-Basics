# Program to print the following pattern:
# 1
# 22
# 333
# 4444
# 55555

for column in range(1, 6):
    for row in range(column):
        print(column, end="")

    # Printing a new line
    print()
