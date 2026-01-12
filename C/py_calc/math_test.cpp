#include <gtest/gtest.h>

// Use extern "C" to tell the C++ compiler that the functions in math1.h
// are C functions, not C++ functions.
extern "C" {
    #include "math1.h"
}

// Test fixture for the add function
TEST(MathFunctionsTest, Add) {
    EXPECT_EQ(add(5, 3), 8);
    EXPECT_EQ(add(-1, 1), 0);
    EXPECT_EQ(add(0, 0), 0);
    EXPECT_EQ(add(-5, -10), -15);
    EXPECT_EQ(add(-15, -10), -25);
    EXPECT_EQ(add(-15, 10), -5);

}

// Test fixture for the average function
TEST(MathFunctionsTest, Average) {
    // Use ASSERT_FLOAT_EQ for comparing floating-point numbers
    ASSERT_FLOAT_EQ(average(1, 2, 3), 2.0f);
    ASSERT_FLOAT_EQ(average(10, 20, 30), 20.0f);
    ASSERT_FLOAT_EQ(average(0, 0, 0), 0.0f);
    ASSERT_FLOAT_EQ(average(-1, 0, 1), 0.0f);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}