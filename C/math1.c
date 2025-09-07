/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>
#include <math.h>

// 1. Basic Math
int basic_math_main() ;
int math_main() ;

// 2. Sum
int sum_main() ;

// 3. Multiplication Table
int table_of_multiplication() ;
int mul_main() ;

// 4. Division
int div_main() ;
int div1_main() ;
int div2_main() ;
int div3_main() ;
int div4_main() ;
int table_of_division() ;

// 5. Product
int product_main() ;
int product1_main() ;
int product2_main() ;

// 6. Decimal
int decimal_main() ;
int decimal2_main() ;

// 7. Power
int power_main() ;

// 8. Name
int name_main() ;
int name1_main() ;
int name3_main() ;

// 9. Sound
int sound(int i) ;
int sound_main() ;

int main() {
    // Call functions in logical order
    basic_math_main();
    sum_main();
    table_of_multiplication();
    mul_main();
    div_main();
    div1_main();
    div2_main();
    div3_main();
    div4_main();
    table_of_division();
    product_main();
    product1_main();
    product2_main();
    decimal_main();
    decimal2_main();
    power_main();
    name_main();
    name1_main();
    name3_main();
    sound_main();
    return 0;
}
int basic_math_main()
{

    int num1,num2,num3 ,num4;
 printf("Enter the first no");
 scanf("%d",&num1);
 printf("\n Enter the second no");
 scanf("%d",&num2);
 printf("\n Enter the third no");
 scanf("%d", &num3);
 
 num4=num1+num2+num3;
    printf("\n addition of 3   numbers:%d",num4 );

 num4=num1-num2-num3;
    printf("\n subtraction of 3   numbers:%d",num4 );
 
 num4=num1*num2*num3;
    printf("\n multiplication of 3   numbers:%d",num4 );
    
 num4=num1+num2/num3;
    printf("\n division of 3   numbers:%d",num4 );
    num4=(num1+num2+num3)/3;
    printf("\n average of 3  numbers and divide by 3 :%d",num4 );

     return 0;
}

int table_of_multiplication() {
  int n;
  printf("Enter an integer: ");
  scanf("%d", &n);

  for (int i = 1; i <= 10; ++i) {
    printf("%d * %d = %d \n", n, i, n * i);
  }
  return 0;
}

int sum_main() {    

    int number1, number2, sum;
    
    printf("Enter two integers: ");
    scanf("%d %d", &number1, &number2);

    // calculate the sum
    sum = number1 + number2;      
    
    printf("%d + %d = %d", number1, number2, sum);
    return 0;
}

int div_main() {
    int dividend, divisor, quotient, remainder;

    printf("Enter dividend: ");
    scanf("%d", &dividend);

    printf("Enter divisor: ");
    scanf("%d", &divisor);


    if (dividend == 0 || divisor == 0) {
        printf("Error: Dividend or divisor cannot be zero.\n");
    } else {
        
        quotient = dividend / divisor;

        
        remainder = dividend % divisor;

        printf("Quotient = %d\n", quotient);
        printf("Remainder = %d\n", remainder);
    }

    return 0;
}

int avg_main()
{
 int num1,num2,num3 ,num4;
 printf("Enter the first no");
 scanf("%d",&num1);
 printf("\n Enter the second no");
 scanf("%d",&num2);
 printf("\n Enter the third no");
 scanf("%d", &num3);

 printf("\n division of 3   numbers:%d",num4 );
    num4=(num1+num2+num3)/3;
    printf("\n average of 3  numbers and divide by 3 :%d",num4 );
 


    return 0;
}

int table_of_division() {
    int i;
    float result;

    printf("Division Table of 8:\n");
    printf("-------------------\n");

    for (i = 1; i <= 10; i++) {
        result = (float)8 / i;
        printf("8 / %d = %.2f\n", i, result);
    }

    return 0;
}

