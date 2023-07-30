# 🧪 Mocking and Patching 🧪

![Python](https://img.shields.io/badge/Python-3.10.6-blueviolet)

![Pyenv](https://img.shields.io/badge/Pyenv-1.2.30-yellow)

![Requests](https://img.shields.io/badge/Requests-2.26.0-orange)

## Installation and Set Up 🛠️
1. Ensure you have Python 3.10.6 installed. Make sure that your `pyenv` installation has this version available.
2. 🍴 Fork and clone the repository to your local machine.
3. install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt#
   ```

## Project Description 📜
This project explores the testing concepts of mocking and patching in Python.

Mocks and patches are powerful testing tools in Python used to isolate units of code during testing. 

A mock is an object that mimics the behavior of a real object in a controlled manner. It allows you to create a test double that stands in for the real object, enabling you to test the interactions with that object without actually invoking it.

A patch is a way to temporarily replace an object or function in the code being tested with a mock. It is typically used to isolate the unit under test from external dependencies. Patches can be applied to classes, functions, or modules, allowing you to control what is returned or called during the test execution.

The mocks and patches I use in this project are implemented to test the projects two main classes, NumberRequester and NumberCruncher, designed to interact with the numbersapi endpoint to retrieve and process random number facts.

### NumberRequester Class 📞
The NumberRequester class retrieves random number facts from the numbersapi endpoint using the requests API to make REST calls. It logs the results of each request and returns a dictionary with the number and its associated fact.

Example:
In the Python 🐍 REPL:

```python
>>> from cruncher import NumberRequester
>>> nr = NumberRequester()
>>> nr.call()
{'result': 'SUCCESS', 'number': 473, 'fact': '473 is the largest known number whose square and 4^{th} power use different digits.'}

```

### NumberCruncher Class 🍔
The NumberCruncher class simulates an entity that eats number facts with a limited tummy size. Upon initialization, you need to specify the size of its tummy (i.e., how many number facts it can store). It has a built-in NumberRequester for fetching number facts. When you call the crunch() method, it uses the NumberRequester to get a number fact and does one of the following:

Rejects the fact with a "Yuk!" message if the number is odd.
Eats the fact and returns a "Yum!" message if the number is even and its tummy is not full.
Expels the oldest fact from its tummy to make room for the new one and returns a "Burp!" message if the number is even and its tummy is full.

Example:
In the Python 🐍 REPL:

```python
>>> from cruncher import NumberCruncher
>>> nc = NumberCruncher(3)  # A NumberCruncher that can store 3 facts
>>> nc.crunch()
'Yum! 8100'   # stored 8100. NumberRequester is invoked from within NumberCruncher
>>> nc.crunch()
'Yuk! 5335'
>>> nc.crunch()
'Yum! 730'  # stored
>>> nc.tummy
[{'number': 8100, 'fact': '8100 is divisible by its reverse.'}, {'number': 730, 'fact': '730 is the number of connected bipartite graphs with 9 vertices.'}]
>>> nc.crunch()
'Yum! 436'  # stored - tummy full
>>> nc.crunch()
'Burp! 8100' # 8100 burped out to make room for the new fact
>>> nc.tummy
[{'number': 730, 'fact': '730 is the number of connected bipartite graphs with 9 vertices.'}, {'number': 436, 'fact': '436 is a boring number.'}, {'number': 5624, 'fact': '5624 is the number of binary 5×5 matrices up to permutations of rows and columns.'}]
>>> nc.requester.log
[{'request_number': 1, 'call_time': '2022-11-09T16:38:23.417667', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 8100},  
{'request_number': 2, 'call_time': '2022-11-09T16:38:26.111704', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 5335},  
{'request_number': 3, 'call_time': '2022-11-09T16:38:37.810081', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 730},  
{'request_number': 4, 'call_time': '2022-11-09T16:38:55.040040', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 436},  
{'request_number': 5, 'call_time': '2022-11-09T16:39:07.712827', 'end_point': 'http://numbersapi.com/random/math', 'result': 'SUCCESS', 'number': 5624}]


```
