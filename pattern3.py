# Program to print the following pattern:
# 1
# 12
# 123
# 1234
# 12345
for column in range(1, 7):
    for row in range(1, column):
        # print(f" iteration = {column}, column = {column}, row = {row}")
        print(row, end="")
    # Printing the new line
    print()
