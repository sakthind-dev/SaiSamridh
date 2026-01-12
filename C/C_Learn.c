/*
 * File: C_Learn.c
 * Description: Demonstrates basic C concepts including structures, arrays, strings, and file handling.
 * Author: saijo
 * Date: 2024
 */
#include <stdio.h>
#include <stdlib.h>  // For malloc
#include <string.h>  // For strlen

// Added stdlib.h for malloc and string.h for strlen
#define SIZE 3  // Number of students

// Define a structure for student
struct Student {
    int roll;
    int age;
    char name[30];
};

/*
 * The Student structure holds information about a student,
 * including roll number, age, and name.
 */
int main() {
    char s1 ='s'; //what is this -character datatype - store 1 byte or 1 char
    char sname[11] = "saisamridh"; //? character array or string datatype - store 5 byte or 5 char
    int a[10] = {1, 2,3,4,5,6,7,8,9,10};
    float b[10] = {9.0, 8.0,o 7.0, 8.0, 9.0,9.1, 9.2};
    struct Student s[SIZE]; //? explain
    char *sname1;
    int i;
    //FILE
    //FILE *fptr;
    //filename = "C://name/kri.csv"
    //fptr = fopen(filename, "w");
    //fptr = fopen("C:\\directoryname\\filename.txt", "w");

    
    sname1 = malloc(sizeof(char)*11);
    if (sname1 == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }
    printf("%c %x\n", s1, &s1);
    printf("%s %x %d\n", sname, &sname, sizeof(sname));
   
    // Demonstrate structure usage and memory addresses
    // s[0].name is an empty string initially
    // &s gives the address of the first element of the array of structures
     printf("%s %x\n", s[0].name, &s);

    // Prints the string 'sname1', its memory address in hexadecimal, and its length.
    // Format: <string> <address_in_hex> <length>
    // Parameters:
    //   sname1 - a null-terminated string to be printed and analyzed.
     printf("%s %x %d\n", sname1, &sname1, strlen(sname1));

    // Input student details  
    for (int i = 0; i < SIZE; i++) {
        printf("Enter name, age, and roll number for student %d:\n", i + 1);
        scanf("%29s %d %d", s[i].name, &s[i].age, &s[i].roll);
    }

    printf("\n--- Student Details ---\n");
    for (int i = 0; i < SIZE; i++) {
        printf("Name: %s, Age: %d, Roll No: %d\n", s[i].name, s[i].age, s[i].roll);
    }

    // File handling with error checking
    FILE *fptr, *fptr1;
    char filename[] = "students.txt";
    char filename1[] = "students.csv";
    
    // Open file for writing
    fptr = fopen(filename, "a");
    if (fptr == NULL) {
        printf("Error opening file %s\n", filename);
        return 1;
    }
    fptr1 = fopen(filename1, "a");
    if (fptr1 == NULL) {
        printf("Error opening file %s\n", filename1);
        fclose(fptr); // Close previously opened file
        return 1;
    }
#if 0
    // Write student details to file
    fprintf(fptr, "Student Details:\n");
    fprintf(fptr, "----------------\n");
    for (int i = 0; i < SIZE; i++) {
        fprintf(fptr, "Student %d:\n", i + 1);
        fprintf(fptr, "Name: %s\n", s[i].name);
        fprintf(fptr, "Age: %d\n", s[i].age);
        fprintf(fptr, "Roll No: %d\n", s[i].roll);
        fprintf(fptr, "----------------\n");
    }
#endif
      // Write student details to file
    fprintf(fptr, "Student Details:\n");
    fprintf(fptr, "----------------\n");
    fprintf(fptr, "Student\tName\tAge\tRoll No\n");
    fprintf(fptr, "----------------\n");
    for (int i = 0; i < SIZE; i++) {
        fprintf(fptr, "%d\t%s\t%d\t%d\n", i + 1, s[i].name, s[i].age, s[i].roll);
        fprintf(fptr, "----------------\n");
    }
  
       // Write student details to file
    //fprintf(fptr1, "----------------\n");
    //fprintf(fptr1, "Student\tName\tAge\tRoll No\n");
    //fprintf(fptr1, "----------------\n");
    i = ftell(fptr1);
    if (i ==0L) {
        fprintf(fptr1, "Student,Name,Age,Roll No\n");
        //fprintf(fptr1, "tName\tAge\tRoll No\n");
        //fclose(fptr);
        //fclose(fptr1);
        //return 1;
    }
    if (i ==-1L) {
        printf("Error getting file position in %s\n", filename1);
        fclose(fptr);
        fclose(fptr1);
        return 1;
    }

    for (int i = 0; i < SIZE; i++) {
        fprintf(fptr1, "%d,%s,%d,%d\n", i + 1, s[i].name, s[i].age, s[i].roll);
        //fprintf(fptr1, "----------------\n");
    }
    // Close file with error checking
    if (fclose(fptr) != 0) {
        printf("Error closing file %s\n", filename);
        return 1;
    }

    
    // Close file with error checking
    if (fclose(fptr1) != 0) {
        printf("Error closing file %s\n", filename1);
        return 1;
    }
    printf("Student details have been written to %s\n", filename1);

    return 0;
}