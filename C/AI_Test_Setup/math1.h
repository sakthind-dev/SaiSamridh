#ifndef MATH1_H
#define MATH1_H

// This allows C++ code (like our tests) to link to C functions correctly.
#ifdef __cplusplus
extern "C" {
#endif

// --- Testable Logic Functions ---
// These functions perform calculations and return a result. They are easy to test.
int add(int a, int b);
float average(int a, int b, int c);

//--- Function Prototypes ---
void show_menu();
void perform_basic_math();
//int add_two_numbers();
void generate_multiplication_table();
void generate_division_table();
void divide_two_numbers_quotient_remainder();
void divide_two_floats();
void multiply_two_numbers();
//int calculate_average();
void calculate_power();
void print_name();

// --- Original I/O Functions ---
// These functions handle user interaction (printf, scanf).
int add_two_numbers();
int calculate_average();

#ifdef __cplusplus
}
#endif

#endif // MATH1_H