int div1_main() {
  int dividend, divisor;
  float quotient;

  printf("Enter dividend: ");
  scanf("%d", &dividend);

  printf("Enter divisor: ");
  scanf("%d", &divisor);

  if (divisor == 0) {
    printf("Error: Division by zero is not allowed.\n");
    return 1;
  }

  quotient = (float)dividend / divisor;
  printf("Quotient: %.2f\n", quotient);

  return 0;
}

int product_main() {
    int num1, num2, product;

    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    product = num1 * num2;

    printf("The product of %d and %d is: %d\n", num1, num2, product);

    return 0;
}

int product1_main() {
    int num1, num2, product;

    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    product = num1 * num2;

    printf("The product of %d and %d is: %d\n", num1, num2, product);

    return 0;
}

int product2_main()
{
    int num1, num2, product;

    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    product = num1 * num2;

    printf("The product of %d and %d is: %d\n", num1, num2, product);

    return 0;
}

 int mul_main() {
    int i;

    printf("Multiplication Table of 5:\n");
    for (i = 1; i <= 10; i++) {
        printf("5 x %d = %d\n", i, 5 * i);
    }

    printf("\nMultiplication Table of 7:\n");
    for (i = 1; i <= 10; i++) {
        printf("7 x %d = %d\n", i, 7 * i);
    }

    return 0;

}

int div2_main() {
    float num1, num2;

    printf("Enter the first number: ");
    scanf("%f", &num1);

    printf("Enter the second number: ");
    scanf("%f", &num2);

    if (num2 == 0) {
        printf("Cannot divide by zero.\n");
    } else {
        float result = num1 / num2;
        printf("The result of the division is: %.2f\n", result);
    }

    return 0;
}

int div3_main() {
    float num1, num2;

    printf("Enter the first number: ");
    scanf("%f", &num1);

    printf("Enter the second number: ");
    scanf("%f", &num2);

    if (num2 == 0) {
        printf("Cannot divide by zero.\n");

    } else {
        float result = num1 / num2;
        printf("The result of the division is: %.2f\n", result);
    }

    return 0;
}

int power_main() {
    int base = 2; // The base number is always 2
    int exponent; // The power to which 2 is raised

    printf("Enter the exponent: ");
    scanf("%d", &exponent);

    // Calculate the power of 2
    double result = pow(base, exponent);

    printf("2^%d = %.0lf\n", exponent, result);

    return 0;
}

int sound(int i) {
    // Placeholder function for sound functionality
    // In a real implementation, this could play a sound or beep
    printf("Sound %d\n", i);
    return 0;
}
int sound_main() {
    for (int i = 0; i < 100; i++) {
        sound(i);
    }
    
    for (int i = 1000; i > 0; i--) {
        sound(i);
    }

    return 0;
}

int div4_main() {
    float num1, num2;

    printf("Enter the first number: ");
    scanf("%f", &num1);

    printf("Enter the second number: ");
    scanf("%f", &num2);

    if (num2 == 0) {
        printf("Cannot divide by zero.\n");
    } else {
        float result = num1 / num2;
        printf("The result of the division is: %.2f\n", result);
    }

    return 0;
}

#include <math.h> // Include for pow() function
/*
int power_main() {
    int base = 2; // The base number is always 2
    int exponent; // The power to which 2 is raised

    printf("Enter the exponent: ");
    scanf("%d", &exponent);

    // Calculate the power of 2
    double result = pow(base, exponent);

    printf("2^%d = %.0lf\n", exponent, result);

    return 0;
}
*/
/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
int math_main()
{
 int num1,num2,num3 ,num4;
 printf("Enter the first no");
 scanf("%d",&num1);
 printf("\n Enter the second no");

 scanf("%d",&num2);
 printf("\n Enter the third no");
 scanf("%d", &num3);
 
 num4=num1+num2+num3;
    printf("\n addition of 3   numbers:%d",num4 );


 num4=num1-num2-num3;
    printf("\n subtraction of 3   numbers:%d",num4 );
    


 num4=num1*num2*num3;
    printf("\n multiplication of 3   numbers:%d",num4 );
    
 num4=num1+num2/num3;
    printf("\n division of 3   numbers:%d",num4 );
    num4=(num1+num2+num3)/3;
    printf("\n average of 3  numbers and divide by 3 :%d",num4 );
 

for(int i=10;i>0;i--){
    printf("\n*^*");
    for(int j=0;j<=i;j++){
        printf("*");
    }
}

for(int i=0;i<5;i++){
    printf("\n**");
    for(int j=0;j<=i;j++){
        printf("\t*SAI*");
        printf("\t*JOSHINI*");
    }
    
}
    return 0;
}

