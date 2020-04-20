secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_number =input()
while user_number!=secret_number:
    print("Ha ha! You're stuck in my loop!")
    print("Enter another number")
    user_number=int(input())
input("Well done, muggle! You are free now")