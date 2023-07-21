cmake_minimum_required(VERSION 3.12)
project(dhc)

# Set C++ standard to C++20
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# set compiler to clang
set(CMAKE_CXX_COMPILER clang++)

# Add source files
file(GLOB_RECURSE SOURCE_FILES "${CMAKE_SOURCE_DIR}/*.cpp" EXCLUDE "${CMAKE_SOURCE_DIR}/CMakeFiles/**/*.cpp")

# Define the target executable
add_executable(dhc ${SOURCE_FILES})

# Add include directories
target_include_directories(dhc PRIVATE ${CMAKE_SOURCE_DIR}/../libraries)
