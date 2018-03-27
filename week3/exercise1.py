# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
    loopy = [] 
    while start < stop: #while = continuous list
        loopy.append(start)
        start += step
    return loopy

    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """

    '''count = 0
    while count < 10:
        print (count)
        count += 1

    count = 0
    print_list = []
    while count < 10:
        print_list.append(count)
        count += 1
    return print_list'''

def lone_ranger(start, stop, step):

    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    a_list = []
    count = start
    while count < stop:
        a_list.append(count)
        count += step
    return a_list

    
def two_step_ranger(start, stop, step=2):
    a_list = []
    count = start
    while count < stop:
        a_list.append(count)
        count = count + 2
    return a_list

    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    pass


def stubborn_asker(low, high):

    list_uno = True
    while list_uno == True:
        Vn = None
        Vstr = input(("Give a number between ") + str(low) + (" and ") + str(high) + (": "))
        try:
            Vn = float(Vstr)
            if Vn >= low and Vn <= high:
                list_uno = False
            else:
                list_uno = True
        except:
            list_uno = True
    return str(Vn) 

    
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    pass


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    ask = True
    while ask == True:
        Vn = None
        Vstr = input("please type a number: ")
        try:
            Vn = float(Vstr)
            ask = False
        except:
            ask = True
    return str(Vn) 


def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    super_duper = True
    while super_duper == True:
        Vn = None
        Vstr = input("Give a number between " + str(low) + " and " + str(high) + ": ")
        try:
            Vn = float(Vstr)
            if Vn >= low and Vn <= high:
                super_duper = False
            else:
                super_duper = True
        except:
            super_duper = False
    return str(Vn) 


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
