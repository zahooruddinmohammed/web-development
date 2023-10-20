import pytest
# make sure there's an __init__.py in this test folder and that
# the test folder is in the same folder as the mini project content
from PumpkinMachine import PumpkinMachine
from PumpkinMachineExceptions import InvalidCombinationException,ExceededRemainingChoicesException, OutOfStockException
# this is an example test showing how to cascade fixtures to build up state
import random
#zm254-10/20/23
@pytest.fixture
def machine():
    pm = PumpkinMachine()
    return pm

# sample fixture, can delete if not using


@pytest.fixture
def first_order(machine):
    machine.reset()
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Happy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("done")
    #machine.handle_pay(10000, "10000")
    machine.handle_pay(machine.calculate_cost(),f"{machine.calculate_cost():.2f}")
    return machine

# sample fixture, can delete if not using


@pytest.fixture
def second_order(first_order,machine):
    machine.handle_pumpkin_choice("Large Pumpkin")#3
    machine.handle_face_stencil_choice("Spooky Face")#1
    machine.handle_face_stencil_choice("Toothy Face")#1
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")#.25
    machine.handle_extra_choice("Dry Ice")#.25
    machine.handle_extra_choice("done")
    machine.handle_pay(machine.calculate_cost(),f"{machine.calculate_cost():.2f}")
    # machine.handle_pay(10000,"10000")
    return machine

# sample test case, can delete if not using
@pytest.fixture
def third_order(second_order,machine):
    machine.handle_pumpkin_choice("Mini Pumpkin")
    machine.handle_face_stencil_choice("Spooky Face")
    machine.handle_face_stencil_choice("Toothy Face")
    machine.handle_face_stencil_choice("next")
    machine.handle_extra_choice("LED Candle")
    machine.handle_extra_choice("Dry Ice")
    machine.handle_extra_choice("done")
    machine.handle_pay(machine.calculate_cost(),f"{machine.calculate_cost():.2f}")
    return machine

def test_first_selection(machine):
    try:
        #zm254-10/20/23
        #order of selection needs to be correct
        #and then it checks if exception is raised if the order is not correct
        machine.handle_face_stencil_choice("Happy Face")
        machine.handle_extra_choice("LED Candle")
        assert False
    except InvalidCombinationException:
        assert True
    
def test_face_stencil_instock(machine):
    try:
        #zm254-10/20/23
        #test case checks if the exception is raised when the out of stock face stencil is choosen by user
        machine.reset()
        tmp = machine.face_stencils[0].quantity
        machine.face_stencils[0].quantity = 0
        machine.handle_pumpkin_choice("Mini Pumpkin")
        machine.handle_face_stencil_choice(machine.face_stencils[0].name)
        assert False
    except OutOfStockException:
        machine.face_stencils[0].quantity =tmp
        assert True


def test_extra_instock(machine):
    try:
        #zm254-10/20/23
        #test case checks if the exception is raised when the user chooses more than 3 extras
        machine.reset()
        tmp = machine.extras[0].quantity
        machine.extras[0].quantity =0
        print(machine.currently_selecting)
        machine.handle_pumpkin_choice("Large Pumpkin")
        machine.handle_face_stencil_choice(machine.face_stencils[0].name)
        machine.handle_face_stencil_choice("next")
        machine.handle_extra_choice(machine.extras[0].name)
        assert False
    except OutOfStockException:
        machine.extras[0].quantity =tmp
        assert True
    

def test_max_face_stencil(machine):
    try:
        #zm254-10/20/23
        #this test case checks if the exception is raised when the user  chooses more than 3 face stencil
        machine.reset()
        machine.handle_pumpkin_choice("Mini Pumpkin")
        machine.handle_face_stencil_choice(machine.face_stencils[0].name)
        machine.handle_face_stencil_choice(machine.face_stencils[0].name)
        machine.handle_face_stencil_choice(machine.face_stencils[0].name)
        machine.handle_face_stencil_choice(machine.face_stencils[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True


def test_max_extras(machine: PumpkinMachine):
    try:
        #zm254-10/20/23
        #test case chceks if the exception is raised when the user chooses more than 3 extras
        machine.handle_pumpkin_choice("Mini Pumpkin")
        machine.handle_face_stencil_choice("next")
        machine.handle_extra_choice(machine.extras[0].name)
        machine.handle_extra_choice(machine.extras[0].name)
        machine.handle_extra_choice(machine.extras[0].name)
        machine.handle_extra_choice(machine.extras[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True


def test_cost_calculation(machine):
    #zm254-10/20/23
    #chekcs if the total cost returned by the calculate_cost is correct
    #checking for all possibilites like pumpkin,face_stencil,extra  using random module
    for i in range(4):
        expected_cost =0
        machine.reset()
        random_pumpkin_choice =  random.choice(machine.pumpkins)
        random_face_stencil_choice = random.choice(machine.face_stencils)
        random_extra_choice = random.choice(machine.extras)
        expected_cost = random_pumpkin_choice.cost + random_face_stencil_choice.cost + random_extra_choice.cost
        machine.handle_pumpkin_choice(random_pumpkin_choice.name)
        machine.handle_face_stencil_choice(random_face_stencil_choice.name)
        machine.handle_face_stencil_choice("next")
        machine.handle_extra_choice(random_extra_choice.name)
        machine.handle_extra_choice("done")
        if f"{expected_cost:.2f}" != f"{machine.calculate_cost():.2f}":
            assert False
        machine.handle_pay(machine.calculate_cost(), f"{expected_cost:.2f}")
    machine.reset()
    assert True 

def test_total_sales(third_order):
    #zm254-10/20/23
    #function is used for total sales
    #using fixtures
    first_order_expected_Cost =2
    second_order_expected_Cost =5.5
    third_order_expected_Cost =3.5
    assert third_order.total_sales == first_order_expected_Cost+second_order_expected_Cost+third_order_expected_Cost

def test_total_pumpkin(third_order):
    #zm254-10/20/23
    #used for total_products
    #to check if the total_products is increased properly
    #testing using fixtures
    assert third_order.total_products == 3 


# #def test_production_line(second_order):
#     for j in second_order.pumpkins:
#         print(second_order.inprogress_pumpkin)
#         if j.name.lower() == second_order.inprogress_pumpkin[0].name.lower():
#             print(f"Pumkin {j.name.lower()} matches in progress \
#                   {second_order.inprogress_pumpkin[0].name.lower()}")
#             assert True
#             return

#     assert False

# add required test cases below