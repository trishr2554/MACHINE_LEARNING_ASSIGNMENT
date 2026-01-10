
def vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count = v_count + 1
            else:
                c_count += 1
    return v_count,c_count

#main program    
string = input("Enter a String: ")
vowels, consonants = vowels_consonants(string)

print("Number of vowels: ", vowels)
print("Number of consonants:", consonants)"""

def count_common_elements(list1, list2):
    common = set(list1) & set(list2)
    return len(common)

# Main program
list1 = [18 , 29, 36, 4, 5, 13]
list2 = [36, 4, 18, 6, 7, 29 , 4]

result = count_common_elements(list1, list2)
print("Number of common elements:", result)"""

import random
import statistics

def calculate():
    numbers = []

    for i in range(100):
        numbers.append(random.randint(100, 150))

    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    mode = statistics.mode(numbers)

    return numbers, mean, median, mode


#Main Program
nums, mean_val, median_val, mode_val = calculate()

print("Numbers generated between 100 and 150: ")
print(nums)

print("\nMean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)

# Get matrix size
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

# Read matrix
matrix = []
print("Enter the matrix elements:")

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    matrix.append(row)

# Transpose
print("Transpose of the matrix:")

for j in range(c):
    for i in range(r):
        print(matrix[i][j], end=" ")
    print()

def multiply_matrices():
    r1 = int(input("Enter number of rows of A: "))
    c1 = int(input("Enter number of columns of A: "))

    A = []
    print("Enter matrix A row-wise:")
    for i in range(r1):
        row = input().split()
        if len(row) != c1:
            return None
        nums = []
        for v in row:
            nums.append(int(v))
        A.append(nums)

    r2 = int(input("Enter number of rows of B: "))
    c2 = int(input("Enter number of columns of B: "))

    B = []
    print("Enter matrix B row-wise:")
    for i in range(r2):
        row = input().split()
        if len(row) != c2:
            return None
        nums = []
        for v in row:
            nums.append(int(v))
        B.append(nums)

    if c1 != r2:
        return None

    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result


#Main Program 
product = multiply_matrices()

if product is None:
    print("Error: Invalid matrix size or input")
else:
    print("Product Matrix (AB):")
    for r in product:
        print(r)













        
                
    
