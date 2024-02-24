# Fibonacci Numbers using Python loops and Recursion

# Algorithm for generating Fabonacci Number till nth number

    # 1.Start with the two first Fibonacci numbers 0 and 1.
    # 2.Add the two previous numbers together to create a new Fibonacci number.
    # 3.Update the value of the two previous numbers.
    # 4.Do point a and b above 18 times.

# Fibonacci Numbers using Python for loop
fibonacci_sequence = []
num1 = 0
num2 = 1
for i in range(10):
    num3 = num1 + num2
    fibonacci_sequence.append(num3)
    num1 = num2
    num2 = num3
print(fibonacci_sequence)
    
# Fibonacci Numbers using Python Functions Recursion

counter = 1
fibonacci_sequence = []
def fiboNumGen(num1, num2):
    global counter
    global fibonacci_sequence
    if counter <= 10:
        num3 = num1 + num2
        fibonacci_sequence.append(num3)
        num2 = num1
        num1 = num3
        counter += 1
        fiboNumGen(num1, num2)
    else:
         print(fibonacci_sequence)

fiboNumGen(1,0)

# Finding the Nth Fabonacci number by F(n) = F(n-1) + F(n-2):
    # This formula uses a 0-based index. This means that to generate the 10th Fibonacci number, we must write 11.
def FindFaboNum(number):
    if number <= 1:
        return number
    else:
        return FindFaboNum(number - 1) + FindFaboNum(number - 2)
    
print(FindFaboNum(11))