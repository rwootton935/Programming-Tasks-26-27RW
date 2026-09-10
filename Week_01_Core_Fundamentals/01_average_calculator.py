"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    import statistics 
    numin = int(input("How many numbers are you going to find the mean off?"))
    numbers = []
    for x in range (numin):
        num = int(input("Input a number"))
        numbers.append(num)
    print(statistics.mean(numbers))
    pass



if __name__ == "__main__":
    main()
