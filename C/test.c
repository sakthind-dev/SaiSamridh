#include<stdio.h>
int main() {
    int num1, num2, product;

    printf("Enter the first number: ");
    scanf("%d", &num1);

    printf("Enter the second number: ");
    scanf("%d", &num2);

    product = num1 * num2;

    printf("The product of %d and %d is: %d\n", num1, num2, product);
    for (int i = 10; i > 0; i--) {
        printf("\n*^*");
        for (int j = 0; j <= i; j++) {
            printf("*");
        }
    }
    for (int i=0;i<100;i++){
        sound(i);
    }
for (int i=1000;i>0;i--){
        sound(i);
    }

    return 0;
}
