# 1
# Replace if-else with try-except in the the example below:

def fourth_element_of_list(L):
    """
    Return the 4th element of ``L`` if it exists, ``None`` otherwise.
    """
    try:
        return L[3]
    except IndexError:
        return None

# 2
# Modify to use try-except to return the sum of all numbers in L,
# ignoring other data-types

def sum_of_numbers(L):
    """
    Return the sum of all the numbers in L.
    """
    s = 0
    for l in L:
        try:
            s+= l
        except TypeError:
            pass
    return s

# TEST
# print sum_of_numbers([3, 1.9, 's']) == 4.9

# L1 = [1,2,3]
# L2 = [1,2,3,4]
# print fourth_element_of_list(L1)
# print fourth_element_of_list(L2)