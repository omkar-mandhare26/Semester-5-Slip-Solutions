# try: 
#     n = int(input("Enter any positive integer: "))
#     assert n > 0, "Please enter a positive integer greater than 0"
#     print(f"Number: {n}")
# except AssertionError as e:
#     print(e)
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")

try:
    n = int(input("Enter any positive integer: "))
    if n <= 0:
        raise ValueError("Please enter a positive integer greater than 0")
    else:
        print(f"Num: {n}")
except ValueError as e:
    print(e)