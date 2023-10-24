from enum import Enum
import sys
from PumpkinMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from PumpkinMachineExceptions import InvalidPaymentException


class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity=10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        #zm254-10/20/23
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity

    def in_stock(self):
        return self.quantity > 0

    def __repr__(self) -> str:
        return self.name


class Pumpkin(Usable):
    pass


class FaceStencil(Usable):
    pass


class Extra(Usable):
    pass


class STAGE(Enum):
    Pumpkin = 1
    FaceStencil = 2
    Extra = 3
    Pay = 4


class PumpkinMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_STENCILS = 3
    MAX_EXTRAS = 3
    def __init__(self):
        self.pumpkins = [Pumpkin(name="Mini Pumpkin", cost=1),
                    Pumpkin(name="Small Pumpkin", cost=2),
                    Pumpkin(name="Medium Pumpkin", cost=2.50),
                    Pumpkin(name="Large Pumpkin", cost=3)]
        self.face_stencils = [FaceStencil(name="Happy Face", quantity=10, cost=1),
                        FaceStencil(name="Scream Face", quantity=10, cost=1),
                        FaceStencil(name="Toothy Face", quantity=10, cost=1),
                        FaceStencil(name="Spooky Face", quantity=10, cost=1)]
        self.extras = [Extra(name="Small Candle", quantity=10, cost=.25),
                Extra(name="LED Candle", quantity=10, cost=.25),
                Extra(name="Spooky Sound Effects", quantity=10, cost=1.25),
                Extra(name="Sticker Pack", quantity=10, cost=1.00),
                Extra(name="Paint Kit", quantity=10, cost=3),
                Extra(name="Dry Ice", quantity=10, cost=.25),
                Extra(name="Googly Eyes", quantity=10, cost=.25),
                Extra(name="Glitter", quantity=10, cost=.25)]

        # variables
        self.remaining_uses = PumpkinMachine.USES_UNTIL_CLEANING
        self.remaining_stencils = PumpkinMachine.MAX_STENCILS
        self.remaining_extras = PumpkinMachine.MAX_EXTRAS
        self.total_sales = 0
        self.total_products = 0
    

    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_stencils = MAX_STENCILS
    remaining_extras = MAX_EXTRAS
    total_sales = 0
    total_products = 0

    inprogress_pumpkin = []
    currently_selecting = STAGE.Pumpkin

    # rules
    # 1 - pumpkin must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - face stencils can't exceed max
    # 4 - extras can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more things can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_products should increment properly after a payment

    def pick_pumpkin(self, choice):
        if self.currently_selecting != STAGE.Pumpkin:
            raise InvalidStageException
        for c in self.pumpkins:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_pumpkin.append(c)
                return
        raise InvalidChoiceException
    #zm254-10/20/23
    def pick_face_stencil(self, choice):
        if self.currently_selecting != STAGE.FaceStencil:
            raise InvalidStageException
        if not self.inprogress_pumpkin:
            raise InvalidChoiceException("Pumpkin must be the first selection (can't add face stencils or extras without a pumpkin choice)")
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_stencils <= 0:
            raise ExceededRemainingChoicesException
        for f in self.face_stencils:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_pumpkin.append(f)
                self.remaining_stencils -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException
    #zm254-10/20/23
    def pick_extras(self, choice):
        if self.currently_selecting != STAGE.Extra:
            raise InvalidStageException
        if self.remaining_extras <= 0:
            raise ExceededRemainingChoicesException
        for t in self.extras:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_pumpkin.append(t)
                self.remaining_extras -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        """Called when a pumpkin is complete"""
        self.remaining_stencils = self.MAX_STENCILS
        self.remaining_extras = self.MAX_EXTRAS
        self.inprogress_pumpkin = []
        self.currently_selecting = STAGE.Pumpkin

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING

    def handle_pumpkin_choice(self, _pumpkin):
        self.pick_pumpkin(_pumpkin)
        self.currently_selecting = STAGE.FaceStencil

    def handle_face_stencil_choice(self, _face_stencil):
        if _face_stencil == "next":
            self.currently_selecting = STAGE.Extra
        elif not self.inprogress_pumpkin:
            raise InvalidStageException
        else:
            self.pick_face_stencil(_face_stencil)
    def handle_extra_choice(self, _extra):
        if _extra == "done":
            self.currently_selecting = STAGE.Pay
        
        else:
            self.pick_extras(_extra)

    def handle_pay(self, expected, total):
        total =float(total)
        expected =float(expected)
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total==expected:
            print("Thank you! Enjoy your Pumpkin and Happy Halloween!")
            self.total_products += 1
            self.total_sales += expected  # <-- TODO increment only if successful
            # print(f"Total sales so far {self.total_sales}")
            #zm254-10/20/23
            self.reset()
        else:
            raise InvalidPaymentException

    def print_current_pumpkin(self):
        print(    f"Current Pumpkin: {','.join([x.name for x in self.inprogress_pumpkin])}")
         
    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_pumpkin
        #zm254-10/18/23
        self.cost =0 
        #adding the input item cost from the user for every choice selected
        for item in self.inprogress_pumpkin:
            self.cost += item.cost
        return round(self.cost,2)  #rounding to 2decimals

    def run(self):
            
        try:
            if self.currently_selecting == STAGE.Pumpkin:
                pumpkin = input(f"What type of pumpkin would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.pumpkins))))}?\n")
                self.print_current_pumpkin()
                self.handle_pumpkin_choice(pumpkin)
                
                #self.currently_selecting=STAGE.FaceStencil
            elif self.currently_selecting == STAGE.FaceStencil:
                stencil = input(f"What type of face stencil would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.face_stencils))))}? Or type next.\n")
                try:
                    self.handle_face_stencil_choice(stencil)
                    #zm254-10/20/23
                    #if the face_Stencil is exceeded more than 3 then we are auto going to next stage after displauing error to user
                    #change to extra stage
                except ExceededRemainingChoicesException:
                    print("Sorry! You've exceeded the maximum no of stencil that you can select,please choose a extra")
                    self.print_current_pumpkin()
                    #self.currently_selecting =STAGE.Extra
            elif self.currently_selecting == STAGE.Extra:
                extra = input(f"What extras would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.extras))))}? Or type done.\n")
                try:
                    self.handle_extra_choice(extra)
                    #zm254-10/20/23
                    #if the extras gets more than 3 error is given as output to user then auto shifts to next stage
                    #changes to displaying total cost stage and getting paid from the user
                except ExceededRemainingChoicesException:
                    print("Sorry! You've exceeded the maximum number of extras;proceeding to payment portal")
                    self.print_current_pumpkin()
                    #self.currently_selecting = STAGE.Pay
                
                

            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # TODO show expected value as currency format
                # TODO require total to be entered as currency format
                total = input(f"Your total is ${expected:.2f}, please enter the exact value.\n")
                try:
                    self.handle_pay(expected, total)
                    #zm254-10/20/23
                    #if the amt entered by the user doesnt match the total amt. error msg will be printed.
                    #user is given another chanve to enter the right amt
                except InvalidPaymentException:
                    print("entered wrong amount. Please try again")
                    self.run()

                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    # exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the pumpkin machine")
                    return 1
            
        except KeyboardInterrupt:
            # quit
            print("Quitting the pumpkin machine")
            sys.exit()
        # TODO items below
        # Note: Stage/category refers to the enum towards the top. Make sure error messages are very clear to the user
            
            #zm254-10/20/23
            #if any of the abov input items from the user is out of stock then error message is displaued
            #and the user will be redireced to select diff items
        except OutOfStockException:# handle OutOfStockException
            print("the selected option is out of stock.try again")# show an appropriate message of what stage/category was out of stock
            
            #zm254-10/20/23
            #if the USES_UNTIL_CLEANING exceeds 15 then the user will be promted with needs cleanig message as the output.
            #when the user types "clean" then "the machine as been cleaned" is shown as the output and continued with nrml activites
        except NeedsCleaningException:# handle NeedsCleaningException
            choice = input("the machine needs to be cleaned!type yes to clean\n")# prompt user to type "clean" to trigger clean_machine()
            # any other input is ignored
            if choice.lower()=="yes":
                print("The machine has been cleaned, you can continue")# print a message whether or not the machine was cleaned
                self.clean_machine()
            
            
            #zm254-10/20/23
            #if ant of the above stage if the user has entered a invalidi choice the invalidChoiceException is called
            # #and asked the user to choose again with the given option        
        except InvalidChoiceException:# handle InvalidChoiceException
            #zm254-10/19/23
            print("Youve entered an invalid choice.Please choose from the given options")
            # show an appropriate message of what stage/category was the invalid choice was in
            self.run()
        
        # handle ExceededRemainingChoicesException
            #zm254-10/19/23
            # move to the next stage/category
        # handle InvalidPaymentException
            # show an appropriate message
        except Exception as e:
            # this is a default catch all, follow the steps above
            print(f"Something went wrong and I didn't handle it: {e}")

        self.run()

    def start(self):
        self.run()


if __name__ == "__main__":
    pm = PumpkinMachine()
    pm.start()