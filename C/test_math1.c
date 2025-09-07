#include "unity.h"
#include "math1.h" // Or use a header file
#include <math.h>

void setUp(void) {}
void tearDown(void) {}

void test_add_two_numbers(void) {
    // Positive numbers
    TEST_ASSERT_EQUAL(5, add(2, 3));
    TEST_ASSERT_EQUAL(10, add(5, 5));
    // Negative numbers
    TEST_ASSERT_EQUAL(-5, add(-2, -3));
    TEST_ASSERT_EQUAL(-10, add(-5, -5));
    // Mixed signs
    TEST_ASSERT_EQUAL(0, add(-2, 2));
    // Zero
    TEST_ASSERT_EQUAL(0, add(0, 0));
    // Assertions for inequality
    TEST_ASSERT_NOT_EQUAL(6, add(2, 3));
    TEST_ASSERT_NOT_EQUAL(1, add(-2, 2));
}

void test_calculate_average(void) {
    TEST_ASSERT_EQUAL_FLOAT(2.0f, average(1, 2, 3));
    TEST_ASSERT_EQUAL_FLOAT(3.0f, average(3, 3, 3));
    TEST_ASSERT_EQUAL_FLOAT(0.0f, average(0, 0, 0));
    TEST_ASSERT_EQUAL_FLOAT(0.0f, average(-1, 0, 1));

    // Assertions for inequality
    TEST_ASSERT_NOT_EQUAL(2.0f, average(1, 2, 4));
    TEST_ASSERT_NOT_EQUAL(3.0f, average(3, 3, 6));
    TEST_ASSERT_NOT_EQUAL(0.0f, average(0, 0, 2));

    // Assertions for floating point precision
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 2.0f, average(1, 2, 3));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 3.0f, average(3, 3, 3));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 0.0f, average(0, 0, 0));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 0.0f, average(-1, 0, 1));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 3.333f, average(2, 3, 5));
}

void test_multiply(void) {
    TEST_ASSERT_EQUAL(6, multiply(2, 3));
    TEST_ASSERT_EQUAL(-6, multiply(-2, 3));
    TEST_ASSERT_EQUAL(6, multiply(-2, -3));
    TEST_ASSERT_EQUAL(0, multiply(5, 0));
    TEST_ASSERT_EQUAL(0, multiply(0, 5));
}

void test_integer_divide(void) {
    int q, r;
    TEST_ASSERT_EQUAL(0, integer_divide(10, 3, &q, &r));
    TEST_ASSERT_EQUAL(3, q);
    TEST_ASSERT_EQUAL(1, r);

    TEST_ASSERT_EQUAL(0, integer_divide(10, 2, &q, &r));
    TEST_ASSERT_EQUAL(5, q);
    TEST_ASSERT_EQUAL(0, r);

    TEST_ASSERT_EQUAL(0, integer_divide(-10, 3, &q, &r));
    TEST_ASSERT_EQUAL(-3, q);
    TEST_ASSERT_EQUAL(-1, r);

    // Test division by zero
    TEST_ASSERT_EQUAL(-1, integer_divide(10, 0, &q, &r));
}

void test_float_divide(void) {
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 2.5f, float_divide(5.0f, 2.0f));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, -2.5f, float_divide(-5.0f, 2.0f));
    TEST_ASSERT_FLOAT_WITHIN(0.001f, 0.0f, float_divide(0.0f, 5.0f));
    TEST_ASSERT_FLOAT_IS_NAN(float_divide(5.0f, 0.0f));
}

void test_power(void) {
    TEST_ASSERT_EQUAL_DOUBLE(8.0, pow(2.0, 3.0));
    TEST_ASSERT_EQUAL_DOUBLE(1.0, pow(10.0, 0.0));
    TEST_ASSERT_EQUAL_DOUBLE(0.25, pow(2.0, -2.0));
    TEST_ASSERT_EQUAL_DOUBLE(1.0, pow(1.0, 100.0));
    TEST_ASSERT_EQUAL_DOUBLE(9.0, pow(-3.0, 2.0));
}

void test_get_name(void) {
    TEST_ASSERT_EQUAL_STRING("saisamridh", get_name());
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_add_two_numbers);
    RUN_TEST(test_calculate_average);
    RUN_TEST(test_multiply);
    RUN_TEST(test_integer_divide);
    RUN_TEST(test_float_divide);
    RUN_TEST(test_power);
    RUN_TEST(test_get_name);
    return UNITY_END();
}