#include <stdio.h>
#include <string.h>

// Function Declarations
void greet(char name[]);  // Function to greet a person
int add(int a, int b);    // Function to add two numbers
int factorial(int n);     // Function to calculate factorial

int main() {
    // 1. Variable Declaration and Assignment
    char name[] = "Alice";    // String assignment
    int age = 25;             // Integer assignment
    float height = 5.7;       // Float assignment
    int is_student = 1;       // Boolean-like assignment (1 is true)

    // 2. Printing to Console
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    printf("Height: %.2f\n", height);
    printf("Is Student: %d\n", is_student);

    // 3. Conditionals (If-Else Statements)
    if (age < 18) {
        printf("%s is a minor.\n", name);
    } else if (age >= 18 && age <= 60) {
        printf("%s is an adult.\n", name);
    } else {
        printf("%s is a senior citizen.\n", name);
    }

    // 4. Basic Math Operations
    int sum = 10 + 5;
    int diff = 10 - 5;
    int prod = 10 * 5;
    float quot = 10.0 / 5.0;  // To demonstrate floating point division
    int mod = 10 % 3;

    printf("\nMath Operations:\n");
    printf("Sum: %d\n", sum);
    printf("Difference: %d\n", diff);
    printf("Product: %d\n", prod);
    printf("Quotient: %.2f\n", quot);
    printf("Modulus: %d\n", mod);

    // 5. Loops: For Loop
    printf("\nFor Loop - Numbers from 1 to 5:\n");
    for (int i = 1; i <= 5; i++) {
        printf("%d\n", i);
    }

    // 6. Loops: While Loop
    printf("\nWhile Loop - Numbers from 1 to 5:\n");
    int i = 1;
    while (i <= 5) {
        printf("%d\n", i);
        i++;
    }

    // 7. Functions
    greet(name);  // Function call to greet
    int result = add(3, 4);  // Function call to add two numbers
    printf("\nSum of 3 and 4: %d\n", result);

    int fact = factorial(5);  // Function call to calculate factorial
    printf("Factorial of 5: %d\n", fact);

    // 8. Arrays
    int numbers[] = {1, 2, 3, 4, 5};
    int array_size = sizeof(numbers) / sizeof(numbers[0]);
    
    printf("\nArray Elements:\n");
    for (int i = 0; i < array_size; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    // 9. String Manipulation
    char greeting[] = "Hello, World!";
    printf("\nOriginal String: %s\n", greeting);

    // String comparison
    if (strcmp(name, "Alice") == 0) {
        printf("Name is Alice.\n");
    } else {
        printf("Name is not Alice.\n");
    }

    // 10. Input from User
    int user_input;
    printf("\nEnter a number to calculate its square: ");
    scanf("%d", &user_input);
    printf("Square of %d is %d\n", user_input, user_input * user_input);

    return 0;
}

// 11. Function Definitions
void greet(char name[]) {
    printf("\nHello, %s! Welcome to the C programming world.\n", name);
}

int add(int a, int b) {
    return a + b;
}

int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factorial(n - 1);  // Recursive factorial calculation
}
