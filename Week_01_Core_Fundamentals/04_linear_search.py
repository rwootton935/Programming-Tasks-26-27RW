"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    import random
listlen = int(input("How many integers do you wish to generate in the list?:"))
numlist = []
low = int(input("What should the lowest value be?:"))
high = int(input("What should the highest value be?:"))
for x in range(listlen):
    numlist.append(random.randint(low,high))
searchterm = int(input("What integer do you want to search for?:"))
print(numlist)
y = 0
while y <(listlen):
    if numlist[y] == searchterm:
        print("Searchterm found at position",y+1,".")
        y = listlen
    else:
        y = y + 1
    pass


if __name__ == "__main__":
    main()
