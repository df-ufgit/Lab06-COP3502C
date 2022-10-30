"""
Title: Lab 6
Name: Duncan Fuller
Date: 10/30/2022
"""

def math(first, second):
    return first + second


def main():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print(f"Result: {math(first, second)}")

if __name__ == '__main__':
    main()