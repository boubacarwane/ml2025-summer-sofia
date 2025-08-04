
# Step 1: Ask the user for input N (a positive integer)
N = int(input("Enter a positive integer N: "))

# Step 2: Read N numbers one by one and store in a list
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 3: Ask for input X
X = int(input("Enter the number X to search for: "))

# Step 4: Search for X in the list
if X in numbers:
    # Output the index (1-based)
    print(numbers.index(X) + 1)
else:
    print(-1)
