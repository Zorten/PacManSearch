# Pac-Man Search
## Authors: Zergio, Tyler, Michael


## Question 1: Depth First Search

**The Pacman board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration). Is the exploration order what you would have expected? Does Pacman actually go to all the explored squares on his way to the goal?**

**A:** Yes, the order is what we expected because it expands to states that lead to a dead-end. Since depth-first search continues searching down a path until it can’t anymore, the exploration order occurs as expected. However, Pacman does not go to all the explored squares. This is because Pacman takes the shortest path to the goal state (food) and avoids taking a path that leads to a dead-end.

**Screenshots:**

Q1.1:

<img src="https://github.com/Zorten/PacManSearch/blob/main/images/Q1.1.png" width="400">

Q1.2:

![Q1.2](https://github.com/Zorten/PacManSearch/blob/main/images/Q1.2.png)

Q1.3:

![Q1.3](https://github.com/Zorten/PacManSearch/blob/main/images/Q1.3.png)

Autograder Q1:

![Autograder Q1](https://github.com/Zorten/PacManSearch/blob/main/images/Q1.autograder.png)

## Question 2: Breadth-First Search

**Screenshots:**

Q2.1

![Q2.1](https://github.com/Zorten/PacManSearch/blob/main/images/Q2.1.png)

Q2.2

![Q2.2](https://github.com/Zorten/PacManSearch/blob/main/images/Q2.2.png)

Q2 Autograder

![Q2.autograder](https://github.com/Zorten/PacManSearch/blob/main/images/Q2.autograder.png)

## Question 3: Uniform Cost Search

**Screenshots:**

Q3.1

![Q3.1](https://github.com/Zorten/PacManSearch/blob/main/images/Q3.1.png)

Q3.2

![Q3.2](https://github.com/Zorten/PacManSearch/blob/main/images/Q3.2.png)

Q3.3

![Q3.3](https://github.com/Zorten/PacManSearch/blob/main/images/Q3.3.png)

Q3 Autograder

![Q3.autograder](https://github.com/Zorten/PacManSearch/blob/main/images/Q3.autograder.png)

## Question 4: A* Search

**Screenshots:**

Q4 Autograder

![Q4.1](https://github.com/Zorten/PacManSearch/blob/main/images/Q4.1.png)


Q4 Autograder

![Q4.autograder](https://github.com/Zorten/PacManSearch/blob/main/images/Q4.Autograder.png)

