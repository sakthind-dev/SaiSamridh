#include "unity.h"
#include "math1.h" // Or use a header file

void setUp(void) {}
void tearDown(void) {}

void test_add_two_numbers(void) {
//    TEST_ASSERT_EQUAL(5, add_two_numbers(2, 3));
//    TEST_ASSERT_EQUAL(0, add_two_numbers(-2, 2));
    TEST_ASSERT_EQUAL(5, add(2, 3));
    TEST_ASSERT_EQUAL(0, add(-2, 2));
    TEST_ASSERT_EQUAL(-5, add(-2, -3));
    TEST_ASSERT_EQUAL(0, add(0, 0));
    TEST_ASSERT_EQUAL(10, add(5, 5));
    TEST_ASSERT_EQUAL(-10, add(-5, -5));
    TEST_ASSERT_NOT_EQUAL(6, add(2, 3));
    TEST_ASSERT_NOT_EQUAL(1, add(-2, 2));
    TEST_ASSERT_NOT_EQUAL(0, add(0, 0));
    TEST_ASSERT_NOT_EQUAL(8, add(5, 3));
    TEST_ASSERT_NOT_EQUAL(-8, add(-5, -3)); 
}

void test_calculate_average(void) {
    TEST_ASSERT_EQUAL(2.0f, average(1, 2, 3));
    TEST_ASSERT_EQUAL(3.0f, average(3, 3, 3));
    TEST_ASSERT_EQUAL(0.0f, average(0, 0, 0));
    TEST_ASSERT_EQUAL(-1.0f, average(-1, 0, 1));
    TEST_ASSERT_NOT_EQUAL(2.0f, average(1, 2, 4));
    TEST_ASSERT_NOT_EQUAL(3.0f, average(3, 3, 6));
    TEST_ASSERT_NOT_EQUAL(0.0f, average(0, 0, 2));
    TEST_ASSERT_NOT_EQUAL(-1.0f, average(-1, 0, 1));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 2.0f, average(1, 2, 3));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 3.0f, average(3, 3, 3));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 0.0f, average(0, 0, 0));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 0.0f, average(-1, 0, 1));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 3.333f, average(2, 3, 5));
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_add_two_numbers);
    RUN_TEST(test_calculate_average);
    return UNITY_END();
}