#zm254-10/13/23
from MyCalc import MyCalc #import Mycalc class form MyCalc File
import pytest #importing pytest framework which is used for software test,including unit tests,end to end tests and functional tests
calc = MyCalc()
#zm254-10/13/23
def test_many_add():
    #zm254-10/13/23
    #testing using multiple values from this list
    data =[{
        "a":"2",
        "b":"2",
        "r":"4"
    },
    {
        "a":"4",
        "b":"4",
        "r":"8"
    },
    {
        "a":"1",
        "b":"1",
        "r":"2"

    },]
    for d in data:
        #checking if the test cases match and pass with our add function by passing the list values to the add function
        #using assertion to debug the code
        assert calc.add(d["a"],d["b"])== int (d["r"])

def test_many_sub():
    #zm254-10/13/23
    #testing using multiple values from this list
    data =[{
        "a":"3",
        "b":"2",
        "r":"1"
    },
    {
        "a":"5",
        "b":"3",
        "r":"2"
    },
    {
        "a":"10",
        "b":"2",
        "r":"8"
    },]
    for d in data:
        #checking if the test cases and pass with our sub function by passing the list values to the sub function
        #using assertion to debug the code
        assert calc.sub(d["a"],d["b"])==int(d["r"])


def test_many_mult():
    #zm254-10/13/23
    #testing using multiple values from the list
    data =[{
        "a":"3",
        "b":"2",
        "r":"6"
    },
    {
        "a":"5",
        "b":"3",
        "r":"15"
    },
    {
        "a":"10",
        "b":"2",
        "r":"20"
    },]
    for d in data:
        #checking if the test cases match and pass with our mult func by passing the list values to the mult function
        #using assertion to debug the code.
        assert calc.mult(d["a"],d["b"])== int (d["r"])

def test_many_div():
    #zm254-10/13/23
    #testing using mult values from this list
    data = [{
        "a":"10",
        "b":"2",
        "r":"5"
    },
    {
        "a":"9",
        "b":"3",
        "r":"3"
    },
    {
        "a":"15",
        "b":"3",
        "r":"5"
    },]
    for d in data:
        #chekcing if the test cases match and pass with our div func by passing the list values to the div func.
        #using assertion to debug the code
        assert calc.div(d["a"],d["b"])== int(d["r"])

#zm254-10/13/23        
@pytest.fixture #using fixtures to hold the data so itsreusable
def my_calc_ans_add():
    calc.ans = "3" #initial value as 3
    return [{
        "a":"ans", 
        "b":"2",
        "r":"5"
    },
    {
        "a":"ans", #ans is getting updated and assigned to "a" from the prev calc
        "b":"4",
        "r":"9"
    },
    {
        "a":"ans", #ans is getting updated and assigned to "a" from the prev calc
        "b":"1",
        "r":"10"
    },
    {
        "a":"ans", #ans is getting updated and assigned to "a" from the prev calc
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_add(my_calc_ans_add):
    #zm254 -10/13/23
    for d in my_calc_ans_add:
        #using if cond to checking negative results
        if "negative" in d and d["negative"]:
            #giving wrong res as input value and checking if the test cases are passing
            assert calc.add(d["a"],d["b"]) != int(d["r"])
        else:
            #doing nrml assertion like the above add test case.
            #passing a,b and the result "r" to the add func and running the test case.
            assert calc.add(d["a"],d["b"])==int(d["r"])

#zm254 -10/13/23
@pytest.fixture #using fictures to hold the data so its reusable
def my_calc_ans_sub():
    calc.ans = "20" #keeping ans=20 as the initial value
    #testing using mult values from this list
    return[{
        "a":"ans",
        "b":"5",
        "r":"15"
    },
    {
        "a":"ans", #ans is getting updated and assigned to a from the prev collection
        "b":"4",
        "r":"11"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"1",
        "r":"10"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_sub(my_calc_ans_sub):
    #zm254-10/13/23
    for d in my_calc_ans_sub:
        #using if cond to checking negative results
        if "negative" in d and d["negative"]:
            #giving wrong results as input value and checking if the test cases are passing
            assert calc.sub(d["a"],d["b"])!=int(d["r"])
        else:
            #doing nrml assertion like the above sub test case.
            #passing a,b and the result 'r' to the sub function and running the test case
            assert calc.sub(d["a"],d["b"])== int(d["r"])

#zm254 -10/13/23
@pytest.fixture #using  fixutres to hold the data so its reusable
def my_calc_ans_mult():
    calc.ans = "5" #keeping ans=5 as the initial value
    return [{
        "a":"ans",
        "b":"5",
        "r":"25"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"4",
        "r":"100"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"1",
        "r":"100"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"1",
        "negative":True,
        "r":"1"
    },]

def test_data_ans_mult(my_calc_ans_mult):
    #zm254- 13/10/23
    for d in my_calc_ans_mult:
        #using if condition to checknig negative result
        if "negative" in d and d["negative"]:
            #giving wrong res as input val and checking if the test cases are passing
            assert calc.mult(d["a"],d["b"])!= int (d["r"])
        else:
            #doingg nrml assertion like the above mult test case.
            #passing a,b and the result 'r' to the mult fucntion and running the test case.
            assert calc.mult(d["a"],d["b"])== int(d["r"])

#zm254-10/13/23
@pytest.fixture #using fixture to hold the data so its reusable
def my_calc_ans_div():
    calc.ans = "20" #keeping ans=20 as initial
    return [{
        "a":"ans",
        "b":"2",
        "r":"10"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"5",
        "r":"2"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"1",
        "r":"2"
    },
    {
        "a":"ans",#ans is getting updated and assigned to a from the prev collection
        "b":"1",
        "negative":True,
        "r":"1"
    }]

def test_data_ans_div(my_calc_ans_div):
    #zm254-10/13/23
    for d in my_calc_ans_div:
        #using if cond to checking negative results
        if "negative" in d and d["negative"]:
            #giving wrong results as input value and checking of the test cases are passing
            assert calc.div(d["a"],d["b"])!= int(d["r"])
        else:
            #doing nrml assertion like the above div test case.
            #passing a,b and the result 'r' to the div function and running the test case.
            assert calc.div(d["a"],d["b"])==int(d["r"])