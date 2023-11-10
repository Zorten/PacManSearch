# Pac-Man Search
## Authors: Zergio, Tyler, Michael

## Phase I

### Our Progress:

> This week we implemented 4 search algorithms (DFS, BFS, UCS, and A*) in Python using the pseudocode available in the books. Translating the pseudocode to Python was not particularly difficult. We found that most of our time was spent experimenting with and understanding the structure of the starter code.

### Question 1: Depth First Search

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

### Question 2: Breadth-First Search

**Screenshots:**

Q2.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q2.1.png" width="450">

Q2.2

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q2.2.png" width="450">

Q2 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q2.autograder.png" width="450">

### Question 3: Uniform Cost Search

**Screenshots:**

Q3.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.1.png" width="450">

Q3.2

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.2.png" width="450">

Q3.3

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.3.png" width="450">

Q3 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q3.autograder.png" width="450">

### Question 4: A* Search

**Screenshots:**

Q4.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q4.1.png" width="450">

Q4 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q4.Autograder.png" width="450">


## Phase II

### Our Progress:

> This week we completed questions five and six which required us to implement the four corners problem, and a heuristic to accelerate A* search. 

### Question 5: Finding All the Corners

**Screenshots:**

Q5.1:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q5.1.png" width="450">

Q5.2:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q5.2.png" width="450">


Autograder Q5:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q5.autograder.png" width="450">

### Question 6: Corners Problem: Heuristic

**Screenshots:**

Q6.1

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q6.1.png" width="450">


Q6 Autograder

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q6.autograder.png" width="450">

Q6 Heuristic Formulation

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q6.heuristic.png" width="450">

> The heuristic is consistent because at any time step, we can move in  north, south, east, or west by exactly one unit for cost 1. Therefore, at each step, our path cost increases by 1, but what about the heuristic? Because our heuristic relies on the minimum distance between the current position and any corner, it can decrease by at most one per move. Therefore, the heuristic is consistent.

> Because every consistent heuristic is admissible, this implies that our heuristic is also admissible.