int name_main()
{
    char myname[10] = "saisamridh";
    printf("%s","myname is",myname);
    
    return 0;
}

int name1_main()
{
    char myname[10] = "saisamridh";
    printf(" my name is %s",  myname);

    return 0;
}


int decimal_main() 
{
    
    float number1, number2, sum;

    
    printf("Enter the first decimal number: ");
    scanf("%f", &number1);

    printf("Enter the second decimal number: ");
    scanf("%f", &number2);

    
    sum = number1 + number2;

    
    printf("The sum is: %.2f\n", sum);

    return 0;
}


int decimal2_main() {
    
    double number1, number2, sum;

    
    printf("Enter the first decimal number: ");
    scanf("%lf", &number1);

    printf("Enter the second decimal number: ");
    scanf("%lf", &number2);

    
    sum = number1 + number2;

    
    printf("The sum is: %.2lf\n", sum);

    return 0;
}

int name3_main() {
    
    char name[] = {'Y', 'o', 'u', 'r', 'N', 'a', 'm', 'e', '\0'};

    printf("Your name is: %s\n", name);

    return 0;
}
/*
// Python equivalent for multiplication table
# This code generates a multiplication table for the number 8
num = 8

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}"
    )
*/

/*
//python equivalent for division table
# This code generates a division table for the number 8
num = 8

for i in range(1, 11):
    result = num / i
    print(f"{num} ÷ {i} = {result:.2f}")
*/

/*
//Python equivalent for creative names of number 8
  # Five creative names of number 8
names = ["Infinity", "Octopus", "sai", "Eightball", "Eighth Wonder"]

for name in names:
    print(name)
*/

/*
//Python equivalent for multiplication of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = num1 * num2

print(f"{num1} × {num2} = {result}")
*/

/*
//Python equivalent for division of two numbers
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Check for division by zero
if num2 != 0:
    result = num1 / num2
    print(f"{num1} ÷ {num2} = {result:.2f}")
else:
    print("Error: Division by zero is not allowed.")
*/

/**
// Python equivalent for checking if a number is prime
int main()
 import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    
    return 0;
 */

/*
// Python equivalent for checking if a number is greater than another
a = 7
b = 5

if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(b, "is greater than", a)
else:
    print(a, "and", b, "are equal")
*/


/*
// Python equivalent for printing a name
Sure! Let’s explore a few easy and fun Python programs for kids—especially useful for a 12-year-old starting out with numbers, characters, and logic. Each program is short, beginner-friendly, and teaches a cool concept:

🧮 1. Multiplication Table of Any Number
number = int(input("Enter a number: "))
print(f"Multiplication table of {number}")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

sum = 0
for i in range(1, 11):
    sum += i
print("Sum of numbers from 1 to 10 is:", sum)
*/


/*
//Python equivalent for division of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num2 == 0:
    print("Cannot divide by zero.")
else:
    
    result = num1 / num2
    
    print("The result of the division is:", result)
*/ 

/*
//Python equivalent for division of two numbers
int main(num1,num2,num3)
{
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


product = num1 * num2
print("The product is:", product)


if num2 == 0:
    print("Cannot divide by zero.")
else:
    quotient = num1 / num2
    print("The quotient is:", quotient)

return 0;
}

i = 1
while i <= 10:
    print(i)
    i += 1 

import operator

num1 = 15
num2 = 8
difference = operator.sub(num1, num2)
print("The difference is:", difference)
*/

/*
//Python equivalent for subtraction of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 - num2
print(" The sum is:", sum)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
print(" The sum is:", sum)
*/

