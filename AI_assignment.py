# Function to display the chessboard
def display_chessboard(queen_positions):
    n = len(queen_positions)
    print("\nChessboard:")
    for i in range(n):
        row = ["Q" if j == queen_positions[i] else "." for j in range(n)]
        print(" ".join(row))

# Function to calculate attacking pairs of queens
def calculate_attacking_pairs(queen_positions):
    n = len(queen_positions)
    attacks = 0
    attacking_pairs = []  # List to store attacking pairs
    for i in range(n):
        for j in range(i + 1, n):
            # Check for same column or diagonal attacks
            if queen_positions[i] == queen_positions[j] or abs(queen_positions[i] - queen_positions[j]) == abs(i - j):
                attacks += 1
                attacking_pairs.append((i + 1, queen_positions[i] + 1, j + 1, queen_positions[j] + 1))  # Storing 1-based indices
    return attacks, attacking_pairs

# Example placement of queens (one in each row)
queen_positions = [0, 2, 4, 1, 3, 5, 7, 6]

# Display the chessboard
display_chessboard(queen_positions)

# Calculate and display the total number of attacking pairs
attacking_pairs, pairs = calculate_attacking_pairs(queen_positions)
print(f"\nTotal attacking pairs: {attacking_pairs}")

# Display the attacking pairs
if attacking_pairs > 0:
    print("\nAttacking pairs (row, column):")
    for pair in pairs:
        print(f"Queen in Row {pair[0]}, Column {pair[1]} attacks Queen in Row {pair[2]}, Column {pair[3]}")
