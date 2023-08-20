# Taking input for the number of rows
n = int(input("Number of rows: "))

k = 0  # Initialize a variable to store cumulative increment
for i in range(n):
    k += i  # Increment k by the current value of i (0 to n-1)

m = n + k  # Calculate the initial value of m based on n and cumulative increment k

# Loop to print the pattern
for i in range(n):
    for j in range(i + 1):
        # Print the current value of m with a width of 5 characters, left-aligned
        print(format(m, "<5"), end=" ")
        m -= 1  # Decrement m for the next iteration
        
    print()  # Print a newline after each row of the pattern
