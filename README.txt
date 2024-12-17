Installation Steps:
-----------------
1. Install Python:

2. Install PLY:

Running the Program:
------------------
1. File Structure:
   - lexer.py 
   - input.txt (test cases)

2. Command Line Execution:
   a) Open command prompt
   b) Navigate to the program directory
   c) Run the program:
    python lexer.py input.txt shadowSparks.tok

3. Output:
   - The program will generate output.tok file
   - Each line in output.tok contains tokenized version of input
   - Format: value/type (e.g., "23/INT +/+ 8/INT")

Test Input Example:
-----------------
Input (input.txt):
23+8
2.5 * 0
5NUM^ 3.0
x=5

Expected Output (output.tok):
23/INT +/+ 8/INT
2.5/REAL */* 0/INT
5/INT NUM/VAR ^/POW 3.0/REAL
x/VAR =/= 5/INT
