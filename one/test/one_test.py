import sys
import os

# Add build directory to import path, so that libone_bindings can be found
# Compute the path to the build directory
build_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'build'))

# Add the build directory to the Python module search path
sys.path.insert(0, build_path)

import libone_bindings

def run_tests():
    print("Run tests with increasing functions...\n")

    # print(libone_bindings.find_square(16.0, 0, 10))  # Should print 4
    # print(libone_bindings.find_square(20.0, 0, 10))  # Should print -1

    # 1.1 square(x) == 36 in [0,10] -> x = 6
    res = libone_bindings.find_square(36.0, 0, 10)
    print("Test 1.1 - Range [0,10], square(x) = 36 -> x = ", res)
    assert res == 6

    # 1.2 square(x) == 100 in [0,10] -> x = 100
    res = libone_bindings.find_square(100.0, 0, 10)
    print("Test 1.2 - Range [0,10], square(x) = 100 -> x = ", res)
    assert res == 10

    # 1.3 square(x) == 1 in [1,10] -> x = 1
    res = libone_bindings.find_square(1.0, 1, 10)
    print("Test 1.3 - Range [1,10], square(x) = 1 -> x = ", res)
    assert res == 1

    # 1.4 square(x) == 25 in [5,5] -> x = 5
    res = libone_bindings.find_square(25.0, 5, 5)
    print("Test 1.4 - Range [5,5], square(x) = 25 -> x = ", res)
    assert res == 5

    # 1.5 square(x) == 1 in [2,10] -> x = -1
    res = libone_bindings.find_square(1.0, 2, 10)
    print("Test 1.5 - Range [2,10], square(x) = 1 -> x = ", res, " | Fail -> (1 < square(2))")
    assert res == -1

    # 1.6 square(x) == 20 in [2,10] -> x = -1
    res = libone_bindings.find_square(20.0, 2, 10)
    print("Test 1.6 - Range [2,10], square(x) = 20 -> x = ", res, " | Fail -> (No index in range matches 20 in this increasing function)")
    assert res == -1

    # 1.7 square(x) == 200 in [2,10] -> x = -1
    res = libone_bindings.find_square(200.0, 2, 10)
    print("Test 1.7 - Range [2,10], square(x) = 200 -> x = ", res, " | Fail -> (200 > square(10))")
    assert res == -1

    # 1.8 square(x) == 36 in [10,0] -> x = -1
    res = libone_bindings.find_square(36.0, 10, 0)
    print("Test 1.8 - Range [10,0], square(x) = 36 -> x = ", res, " | Fail -> (a > b)")
    assert res == -1

    # 1.9 square(x) == 36 in [-10,10] -> x = -1
    res = libone_bindings.find_square(36.0, -10, 10)
    print("Test 1.9 - Range [-10,10], square(x) = 36 -> x = ", res, " | Fail -> (a < 0)")
    assert res == -1

    print("\nAll tests passed.")

if __name__ == '__main__':
    run_tests()
