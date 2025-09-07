/******************************************************************************

                            Online C Compiler.
This is a refactored version of the original code to be more structured,
robust, and user-friendly.

*******************************************************************************/
#include <stdio.h>
#include <math.h>
#include "math1.h"

// By wrapping main in this #ifndef block, we can exclude it from the test build
// by defining EXCLUDE_MAIN_FOR_TESTS in our CMakeLists.txt for the test target.
// This prevents a "multiple definition of main" linker error.
#ifndef EXCLUDE_MAIN_FOR_TESTS

int call_main() {
    int choice;
    do {
        show_menu();
        printf("Enter your choice (0-9): ");
        
        // Basic input validation
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Please enter a number.\n\n");
            // Clear the input buffer to prevent an infinite loop
            while (getchar() != '\n');
            choice = -1; // Set to an invalid choice to continue loop
            continue;
        }

        switch (choice) {
            case 1: perform_basic_math(); break;
            case 2: add_two_numbers(); break;
            case 3: multiply_two_numbers(); break;
            case 4: generate_multiplication_table(); break;
            case 5: generate_division_table(); break;
            case 6: divide_two_numbers_quotient_remainder(); break;
            case 7: divide_two_floats(); break;
            case 8: calculate_average(); break;
            case 9: calculate_power(); break;
            case 10: print_name(); break;
            case 0: printf("Exiting program. Goodbye!\n"); break;
            default: printf("Invalid choice. Please try again.\n");
        }
        printf("\n");
    } while (choice != 0);

    return 0;
}
#endif // EXCLUDE_MAIN_FOR_TESTS

void show_menu() {
    printf("--- C Math Program Menu ---\n");
    printf("1.  Basic Math on 3 Integers (Add, Subtract, Multiply)\n");
    printf("2.  Add Two Integers\n");
    printf("3.  Multiply Two Integers\n");
    printf("4.  Generate Multiplication Table\n");
    printf("5.  Generate Division Table\n");
    printf("6.  Divide Integers (Quotient & Remainder)\n");
    printf("7.  Divide Two Decimal Numbers\n");
    printf("8.  Calculate Average of 3 Integers\n");
    printf("9.  Calculate Power (base^exponent)\n");
    printf("10. Print a Name\n");
    printf("0.  Exit\n");
    printf("---------------------------\n");
}

void generate_multiplication_table() {
  int n;
  printf("Enter an integer: ");
  scanf("%d", &n);

  for (int i = 1; i <= 10; ++i) {
    printf("%d * %d = %d \n", n, i, n * i);
  }
}

/**
 * @brief Testable function to add two integers.
 * This function contains only the core logic.
 */
int add(int a, int b) {
    return a + b;
}

#include <stdio.h>

// Testable logic function
int add1(int a, int b) {
    return a + b;
}

// Input/output wrapper
int add_two_numbers() {
    int number1, number2, sum;

    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    // Call the testable logic function
    sum = add(number1, number2);
    printf("Result: %d + %d = %d\n", number1, number2, sum);
    return sum; // Return the result for testing purposes
}

int add_main() {
    add_two_numbers();
    return 0;
}

void divide_two_numbers_quotient_remainder() {
    int dividend, divisor, quotient, remainder;

    printf("Enter dividend: ");
    scanf("%d", &dividend);

    printf("Enter divisor: ");
    scanf("%d", &divisor);

    if (divisor == 0) {
        printf("Error: Cannot divide by zero.\n");
    } else {
        quotient = dividend / divisor;
        remainder = dividend % divisor;

        printf("Quotient = %d\n", quotient);
        printf("Remainder = %d\n", remainder);
    }
}

void generate_division_table() {
    int num;
    float result;

    printf("Enter an integer to generate its division table: ");
    scanf("%d", &num);

    printf("Division Table of %d:\n", num);
    printf("-------------------\n");

    for (int i = 1; i <= 10; i++) {
        if (i == 0) continue; // Should not happen in this loop, but good practice
        result = (float)num / i;
        printf("%d / %d = %.2f\n", num, i, result);
    }
}

void multiply_two_numbers() {
    int num1, num2, product;

    printf("Enter the first integer: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    product = num1 * num2;
    printf("Result: %d * %d = %d\n", num1, num2, product);
}

void divide_two_floats() {
    float num1, num2;

    printf("Enter the numerator (can be a decimal): ");
    scanf("%f", &num1);

    printf("Enter the denominator (can be a decimal): ");
    scanf("%f", &num2);

    if (num2 == 0) {
        printf("Cannot divide by zero.\n");
    } else {
        float result = num1 / num2;
        printf("Result: %.2f / %.2f = %.2f\n", num1, num2, result);
    }
}

void calculate_power() {
    double base, exp, result;

    printf("Enter the base number: ");
    scanf("%lf", &base);

    printf("Enter the exponent: ");
    scanf("%lf", &exp);

    result = pow(base, exp);
    printf("Result: %.2lf ^ %.2lf = %.2lf\n", base, exp, result);
}

void print_name() {
    // Allocate enough space. "saisamridh" is 10 chars + 1 for null terminator.
    char myname[11] = "saisamridh";
    printf("My name is: %s\n", myname);
}

void perform_basic_math() {
    int num1, num2, num3, result;
    printf("Enter three integers, separated by spaces: ");
    scanf("%d %d %d", &num1, &num2, &num3);
 
    result = num1 + num2 + num3;
    printf("Addition: %d + %d + %d = %d\n", num1, num2, num3, result);

    result = num1 - num2 - num3;
    printf("Subtraction: %d - %d - %d = %d\n", num1, num2, num3, result);
 
    result = num1 * num2 * num3;
    printf("Multiplication: %d * %d * %d = %d\n", num1, num2, num3, result);
}

/**
 * @brief Testable function to calculate the average of three integers.
 * This function contains only the core logic.
 */
float average(int a, int b, int c) {
    // Use 3.0f to ensure the division is done with floating-point precision.
    return (a + b + c) / 3.0f;
}

int calculate_average() {
    int num1, num2, num3;
    float avg;
    printf("Enter three integers to average, separated by spaces: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    // Call the testable logic function
    avg = average(num1, num2, num3);
    printf("The average of %d, %d, and %d is: %.2f\n", num1, num2, num3, avg);
    return avg; // Return the result for testing purposes
}

int sq_areamain() {
    float side, area;

    // Ask the user for the side of the square
    printf("Enter the side of the square: ");
    scanf("%f", &side);

    // Calculate the area
    area = side * side;

    // Display the result
    printf("Area of the square = %.2f\n", area);

    return 0;
}

int rect_areamain() {
    float length, width, area;

    // Ask the user for length and width
    printf("Enter the length of the rectangle: ");
    scanf("%f", &length);

    printf("Enter the width of the rectangle: ");
    scanf("%f", &width);

    // Calculate the area
    area = length * width;

    // Display the result
    printf("Area of the rectangle = %.2f\n", area);

    return 0;
}

int UT_main(){

    call_main();
    sq_areamain();
    rect_areamain();
    return 0;
}
