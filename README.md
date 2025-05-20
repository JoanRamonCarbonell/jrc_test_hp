# libone — A C++ Library Exposed to Python with pybind11

This project wraps a C++ function

## Function

Main function exposed to Python:

```cpp
long find(double (*f)(long), double y, long a, long b);
```

- This function finds an integer x in the range [a, b], that matches f(x) == y.

- f(x) is an increasing function.

## Install Python dependencies:
python3 -m pip install -U pip pybind11

## Clone the repo and enter it
git clone https://github.com/JoanRamonCarbonell/jrc_test_hp.git

cd your-repo

## Create build directory
mkdir -p build
cd build

## Configure with CMake
cmake ..

## Build the C++ library and Python bindings
make buildlib

## Install the Library and Headers:
sudo make installlib

## Running Tests
cd ..
python3 test/one_test.py


## Project Structure:
```
your-project/
├── CMakeLists.txt
├── includes/
│   └── libone/
│       └── one.h         # C++ header
├── src/
│   └── one.cpp           # C++ implementation
│   └── bindings.cpp      # pybind11 binding code
├── test/
│   └── one_test.py       # Python tests
└── build/                # (created during build)
```


This project includes a GitHub Actions workflow that works on all branches.

See .github/workflows/build.yml.


