"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    def gradecalc(score):
        if score > 100:
            print("The maximum marks achievable is 100")
        elif score > 79:
            print("Grade A")
        elif score > 59:
            print("Grade B")
        elif score > 39:
            print("Grade C")
        else:
            print("Grade D")

    score = int(input("What is your score?"))
    gradecalc(score)
    pass


if __name__ == "__main__":
    main()
