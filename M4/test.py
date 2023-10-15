#zm254-10/13/23
from MyCalc import MyCalc
import pytest
calc = MyCalc()

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
        #checking if the test cases match 
        assert calc.mult(d["a"],d["b"])== int (d["r"])

def test_many_div():
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
        assert calc.div(d["a"],d["b"])== int(d["r"])
@pytest.fixture
def my_calc_ans_add():
    calc.ans = "3"
    return [{
        "a":"ans",
        "b":"2",
        "r":"5"
    },
    {
        "a":"ans",
        "b":"4",
        "r":"9"
    },
    {
        "a":"ans",
        "b":"1",
        "r":"10"
    },
    {
        "a":"ans",
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_add(my_calc_ans_add):
    for d in my_calc_ans_add:
        if "negative" in d and d["negative"]:
            assert calc.add(d["a"],d["b"]) != int(d["r"])
        else:
            assert calc.add(d["a"],d["b"])==int(d["r"])

@pytest.fixture
def my_calc_ans_sub():
    calc.ans = "20"
    return[{
        "a":"ans",
        "b":"5",
        "r":"15"
    },
    {
        "a":"ans",
        "b":"4",
        "r":"11"
    },
    {
        "a":"ans",
        "b":"1",
        "r":"10"
    },
    {
        "a":"ans",
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_sub(my_calc_ans_sub):
    for d in my_calc_ans_sub:
        if "negative" in d and d["negative"]:
            assert calc.sub(d["a"],d["b"]!=int(d["r"]))
        else:
            assert calc.sub(d["a"],d["b"])== int(d["r"])

@pytest.fixture
def my_calc_ans_mult():
    calc.ans = "5"
    return [{
        "a":"ans",
        "b":"5",
        "r":"25"
    },
    {
        "a":"ans",
        "b":"4",
        "r":"100"
    },
    {
        "a":"ans",
        "b":"1",
        "r":"100"
    },
    {
        "a":"ans",
        "b":"1",
        "negative":True,
        "r":"1"
    },]

def test_data_ans_mult(my_calc_ans_mult):
    for d in my_calc_ans_mult:
        if "negative" in d and d["negative"]:
            assert calc.mullt(d["a"],d["b"])!= int (d["r"])
        else:
            assert calc.mult(d["a"],d["b"])== int(d["r"])

@pytest.fixture
def my_calc_ans_div():
    calc.ans = "20"
    return [{
        "a":"ans",
        "b":"2",
        "r":"10"
    },
    {
        "a":"ans",
        "b":"5",
        "r":"2"
    },
    {
        "a":"ans",
        "b":"1",
        "r":"2"
    },
    {
        "a":"ans",
        "b":"1",
        "negative":True,
        "r":"1"
    }]

def test_data_ans_div(my_calc_ans_div):
    for d in my_calc_ans_div:
        if "negative" in d and d["negative"]:
            assert calc.div(d["a"],d["b"]!= int(d["r"]))
        else:
            assert calc.div(d["a"],d["b"])==int(d["r"])