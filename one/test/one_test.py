# from __future__ import print_function   # to make print() work in python2 -> python2 not supported for Ubuntu 24.04
import sys
import os

# Add build directory to import path, so that libone_bindings can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build')))

import libone_bindings


# Increasing functions returning double
def increment(x):
    return float(x + 1)

def run_tests():
    print("Run tests with increasing functions...\n")

    # 1.1 increment(x) == 6 in [0,10] -> x = 5
    res = libone_bindings.find(increment, 6.0, 0, 10)
    print("Test 1.1 - Range [0,10], increment(x) = 6:", res)
    assert res == 5

    # 1.2 increment(x) == 11 in [0,10] -> x = -1
    res = libone_bindings.find(increment, 11.0, 0, 10)
    print("Test 1.2 - Range [0,10], increment(x) = 11:", res)
    assert res == -1

    # 1.3 increment(x) == 4 in [5,10] -> x = -1
    res = libone_bindings.find(increment, 4.0, 5, 10)
    print("Test 1.3 - Range [5,10], increment(x) = 4:", res)
    assert res == -1

    # 1.4 increment(x) == 4 in [-5,10] -> x = -1
    res = libone_bindings.find(increment, 4.0, -5, 10)
    print("Test 1.4 - Range [-5,10], increment(x) = 4:", res)
    assert res == -1

    # 1.5 increment(x) == 4 in [10,0] -> x = -1
    res = libone_bindings.find(increment, 4.0, 10, 0)
    print("Test 1.5 - Range [10,0], increment(x) = 4:", res)
    assert res == -1


    print("\nAll tests passed.")


if __name__ == '__main__':
    run_tests()
