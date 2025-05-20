cmake_minimum_required(VERSION 3.14)
project(libone)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add FetchContent module
include(FetchContent)

# Download and make available pybind11
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.11.1
)
# using pybind11 for python binding with C++
FetchContent_MakeAvailable(pybind11)

# Create a library target from src file
add_library(libone SHARED src/one.cpp)

# libone include public for someone to link with 
target_include_directories(libone PUBLIC includes/libone)

# Create bindings for python module
pybind11_add_module(libone_bindings
    src/bindings.cpp      # Bindings logic for Python
)

# Link the Python module with the C++ library
target_link_libraries(libone_bindings PRIVATE libone)

# libone_bindings include is private 
target_include_directories(libone_bindings PRIVATE includes/libone)
