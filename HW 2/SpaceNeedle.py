# In this program, I draw a space needle by using the characters. I divided the whole
# space needle into several sections and make each section a function to make the code
# eaiser. I followed every rules about the figure's size in the spec, and I also added
# some rule about the figure size which did not mentioned in the spec to make the figure
# looks better. We can change the size of the structure, and the scale has to be an even
# number.

# Changed the size of the space needle here.
constant = 6
# Print the top level part which appears twice in this figure.
def tube(num):
    for i in range(num):
        for j in range(3 * constant):
            print(' ', end = '')
        print('||')

# Print the bottom level part which also appears twice.
def pyramid(num):
    for i in range(1, num + 1):
        for j in range(3 * (num-i)):
            print(' ', end = '')
        print('__/', end = '')
        for k in range(3 * (i-1)):
            print(':', end = '')
        print('||', end = '')
        for m in range(3 * (i-1)):
            print(':', end = '')
        print('\\__')
    print('|', end = '')
    for n in range (1, 6 * num + 1):
        print('\"', end = '')
    print('|')

# Print the bottom half of the head of the space needle.
def bowl(num):
    for i in range(1, num + 1):
        for j in range(1, (i-1) * 2 + 1):
            print(' ', end = '')
        print('\\_', end = '')
        for k in range(1, int((3*num-2*i)/2) * 2 + 2):
            print('/\\', end ='')
        print('_/')


# Print the body of the space needle, and I changed the number of '%' in each line such that
# the space needle looks neat.
def body(num):
    for i in range(1, num ** 2 + 1):
        for  j in range(1, int(5 * num/2)):
            print(' ', end = '')
        print('|', end = '')
        for k in range(1, int(num/2 + 1)):
            print('%', end = '')
        print('||', end = '')
        for m in range(1, int(num/2 + 1)):
            print('%', end = '')
        print('|')

tube(constant)
pyramid(constant)
bowl(constant)
tube(constant)
body(constant)
pyramid(constant)
