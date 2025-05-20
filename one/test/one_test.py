from __future__ import print_function   # to make print() work in python2
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
    print("Test 1 - increment(x) = 6:", res)
    assert res == 5


    print("\nAll tests passed.")


if __name__ == '__main__':
    run_tests()
