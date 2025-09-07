# Minimum version of CMake required
cmake_minimum_required(VERSION 3.14)

# Project name and languages
project(CMathProject C CXX)

# Set the C++ standard. Google Test requires at least C++14.
# This is a common fix for gtest build failures with some compilers.
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- Define the main application executable ---
# This creates the interactive program from math1.c that you can run.
add_executable(math_app
    "math1.c"
)

# --- Fetch Google Test ---
# This automatically downloads and configures GTest for your project.
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)

# By setting BUILD_TESTING to OFF, we prevent googletest from building its own internal tests,
# which can sometimes cause issues in the sub-build process.
# We also disable installation of gtest to keep the build self-contained.
set(INSTALL_GTEST OFF)
set(BUILD_TESTING OFF)
FetchContent_MakeAvailable(googletest)

# --- Define the test executable ---
# This tells CMake to create a separate program called "run_tests".
# It includes the test code and the C code it needs to test.
add_executable(run_tests
    "math_test.cpp" # The C++ test file
    "math1.c"       # The C source file to be tested
)

# Add a compile definition to exclude the main() function from math1.c
# when building this test executable. This prevents a "multiple definition" linker error.
target_compile_definitions(run_tests PRIVATE EXCLUDE_MAIN_FOR_TESTS)

# Link the test executable with the GTest libraries.
# gtest_main provides a main() function for the test runner.
target_link_libraries(run_tests PRIVATE gtest_main)

# --- Enable Testing ---
# This allows you to run tests with the 'ctest' command.
include(GoogleTest)
gtest_discover_tests(run_tests)