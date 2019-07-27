#imports everything (*) form the byotest file
from byotest import *       #step 1


def get_change(amount):                     #step 4
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    Returns a list of coin values
    """
    if amount == 0:                             #step 7
        return []                               #step 5

        #return [1]                             #step 8 This is commented out because it is for any coin amount!
    
    if amount in [100, 50, 20, 10, 5, 2, 1]:    #step 13
        return [amount]                         #step 10

    change = []                                 #step 16
    #change.append(2)                           #step 17
    #change.appende(1)                          #step 18
        #return [2,1]                           #step 14
    for coin in [100, 50, 20, 10, 5, 2, 1]:     #step 19
        if coin <= amount:                      #step 20
            amount -= coin                      #step 23
            change.append(coin)                 #step 21

    return change                               #step 22


#  Write our tests for our code
test_are_equal(get_change(0), [])           #step 3
test_are_equal(get_change(1), [1])          #step 6
test_are_equal(get_change(2), [2])          #step 9
test_are_equal(get_change(5), [5])          #step 11
test_are_equal(get_change(10), [10])        #step 11
test_are_equal(get_change(20), [20])        #step 11
test_are_equal(get_change(50), [50])        #step 11
test_are_equal(get_change(100), [100])      #step 11
test_are_equal(get_change(3), [2, 1])       #step 12
test_are_equal(get_change(7), [5, 2])       #step 15

print("All tests pass!")                    #step 2
