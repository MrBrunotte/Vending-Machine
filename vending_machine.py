#imports everything (*) form the byotest file
from byotest import *       #step 1

#coins = [100, 50, 20, 10, 5, 2, 1]          #step 26

usd_coins = [100, 50, 25, 10, 5, 2, 1]      #step 28
eur_coins = [100, 50, 20, 10, 5, 2, 1]      #step 28

#def get_change(amount):                     #step 4
    
    # The get_change(amount) funcion:
    # Takes the payment amount and returns the change
    # `amount` the amount of money that we need to provide change for
    # Returns a list of coin values

    #if amount == 0:                             #step 7
        #return []                               #step 5

        #return [1]                             #step 8 This is commented out because it is for any coin amount!
    
    #if amount in coins:    #step 13
        #return [amount]                         #step 10

def get_change(amount, coins=eur_coins):        #step 29
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)
    Returns a list of coin values
    """

    change = []                                 #step 16
    #change.append(2)                           #step 17
    #change.appende(1)                          #step 18
        #return [2,1]                           #step 14
    #for coin in [100, 50, 20, 10, 5, 2, 1]:     #step 19
        #if coin <= amount:                      #step 20
    for coin in coins:
        while coin <= amount:                   #step 25
            amount -= coin                      #step 23
            change.append(coin)                 #step 21

    return change                               #step 22


#  Write our tests for our code
test_are_equal(get_change(0), [])                   #step 3
test_are_equal(get_change(1), [1])                  #step 6
test_are_equal(get_change(2), [2])                  #step 9
test_are_equal(get_change(5), [5])                  #step 11
test_are_equal(get_change(10), [10])                #step 11
test_are_equal(get_change(20), [20])                #step 11
test_are_equal(get_change(50), [50])                #step 11
test_are_equal(get_change(100), [100])              #step 11
test_are_equal(get_change(3), [2, 1])               #step 12
test_are_equal(get_change(7), [5, 2])               #step 15
test_are_equal(get_change(9), [5, 2, 2])            #step 24
test_are_equal(get_change(35, usd_coins), [25, 10]) #step 27

print("All tests pass!")                    #step 2
