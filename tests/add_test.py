# Import necessary packages here
import pytest

from py_dir.main import add

# ==========================================================================================
# ==========================================================================================
# File:    test.py
# Date:    March 10, 2023
# Author:  Jonathan A. Webb
# Purpose: Describe the types of testing to occur in this file.
# Instruction: This code can be run in hte following ways
#              - pytest # runs all functions beginnning with the word test in the
#                         directory
#              - pytest file_name.py # Runs all functions in file_name beginning
#                                      with the word test
#              - pytest file_name.py::test_func_name # Runs only the function
#                                                      titled test_func_name in
#                                                      the file_name.py file
#              - pytest -s # Runs tests and displays when a specific file
#                            has completed testing, and what functions failed.
#                            Also displays print statments
#              - pytest -v # Displays test results on a function by function
#              - pytest -p no:warnings # Runs tests and does not display warning
#                          messages
#              - pytest -s -v -p no:warnings # Displays relevant information and
#                                supports debugging
#              - pytest -s -p no:warnings # Run for record
# ==========================================================================================
# ==========================================================================================
# Insert Code here


def test_add():
    one: float = 2.1
    two: float = 3.3
    val = add(one, two)
    assert val == pytest.approx(5.4, rel=1.0e-3)


# ==========================================================================================
# ==========================================================================================
# eof
