class MyCalc: #creating class MyCalc
    ans=0
    #storing the variable ans as 0 
    #starts for the first time ans wont have calue and it will throw an error
    
    
    def _is_float(self,val):
    #zm254-10/11/23
    #summary: _is_float is function which checks if the input is a float and using 
    #try and except method in this function _is_float is used in _as_number function
        try:
            val =float(val)
            return True
        except:
            return False
        

    def _is_int(self,val):
        #zm254-10/11/23
        #summar:this is a function which checks if the given input is int
        #using try and except method in this function, _is_int is used in _as_number function
        try: 
            val =int(val)
            return True
        except:
            return False
        

    def _as_number(self, val):
        #zm254-10/11/23
        #Summary:_as_number is a func which converts inputs of string of numbers into its respective type(int or float)
        #first line is to solve the bug which was existingin this code.
        #basicallu written to convert out final ans back to a string beause if its float it will convert to
        #float value into int in the "if" condition
        #main part of the function:we are checking the if input value of string is a int, float or not number.
        #acc to which cond passes we will returnthe datatype converted val to where ever the _as_number function is called.

        val =str(val)
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("not a number")


    def add(self,num1,num2):
        #zm254-10/11/23
        #Summary: in here adding 2 number.
        #we are calling _as_number to convert the input value of string into its particular datatype.
        #if we are adding a number to the previous ans then the statement in "if" cond will run in a "while"
        #loop below where there add function is called and the add func is executed again and the normal
        #calculation(add) in the "else" cond will reutrned as the final ans.
        if num1 == "ans":
            return self.add(self.ans,num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans
    

    def sub(self,num1,num2):
        #zm254-10/11/23
        #Sumary: subtracting the numbers here
        #we are calling _as_numbr to convert the input val of string into its part datatype.
        #if we are subt a number to the prev ans then the statement in "if" cond will run in a "while"
        #loop below where there sub func is called, then the main sub func is executed again and the nrml
        #calc(sub) in the "else" cond will returned as the final ans.
        if num1 == "ans":
            return self.sub(self.ans,num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 - num2
        return self.ans


    def mult(self, num1, num2):
        #zm254-10/11/23
        #summary:mult is basically used for multiplying 2 numbers.
        #we are calling _as_number to convert the input val of string into its particular datatype.
        #if we are multiplying a number to the prev ans then the stmt in "if " cond will run in a "while"
        #loop below where there mult function is called and the mult func is executed again and the nrml
        #calculation(mult) in the "else" cond will reutrned as the final answer.
        if num1 == "ans":
            return self.mult(self.ans,num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1 * num2
        return self.ans


    def div(self,num1,num2):
        #zm254-10/11/23
        #div is basically used for dividing 2 numbers.
        #we are calling _as_number to convert the input val of string into its particular datatype.
        #if we are dividing a number to the prev ans then the stmt in "if" cond will run in a "while"
        # loop below where there div fun is called and the div function is executed again and the nrml
        # #cal(division) in the "else" cond will return as the final answer.
        # in div func we have another cond in which we are checking if the divisor is equal to 0
        # in that case we are printing "cant divide by zero" 
        if num1 == "ans":
            return self.div(self.ans,num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 ==0 :
                print("cant divide by zero")
            else:
                self.ans = num1 / num2
        
        return self.ans
#zm254-10/13/23   
if __name__ == '__main__':
    is_running = True #to keep running in while loop
    calc = MyCalc()
    while is_running: #to keep running after solving one problem
        iSTR = input("what is your eq (to quit: q): ") #taking input from the user for the eq
        if iSTR == "quit" or iSTR == "q": #if the user enters quit or q the prog will get terminated
            print("Good bye")
            is_running=False #triggers termination
        else:
            print("your eq was "+ str(iSTR)) #this print stmt primes the same eq which was given by the user
        
            if "+" in iSTR: #this cond runs if there is a '+' symbol in the input equation
                nums = iSTR.split("+") #the eq is split using method into 2 parts keeping '+' as the reference and stored in array called nums
                #below r is the o/p if the eq
                #nums has the 2 numbers using which the add has to be performed
                #we are calling it individually from the array as num[0] and num[1] and strippingtp remove the all the spaces in that string
                #the striped values in snet to the add function
                r=calc.add(nums[0].strip(),nums[1].strip())
                print("Result is "+ str(r))
        # elif "-" in iSTR:
        #     iSTR= iSTR.replace(" "," ")
        #     if "--" in iSTR:
        #         nums = iSTR.split("--")
        #         nums[-1] = f"-{nums[-1]}"
        #     else:
        #         nums = iSTR.rsplit("-",1)
        #         r= calc.sub(nums[0].strip(),nums[1].strip())
        #         print("Result is "+ str())
            elif "*" in iSTR or "x" in iSTR:#this cond runs if there is 'x' or '*' symbol
                nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x") # the eq is split using .split() method into 2 parts keeping 'x' or '*' as reference
                #r is o/p if the eq
                #nums has the 2 numbers using which the mult has to be performed
                #calling individually from array num[0] and num[1] and striping to remove the all spaces in that string
                #striped value is sent to the mult function
                r= calc.mult(nums[0].strip(),nums[1].strip())
                print("result is "+ str(r))
            elif "/" in iSTR: #this cond runs if there is a '/' symbol in the input eq
                nums = iSTR.split("/") #the eq is split using .split() method into 2 parts keeping
                #r is o/p if the eq
                #nums has the 2 numbers using which the divisoin has to be performed
                #we are calling it ind from thearray num[0] and num[1] and stripping to remove all the spaces
                #the striped values in sent to the div func
                r= calc.div(nums[0].strip(),nums[1].strip())
                print("the result is"+ str(r))
            
            #doing it last so negative can be handled
            elif "-" in iSTR:# this condition runs if there is a '-' symbol in the input equation
                iSTR= iSTR.replace(" "," ")# Removing all the white spaces from the string to remove complications while subtracting negative numbers. 
                if "--" in iSTR: # Here we are checking for if subtrahend is a negative number by checking if there is "--" in the string
                    nums = iSTR.split("--")# if the above condition passes then we are spliting the string using "--" as the refrence
                    nums[-1] = f"-{nums[-1]}"# since in the above line we removed the negative sign for the subtrahend, now we are adding it back again manually
                else:
                    nums = iSTR.rsplit("-",1)
                    #r is o/p if the eq
                    #nums has the 2 numbers using which the divisoin has to be performed
                    #we are calling it ind from thearray num[0] and num[1] and stripping to remove all the spaces
                    #the striped values in sent to the div func
                    r= calc.sub(nums[0].strip(),nums[1].strip())
                    print("Result is "+ str())




