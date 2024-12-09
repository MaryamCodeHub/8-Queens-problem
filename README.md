8-Queens Problem Solver


This Python program solves the 8-Queens problem, a classic puzzle in which 8 queens must be placed on an 8x8 chessboard such that no two queens attack each other. The program not only places the queens on the board but also calculates how many pairs of queens are attacking each other, based on their positions.

Problem Explanation:
In chess, queens can attack each other in the following ways:

Same Column: If two queens share the same column, they can attack each other.
Same Diagonal: Queens can also attack each other if they share the same diagonal. There are two types of diagonals:
Descending Diagonal: The row and column positions of two queens have the same difference.
Ascending Diagonal: The sum of their row and column positions is the same.
The objective of the 8-Queens problem is to arrange the 8 queens on the board such that no two queens can attack each other.

Features:
Chessboard Representation: The chessboard is represented using a list, where each index corresponds to a row, and the value at each index represents the column where a queen is placed in that row.
Attack Detection: The program checks every pair of queens to determine if they are attacking each other. It checks for attacks in the same column and both types of diagonals.
Board Visualization: The chessboard is printed with 'Q' for queens and '.' for empty spaces, providing a visual representation of the queens' positions.
Attack Pair Counting: After checking all possible queen pairs, the program calculates and displays the total number of attacking pairs. It also shows the positions of each attacking pair.
Logic:
Queen Positioning: The queens are placed such that each queen is in a different row. The list queen_positions[i] holds the column index for the queen in row i.
Attack Calculation: The program uses two nested loops to compare each queen with every other queen. It checks if they are in the same column or diagonal:
Column Attack: If queen_positions[i] == queen_positions[j], they are in the same column.
Diagonal Attack: If abs(queen_positions[i] - queen_positions[j]) == abs(i - j), they are on the same diagonal.
Display: The program displays the chessboard and the total number of attacking pairs, along with the positions of the attacking queens.

Example Output:

Chessboard:
Q . . . . . . .
. . Q . . . . .
. . . . Q . . .
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . . . . . . Q
. . . . . . Q .

Total attacking pairs: 4

Attacking pairs (row, column):
Queen in Row 1, Column 1 attacks Queen in Row 6, Column 6
Queen in Row 2, Column 3 attacks Queen in Row 7, Column 8
Queen in Row 5, Column 4 attacks Queen in Row 8, Column 7
Queen in Row 7, Column 8 attacks Queen in Row 8, Column 7


The chessboard will be displayed with the queens' positions.
The program will output the total number of attacking pairs and their respective positions on the board.
How It Works:
The program represents the board as a list where each index holds the column position of the queen in that row.
It checks all pairs of queens to find out if they are attacking each other using simple conditions based on their row, column, and diagonal positions.
The program then outputs the total number of attacking pairs and their positions.

Conclusion:
This program demonstrates a simple yet effective solution to the 8-Queens problem by utilizing basic list indexing and loops. The logic checks all possible queen pairs for attacks based on column and diagonal positions, making it a useful tool for understanding optimization and constraint-based problems.
