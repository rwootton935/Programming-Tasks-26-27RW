"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
numin = int(input("How many numbers to add?"))
numlist = []
for x in range(numin):
    numappend = int(input("What integer to add?:"))
    numlist.append(numappend)
print(numlist)
print(len(numlist))
y = len(numlist)
for x in range(y - 1):
    for x in range(y - 1):
        print(x)
        if numlist[x] > numlist[x + 1]:
            numlist[x],numlist[x + 1] = numlist[x + 1],numlist[x]
            print(numlist)
        else:
            numlist[x],numlist[x + 1] = numlist[x],numlist[x + 1]
            print(numlist)
print(numlist)
maxnum = numlist[y - 1]
minnum = numlist[0]
print(maxnum)
print(minnum)
    pass


if __name__ == "__main__":
    main()
