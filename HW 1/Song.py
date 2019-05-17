# In this program, I will print a cumulative song.
# To eliminate the redundancy, I will developed several functions such that
# there is only one print statement for each distinct line of the song.

# Define the functions for each paragraph  after the name of different things.
# For each function, it also include some other functions to avoid redundancy.
def partridge():
    print("a partridge in a pear tree.")
    print()

def turtle():
    print("two turtle doves, and")
    partridge()

def hens():
    print("three French hens,")
    turtle()

def birds():
    print("four calling birds,")
    hens()

def rings():
    print("five golden rings,")
    birds()

def geese():
    print("six geese a-laying,")
    rings()

def caixukun():
    print("seven dancing caixukun,")
    geese()

# Start to print the song after defining the functions. Each paragraph starts
# with a print  statement.
print("On the 1st day of \"Xmas\", my true lovegave to me")
partridge()

print("On the 2nd day of \"Xmas\", my true lovegave to me")
turtle()

print("On the 3rd day of \"Xmas\", my true lovegave to me")
hens()

print("On the 4th day of \"Xmas\", my true lovegave to me")
birds()

print("On the 5th day of \"Xmas\", my true lovegave to me")
rings()

print("On the 6th day of \"Xmas\", my true lovegave to me")
geese()

print("On the 7th day of \"Xmas\", my true lovegave to me")
caixukun()
