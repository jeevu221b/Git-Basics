# Program to print the following pattern:
# *
# **
# ***
# ****
# *****

for row in range(1, 6):
    for column in range(row):
        print("*", end="")

    print()
