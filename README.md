# QA Coding Solution

# Design decisions
I realize that the challenge required me to write just one automated test. 
So, I could have used components in the Python Standard Library such as Py.Unit, urllib2 for this exercise. 
But, in this example, I am trying to showcase how I would build a larger test framework that can scale as 
requirements and testing needs grow. So I used PyTest and the Requests library, both of which are 3rd party 
libraries but extremely popular ones.

The test has been written to handle *PASS* for the happy path, and *FAIL* for http errors, timeouts, and other exceptions

# Files and directories in the repo

## For Challenge 1:

- README.md --> The readme file for the repo that you are currently reading! :-)
- conftest.py --> This is the first file that Pytest will discover and execute. It contains test fixtures.
- config.yaml --> A config file that contains the URLS to be tested - used for clean separation of concerns from the tests
- requirements.txt --> All the Python modules required to run the tests
- tests/test_availability.py --> The *tests* folder has the one test file - *test_availability.py* - that has the test case  

## For Challenge 2:
- testplan/testplan.md --> The *testplan* folder has the test plan file - *testplan.md* 


# Instructions to install and execute the tests
#### NOTE: Instructions were tested on MacOS and Linux. Should work on Windows but not verified.
- Clone this repo to your local machine - https://github.com/vbhandari/QACodingChallenge
- You will need Python3 to execute the tests. So, make sure Python3 is installed and in your execution path.
- As a Python best practice, create a new Python virtual environment - let's name it venv
- Activate the newly created Python virtual environment as follows - *source venv/bin/activate*
- Then use the requirements.txt file to install the dependencies for the tests as follows - *pip install -r requirements.txt* 
- From the top level of the directory tree (at the same level as the file **conftest.py**), run the tests as follows:
**pytest -sv .** (Note the trailing '.')
- You can also run the tests as **pytest -sv tests**
- Pytest will discover and execute one test - *tests/test_availability.py::test_google_is_available*
- You should see the result as **PASSED**

#### Here is an example of tests running:
>
(venv) sh-3.2$ pytest -sv .

============================= test session starts ==============================

platform darwin -- Python 3.7.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1 -- /Users/vinay/code/vbhandari/QACodingChallenge/venv/bin/python

cachedir: .pytest_cache

rootdir: /Users/vinay/code/vbhandari/QACodingChallenge

plugins: timeout-1.4.1

collected 1 item                                                               

tests/test_availability.py::test_google_is_available PASSED

============================== 1 passed in 0.26s ===============================