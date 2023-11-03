# Pac-Man Search
## Authors: Zergio, Tyler, Michael

## Our Progress:

> This week we implemented 4 search algorithms (DFS, BFS, UCS, and A*) in Python using the pseudocode available in the books. Translating the pseudocode to Python was not particularly difficult. We found that most of our time was spent experimenting with and understanding the structure of the starter code.

## Question 1: Depth First Search

**The Pacman board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). Is the exploration order what you would have expected? Does Pacman actually go to all the explored squares on his way to the goal?**

> Yes, the order is what we expected because it expands to states that lead to a dead-end. The DFS algorithm continues exploring a path until it can’t anymore. However, Pacman does not traverse all squares explored by the DFS algorithm. This is because Pacman takes the shortest path to the goal state (food) and avoids exploring a path that leads to a dead-end.

**Screenshots:**

Q1.1:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q1.1.png" width="450">

Q1.2:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q1.2.png" width="450">

Q1.3:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q1.3.png" width="450">

Autograder Q1:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q1.autograder.png" width="450">

## Question 2: Breadth-First Search

**Screenshots:**

Q2.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q2.1.png" width="450">

Q2.2

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q2.2.png" width="450">

Q2 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q2.autograder.png" width="450">

## Question 3: Uniform Cost Search

**Screenshots:**

Q3.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.1.png" width="450">

Q3.2

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.2.png" width="450">

Q3.3

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.3.png" width="450">

Q3 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.autograder.png" width="450">

## Question 4: A* Search

**Screenshots:**

Q4.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q4.1.png" width="450">

Q4 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q4.Autograder.png" width="450">
