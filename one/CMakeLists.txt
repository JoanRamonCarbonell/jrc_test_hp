cmake_minimum_required(VERSION 3.14)
project(libone)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include public headers globally as a beginnning
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/includes/libone)

# Create a library target from src file
add_library(libone SHARED src/one.cpp)
