class MyCalc:
    ans=0
    def _is_float(self,val):
        try:
            val =float(val)
            return True
        except:
            return False
    def _is_int(self,val):
        try: 
            val =int(val)
            return True
        except:
            return False
    def _as_number(self, val):
        val =str(val)
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            print("please type a number")
            
    def add(self,num1,num2):
        #zm254-10/11/23
        if num1 == "ans":
            return self.add(self.ans,num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans
    def sub(self,num1,num2):
        #zm254-10/11/23
        if num1 == "ans":
            return self.sub(self.ans,num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans        
    def mult(self,num1 ,num2):
        #zm254-10/11/23
        if num1 == "ans":
            return self.mult(self.ans,num1)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans
    def div(self,num1,num2):
        #zm254-10/11/23
        if num1 == "ans":
            return self.div(self.ans,num1)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 ==0 :
                print("cant divide by zero");
            else:
                self.ans = num1/num2
        return self.ans
    
if __name__ == '__main__':
    is_running = True #to keep running in while loop
    calc = MyCalc()
    while is_running: #to keep running after solving one problem
        iSTR = input("what is your eq (to quit: q): ")
        if iSTR == "quit" or iSTR == "q":
            print("Good bye")
            is_running=False
        else:
            print("your eq was "+ str(iSTR))
            if "+" in iSTR:
                nums = iSTR.split("+")
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
            elif "*" in iSTR or "x" in iSTR:
                nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                r= calc.mult(nums[0].strip(),nums[1].strip())
                print("result is "+ str(r))
            elif "/" in iSTR:
                nums = iSTR.split("/")
                r= calc.div(nums[0].strip(),nums[1].strip())
                print("the result is"+ str(r))
            elif "-" in iSTR:
                iSTR= iSTR.replace(" "," ")
                if "--" in iSTR:
                    nums = iSTR.split("--")
                    nums[-1] = f"-{nums[-1]}"
                else:
                    nums = iSTR.rsplit("-",1)
                    r= calc.sub(nums[0].strip(),nums[1].strip())
                    print("Result is "+ str())




