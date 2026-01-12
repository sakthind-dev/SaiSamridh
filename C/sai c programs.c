/******************************************************************************

                            Online C Compiler.
This is a refactored version of the original code to be more structured,
robust, and user-friendly.

*******************************************************************************/
#include <stdio.h>
#include <math.h>
// #include "math1.h" // Removed because the header file does not exist

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
 * @brief Testable function to multiply two integers.
 * This function contains only the core logic.
 */
int multiply(int a, int b) {
    return a * b;
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

/**
 * @brief Testable function to divide two integers and get quotient and remainder.
 * This function contains only the core logic.
 * @return 0 on success, -1 on division by zero.
 */
int integer_divide(int dividend, int divisor, int* quotient, int* remainder) {
    if (divisor == 0) {
        return -1; // Error: division by zero
    }
    *quotient = dividend / divisor;
    *remainder = dividend % divisor;
    return 0; // Success
}

void divide_two_numbers_quotient_remainder() {
    int dividend, divisor, quotient, remainder;

    printf("Enter dividend: ");
    scanf("%d", &dividend);

    printf("Enter divisor: ");
    scanf("%d", &divisor);

    if (integer_divide(dividend, divisor, &quotient, &remainder) != 0) {
        printf("Error: Cannot divide by zero.\n");
    } else {
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

    product = multiply(num1, num2);
    printf("Result: %d * %d = %d\n", num1, num2, product);
}

/**
 * @brief Testable function to divide two floats.
 * This function contains only the core logic.
 * @return The result of the division, or NAN if dividing by zero.
 */
float float_divide(float numerator, float denominator) {
    if (denominator == 0.0f) {
        return NAN; // Not-a-Number from math.h
    }
    return numerator / denominator;
}

void divide_two_floats() {
    float num1, num2;

    printf("Enter the numerator (can be a decimal): ");
    scanf("%f", &num1);

    printf("Enter the denominator (can be a decimal): ");
    scanf("%f", &num2);

    float result = float_divide(num1, num2);
    if (isnan(result)) {
        printf("Cannot divide by zero.\n");
    } else {
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

/**
 * @brief Testable function to get a name.
 * This function contains only the core logic.
 */
const char* get_name(void) {
    // Statically allocated so it remains valid after function returns
    static char myname[] = "myname";
    return myname;
}

void print_name() {
    // Allocate enough space. "saisamridh" is 10 chars + 1 for null terminator.
    char myname[11] = "myname";
    printf("My name is: %s\n", myname);
    printf("My name is: %s\n", get_name());
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

// By wrapping main in this #ifndef block, we can exclude it from the test build
// by defining EXCLUDE_MAIN_FOR_TESTS in our CMakeLists.txt for the test target.
// This prevents a "multiple definition of main" linker error.
#ifndef EXCLUDE_MAIN_FOR_TESTS

int main(){

    call_main();
    sq_areamain();
    rect_areamain();
    return 0;
}
#endif // EXCLUDE_MAIN_FOR_TESTS



#include<stdio.h>

int main() {

    int a=5,b=1,c;

    c=a+b;

    printf("a+b= %d \n",c);

    c=a-b;

    printf("a-b= %d \n",c);
c=a*b;

    printf("a*b= %d \n",c);
c=a/b;

    printf("a/b= %d \n",c);

    c=a%b;

    printf("REMAINDER WHEN DIVIDED BY B =%d \n",c)
;
    return 0;
}

#include <stdio.h>

int main() {
    int number1, number2, remainder;

    printf("Enter the first number (dividend): ");
    scanf("%d", &number1);

    printf("Enter the second number (divisor): ");
    scanf("%d", &number2);

    remainder = number1 % number2;

    printf("Remainder when %d is divided by %d is: %d\n", number1, number2, remainder);

    return 0}


#include <stdio.h>

int main() {
    char name[15] = "SAISAMRIDH";
    printf("%s\n", name); 
    return 0;
}


#include <stdio.h>

int main() {
    char myChar = 'A'; 
    printf("%c\n", myChar); 

    return 0;
}

#include <stdio.h>

int main() {
    int a = 3, b = 4, c = 5;
    int median;


    if ((a > b && a < c) || (a < b && a > c))
        median = a;
    else if ((b > a && b < c) || (b < a && b > c))
        median = b;
    else
        median = c;

    printf("The median of %d, %d, and %d is: %d\n", a, b, c, median);
    return 0;
}


#include <stdio.h>
#include <string.h>

int main() {
    char piece[10], color[10];

    printf("Enter the chess piece (king, queen, bishop, knight, rook, pawn): ");
    scanf("%s", piece);

    printf("Enter the color (white or black): ");
    scanf("%s", color);

    if (strcmp(color, "white") == 0 || strcmp(color, "black") == 0) {
        if (strcmp(piece, "king") == 0)
            printf("Moves one square in any direction.\n");
        else if (strcmp(piece, "queen") == 0)
            printf("Moves diagonally, horizontally, or vertically any number of squares.\n");
        else if (strcmp(piece, "bishop") == 0)
            printf("Moves diagonally any number of squares.\n");
        else if (strcmp(piece, "knight") == 0)
            printf("Moves in an L-shape: two squares in one direction and then one square perpendicular.\n");
        else if (strcmp(piece, "rook") == 0)
            printf("Moves horizontally or vertically any number of squares.\n");
        else if (strcmp(piece, "pawn") == 0)
            printf("Moves forward one square. On first move, can move two squares. Captures diagonally.\n");
        else
            printf("Invalid piece.\n");
    } else {
        printf("Invalid color.\n");
    }

    return 0;
}

#include <stdio.h>

int main() {
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    if (number % 2 == 0) {
        printf("The number is even.\n");
    } else {
        printf("The number is odd.\n");
    }

    return 0;
}


#include <stdio.h>

int main() {
    int i;
    printf("2 Times Table:\n");
    for(i = 1; i <= 10; i++) {
        printf("2 x %d = %d\n", i, 2 * i);
    }
    return 0;
}
print("2 Times Table:")
for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")

    #include <stdio.h>

int main() {
    int i, j;
    for(i = 2; i <= 12; i++) {
        printf("\nTable of %d:\n", i);
        for(j = 1; j <= 10; j++) {
            printf("%d x %d = %d\n", i, j, i * j);
        }
    }
    return 0;
}
for i in range(2, 13):
    print(f"\nTable of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
        #include <stdio.h>

int main() {
    int num1, num2, remainder;

    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    remainder = num1 % num2;

    printf("Remainder when %d is divided by %d = %d\n", num1, num2, remainder);

    return 0;
}
#include <stdio.h>

int main() {
    int choice, a, b;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    printf("Choose operation:\n");
    printf("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n");
    scanf("%d", &choice);

    switch(choice) {
        case 1:
            printf("Result = %d\n", a + b);
            break;
        case 2:
            printf("Result = %d\n", a - b);
            break;
        case 3:
            printf("Result = %d\n", a * b);
            break;
        case 4:
            if(b != 0)
                printf("Result = %d\n", a / b);
            else
                printf("Division by zero not allowed!\n");
            break;
        default:
            printf("Invalid choice!\n");
    }

    return 0;
}
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero not allowed!")
else:
    print("Invalid choice!")

    # Simple calculator using match-case (Python 3.10+)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Result =", a + b)
    case 2:
        print("Result =", a - b)
    case 3:
        print("Result =", a * b)
    case 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Division by zero not allowed!")
    case _:
        print("Invalid choice!")

        # Subtraction of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Difference =", a - b)

# Multiplication of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Product =", a * b)

# Division of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if b != 0:
    print("Quotient =", a / b)
else:
    print("Division by zero not allowed!")

    # Average of n numbers
n = int(input("How many numbers? "))
total = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total / n
print("Average =", average)


#include <stdio.h>

int main() {
    float base, height, area;

    printf("Enter base: ");
    scanf("%f", &base);

    printf("Enter height: ");
    scanf("%f", &height);

    area = base * height;
    printf("Area of Parallelogram = %.2f\n", area);

    return 0;
}

# Area of Triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = 0.5 * base * height
print("Area of Triangle =", area)

# Area of Parallelogram
base = float(input("Enter base: "))
height = float(input("Enter height: "))

area = base * height
print("Area of Parallelogram =", area)

#include <stdio.h>

int main() {
    int i = 1;

    printf("While Loop:\n");
    while(i <= 5) {
        printf("%d\n", i);
        i++;
    }

    return 0;
}

#include <stdio.h>

int main() {
    int i = 1;

    printf("Do-While Loop:\n");
    do {
        printf("%d\n", i);
        i++;
    } while(i <= 5);

    return 0;
}

#include <stdio.h>

int main() {
    int i;

    printf("Using break:\n");
    for(i = 1; i <= 10; i++) {
        if(i == 5) {
            break;  // exits loop when i = 5
        }
        printf("%d ", i);
    }

    printf("\n\nUsing continue:\n");
    for(i = 1; i <= 10; i++) {
        if(i == 5) {
            continue;  // skips printing 5
        }
        printf("%d ", i);
    }

    return 0;
}

print("Using break:")
for i in range(1, 11):
    if i == 5:
        break   # exits loop when i = 5
    print(i, end=" ")

print("\n\nUsing continue:")
for i in range(1, 11):
    if i == 5:
        continue   # skips printing 5
    print(i, end=" ")

    #include <stdio.h>

int main() {
    int n, i;
    unsigned long long fact = 1;  // factorial grows fast, so use long long

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if(n < 0) {
        printf("Factorial of negative numbers doesn't exist.\n");
    } else {
        for(i = 1; i <= n; i++) {
            fact *= i;
        }
        printf("Factorial of %d = %llu\n", n, fact);
    }

    return 0;
}

n = int(input("Enter a positive integer: "))

if n < 0:
    print("Factorial of negative numbers doesn't exist.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "=", fact)


    
    
int main() {
    float radius, area;

    printf("Enter radius of the circle: ");
    scanf("%f", &radius);

    area = PI * radius * radius;

    printf("Area of Circle = %.2f\n", area);

    return 0;
}


radius = float(input("Enter radius of the circle: "))

area = math.pi * radius * radius

print("Area of Circle =", area)

#include <stdio.h>

int main() {
    float side, perimeter;

    printf("Enter side of square: ");
    scanf("%f", &side);

    perimeter = 4 * side;
    printf("Perimeter of Square = %.2f\n", perimeter);

    return 0;
}

#include <stdio.h>

int main() {
    float length, width, perimeter;

    printf("Enter length: ");
    scanf("%f", &length);

    printf("Enter width: ");
    scanf("%f", &width);

    perimeter = 2 * (length + width);
    printf("Perimeter of Rectangle = %.2f\n", perimeter);

    return 0;
}

#include <stdio.h>

int main() {
    float a, b, c, perimeter;

    printf("Enter three sides of triangle: ");
    scanf("%f %f %f", &a, &b, &c);

    perimeter = a + b + c;
    printf("Perimeter of Triangle = %.2f\n", perimeter);

    return 0;
}

#include <stdio.h>

int main() {
    int choice;
    int totalamount = 0; 
    int paid = 1000;   
    

    printf("1. Cheese Pizza (Rs.120)\n");
    printf("2. Onion Pizza  (Rs.100)\n");
    printf("3. Chicken Pizza (Rs.220)\n");
    printf("4. Veggie Pizza (Rs.150)\n");

    
    do {
        printf("\nEnter your choice (1-5): ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("You chose Cheese Pizza: Rs.120\n");
                totalamount += 120;
                break;
            case 2:
                printf("You chose Onion Pizza: Rs.100\n");
                totalamount += 100;
                break;
            case 3:
                printf("You chose Chicken Pizza: Rs.220\n");
                totalamount += 220;
                break;
            case 4:
                printf("You chose Veggie Pizza: Rs.150\n");
                totalamount += 150;
                break;
            case 5: // Billing
                
                printf("Your total bill is: Rs.%d\n", totalamount);
                
                
                if(paid > totalamount) {
                    printf("Balance to return: Rs.%d\n", paid - totalamount);
                } else {
                    printf(" the money is not enough Rs.%d\n", totalamount - paid);
                }
                
                printf("THANKS, VISIT US AGAIN!\n");
                break;
            default:
                printf("Invalid choice! Please try again.\n");
        }

    } while(choice != 5);  

    return 0;
}

#include <stdio.h>
#include <stdbool.h>
int main() {
    bool isRaining = true;.
    bool isSunny = false;
    if (isRaining) {
    printf("Take an umbrella!\n");
    }
else {
    printf("Enjoy the sunshine!\n");
    return 0;
}

#include <stdio.h>

int main() {
    char name[5][50];
    char className[5][10];
    char section[5][5];
    char dob[5][15];   // New array for Date of Birth (format: DD/MM/YYYY)
    int rollNo[5];
    int age[5];
    int i, choice;

    for(i = 0; i < 5; i++) {
        printf("\nEnter details for Student %d:\n", i+1);

        printf("Name: ");
        scanf("%s", name[i]);

        printf("Class: ");
        scanf("%s", className[i]);

        printf("Section: ");
        scanf("%s", section[i]);

        printf("Roll Number: ");
        scanf("%d", &rollNo[i]);

        printf("Age: ");
        scanf("%d", &age[i]);

        printf("Date of Birth : ");
        scanf("%s", dob[i]);   
    }

    printf("\nEnter the student number (1-5) to display details: ");
    scanf("%d", &choice);

    if(choice >= 1 && choice <= 5) {
        printf("\n--- Details of Student %d ---\n", choice);
        printf("Name: %s\n", name[choice-1]);
        printf("Class: %s\n", className[choice-1]);
        printf("Section: %s\n", section[choice-1]);
        printf("Roll No: %d\n", rollNo[choice-1]);
        printf("Age: %d\n", age[choice-1]);
        printf("Date of Birth: %s\n", dob[choice-1]);  
    } else {
        printf("\nInvalid choice! Please enter a number between 1 and 5.\n");
    }

    return 0;
}

#include <stdio.h>

// Define a structure for Student
struct Student {
    char name[50];
    char className[10];
    char section[5];
    char dob[15];   // Date of Birth (format: DD/MM/YYYY)
    int rollNo;
    int age;
};

int main() {
    struct Student students[5];  // Array of 5 students
    int i, choice;

    // Input details for each student
    for(i = 0; i < 5; i++) {
        printf("\nEnter details for Student %d:\n", i+1);

        printf("Name: ");
        scanf("%s", students[i].name);

        printf("Class: ");
        scanf("%s", students[i].className);

        printf("Section: ");
        scanf("%s", students[i].section);

        printf("Roll Number: ");
        scanf("%d", &students[i].rollNo);

        printf("Age: ");
        scanf("%d", &students[i].age);

        printf("Date of Birth: ");
        scanf("%s", students[i].dob);
    }

    // Display details of a chosen student
    printf("\nEnter the student number (1-5) to display details: ");
    scanf("%d", &choice);

    if(choice >= 1 && choice <= 5) {
        printf("\n--- Details of Student %d ---\n", choice);
        printf("Name: %s\n", students[choice-1].name);
        printf("Class: %s\n", students[choice-1].className);
        printf("Section: %s\n", students[choice-1].section);
        printf("Roll No: %d\n", students[choice-1].rollNo);
        printf("Age: %d\n", students[choice-1].age);
        printf("Date of Birth: %s\n", students[choice-1].dob);
    } else {
        printf("\nInvalid choice! Please enter a number between 1 and 5.\n");
    }

    return 0;
}

#include <stdio.h>

struct student{
    int roll_no;
    int age;
    char class[3];
    char sec;
    char name[65];
    char dob[10];
};

int main() {
    struct student S1;
    char name[10][100];
    int n[1000];
    int i, choice;
    
    //1::get 10 student details
    for(i = 0; i < 10; i++) {
        printf(" Enter  the name\n " );
        scanf("%s", name[i]);
        n[i] = 100+i;
    }
    
    //2:: print 10 student details
     for(i=0; i <10;  i++){
        printf("%s\t",name[i]);
        printf("%d\t",n[i]);
     }
    
    //3::print specific student details
    printf(" \nenter the index which you want to see student name (1-10)");
    scanf("%d",&i);
    
    printf("\nStudent name::%s",name[i-1]);
    printf("\nStudent roll no::%d",n[i-1]);
 
   
   
   return 0;
  
    }
    
    
    