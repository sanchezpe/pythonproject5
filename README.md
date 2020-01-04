# Programming Assignment #5

## Description
Type a brief description of the program.

## Instructions
Write a program to process a file ("pa5.data") of quarterback passer rating data. There is data for 20 quarterbacks in the file. The file contains data in the following order: quarterback name, team name, pass attempts, pass completions, passing yards, passing touchdowns, and interceptions. Numeric items will be on the same line (see sample data).

The passer rating is computed as follows. There are 4 intermediate results that must be computed.

a = (completions / attempts * 100 – 30) * 0.05
b = (yards / attempts – 3) * 0.25
c = touchdowns / attempts * 20
d = 2.375 – interceptions / attempts * 25

Next, you must make adjustments for results less than zero and results greater than 2.375. If any intermediate result is less than zero, you must change it to zero, and if any intermediate result is greater than 2.375, you must change it to 2.375.

This makes the maximum possible NFL quarterback rating 158.3. Aren't you glad you know this?!

Once you have computed these intermediate results, and adjusted them properly if necessary, the final passer rating is computed using the following calculation:

rating = (a + b + c + d) / 6 * 100

Your program should open the file and read in exactly 20 quarterbacks. You may use either a while loop or a for loop to process through the file of data. After reading in data for a quarterback, compute the passer rating for that player (making the necessary adjustment of intermediate values that are negative or greater than 2.375), print a line of output for that player before the loop begins its next repetition.

## Sample Run
	Quarterback Name Team Name Passer Rating
	----------------------------------------------------
	Drew Brees New Orleans 109.6
	Phillip Rivers San Diego 104.4
	Aaron Rodgers Green Bay 103.2
	Ben Roethlisberger Pittsburgh 100.5
	…………………………
	…………………………