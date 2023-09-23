a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    pos =[]
    for x in arr:
        if ((isinstance(x,float) or (isinstance(x,int)))   and (x)> 0):
            pos.append(x)
    #creatig for loop in which using isinstance function to get float or int with or operator
    #using operation "and" to get 2nd condition "">0"
    #in the end using append operation to add it to the list
    print(pos)
    #zm254-09/22/23
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)