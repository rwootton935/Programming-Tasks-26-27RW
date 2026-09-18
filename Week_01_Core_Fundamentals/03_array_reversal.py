"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
   itemin = int(input("How many items do you wish to add?:"))
itemlist = []
for x in range(itemin):
    itemappend = input("Add an item:")
    itemlist.append(itemappend)
print(itemlist)
reverse = []
reverse.append(itemlist[itemin - 1])
index = 2
for x in range(itemin - 1):
    reverse.append(itemlist[-index])
    index = index + 1
print(reverse)
    pass


if __name__ == "__main__":
    main()
