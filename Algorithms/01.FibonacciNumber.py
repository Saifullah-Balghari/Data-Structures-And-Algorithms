# Algorithms: Is the step by step solution to any problem.

# Algorithm for generating Fabonacci Numbers using for Loops.

    # STEP 1: Start.
    # STEP 2: Initialize an empty list "fibonacci_numbers" to store Fibonacci numbers.
    # STEP 3: Initialize variables "num1" and "num2" to 0 and 1, respectively, to represent the first two Fibonacci numbers.
    # STEP 4: Use a for loop to iterate 10 times (from 0 to 9).
    # STEP 5: Inside the loop:
        # a. Calculate the next Fibonacci number "num3" by adding "num1" and "num2".
        # b. Append "num3" to the "fibonacci_numbers" list.
        # c. Update "num1" to the value of "num2".
        # d. Update "num2" to the value of "num3".
    # STEP 6: After the loop, print the "fibonacci_numbers".
    # STEP 7: Stop.

# Code

fibonacci_numbers = []
num1 = 0
num2 = 1
for i in range(10):
    num3 = num1 + num2
    fibonacci_numbers.append(num3)
    num1 = num2
    num2 = num3
print(fibonacci_numbers)    # Output: [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
# Algorithm for generating Fabonacci Numbers using Functions Recursion.

    # STEP 1: Start.
    # STEP 2: Initialize "counter" to 1 and "fibonacci_numbers" as an empty list.
    # STEP 3: Define a function fiboNumGen with parameters "num1" and "num2".
    # STEP 4: Check if "counter" is less than or equal to 10.
    # STEP 5: If true, do the following:
        # a. Calculate the next Fibonacci number "num3" by adding "num1" and "num2".
        # b. Append "num3" to the "fibonacci_numbers" list.
        # c. Update "num2" to the value of "num1" and "num1" to the value of "num3".
        # d. Increment "counter" by 1.
        # e. Call fiboNumGen recursively with updated "num1" and "num2".
    # STEP 6: If "counter" exceeds 10, print the list "fibonacci_numbers".
    # STEP 7: End.

# Code

counter = 1
fibonacci_numbers = []
def fiboNumGen(num1, num2):
    global counter
    global fibonacci_numbers
    if counter <= 10:
        num3 = num1 + num2
        fibonacci_numbers.append(num3)
        num2 = num1
        num1 = num3
        counter += 1
        fiboNumGen(num1, num2)
    else:
         print(fibonacci_numbers)

fiboNumGen(1,0)     # Output: [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Finding the Nth Fabonacci number by F(n) = F(n-1) + F(n-2):
# This formula uses a 0-based index. This means that to generate the Nth Fibonacci number, we must give a value lower then that.

def FindFaboNum(number):
    if number <= 1:
        return number
    else:
        return FindFaboNum(number - 1) + FindFaboNum(number - 2)
    
print(FindFaboNum(9))          # Output: 34