# Minimum version of CMake required
cmake_minimum_required(VERSION 3.14)

# Project name and language
project(CMathProject C)

# --- Define the main application executable ---
# This creates the interactive program from math1.c that you can run.
add_executable(math_app
    "math1.c"
)

# --- Define the test executable ---
# This creates the test runner executable from your Unity test file.
add_executable(run_tests
    "test_math1.c"
    "math1.c"
    "unity.c" # Include the Unity source file
)

# Add a compile definition to exclude the main() function from math1.c
# when building this test executable. This prevents a "multiple definition" linker error.
target_compile_definitions(run_tests PRIVATE EXCLUDE_MAIN_FOR_TESTS)

# --- Enable Testing ---
# This allows you to run tests with the 'ctest' command.
enable_testing()
add_test(NAME MathTests COMMAND run_tests)