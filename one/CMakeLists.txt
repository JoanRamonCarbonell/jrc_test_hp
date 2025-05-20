cmake_minimum_required(VERSION 3.14)
project(libone)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Create a library target from src file
add_library(libone SHARED src/one.cpp)


# libone include public for someone to link with 
target_include_directories(libone PUBLIC includes/libone)

# using pybind11 for python binding with C++
find_package(pybind11 REQUIRED)

# Create bindings for python module
pybind11_add_module(libone_bindings
    src/one.cpp           # Reuse the implementation
    src/bindings.cpp      # Bindings logic for Python
)

# libone_bindings include is private 
target_include_directories(libone_bindings PRIVATE includes/libone)
