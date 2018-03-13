"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?'] 

# I think this line will print "what does this line do?" each word indiviually
for word in some_words:
    print(word)
    # each time the string was stepped over, it printed a word within quotation

# I think this line will only print the first word
for x in some_words:
    print(x)
    # same as previous string

# will print ['what' 'does' 'this' 'line' 'do' '?'] 
print(some_words) # printed ['what', 'does', 'this', 'line', 'do', '?'] (lol forgot about commas)

#if "some_words" is bigger than 3, it will print ('some_words contains more than 3 words')
if len(some_words) > 3:
    print('some_words contains more than 3 words') #it printed ('some_words contains more than 3 words'),
    #as it contains more than three words


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # It will Returns a namedtuple() containing six attributes: 
    # system, node, release, version, machine, and processor.
    print(platform.uname())
    #yup, it did it 

usefulFunction()
