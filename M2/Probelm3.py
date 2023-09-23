a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    pos_arr=[]
    type_and_value =[]
    for x in arr:
        if isinstance(x,(int,float)):
            pos_x=abs(x)
            pos_arr.append(pos_x)
            #print(f"{abs(x)} ({type(x)})")
            print(f"({type(pos_x)}, {pos_x})", end=' ')
            #type_and_value.append(f"({pos_x})")
            
        elif isinstance(x, str): 
            if x.startswith('-'):
                pos_x=x[1:]
                pos_arr.append(pos_x)
                #print(f"{pos_x} ({type(pos_x)})") 
                print(f"({type(pos_x)}, {pos_x})", end=' ')
            else:
                pos_x=x
                pos_arr.append(pos_x)
                print(f"({type(pos_x)}, {pos_x})", end=' ')
                # print(f"{pos_x} ({type(pos_x)})") 
        else:
            pos_arr.append(x)
    print("\n")   
    #print( pos_arr)    
    #print(" ".join(type_and_value))


    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)