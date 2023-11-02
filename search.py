# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    
    # Get the initial state and check if it is goal
    #All states are in the form of coordinates (x, y), with (0,0) being the lower left corner of gameboard
    start_state = problem.getStartState()
    
    if problem.isGoalState(start_state):
        return []
    
    #initialize stack to keep track of nodes at frontier being explored
    frontier = util.Stack()
    #initialize set to keep track of nodes already visited
    visited = set()
    
    #start with exploring initial state 
    frontier.push(([start_state], [])) ## appends a tuple of the form: ([Path], [moves]) to the stack
    
    #Loop while there are nodes to be explored in the frontier
    while not frontier.isEmpty():
        #Get the node at the top of the frontier stack 
        path, moves = frontier.pop()
        #path contains a list of nodes visited up to this point that make up our path to the goal
        # Access the last node in this list by using -1 index, and add to visited set 
        visited.add(path[-1])
        #Check if last node in path is the goal, if so return the list of moves in this path
        if problem.isGoalState(path[-1]):
            return moves
        
        #If not at goal state, expand successors of the last node in the path to the goal
        #problem.getSuccessors(coordinate) returns a list of successors in the form: (successor_state, move_to_get_there, cost_of_that_move)
        for (state, move, cost) in problem.getSuccessors(path[-1]):
            #If the node has not been added to the visited set, append it to the frontier stack, with the updated path and moves
            if state not in visited:
                frontier.push((path + [state], moves+[move]))       
    #If stack is empty, it means no solution was found as the goal state was not found in any of the explorable nodes
    raise ValueError("There is no solution")

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    # Get the initial state and check if it is goal
    #All states are in the form of coordinates (x, y), with (0,0) being the lower left corner of gameboard
    start_state = problem.getStartState()
    
    if problem.isGoalState(start_state):
        return []
    
    #initialize set to keep track of nodes already visited
    visited = set()
    #initialize queue to keep track of nodes being explored 
    frontier = util.Queue()
    #initialize set to keep track of states in queue to prevent exploring twice
    frontier_states = set()
    
    #start by exploring initial state
    frontier.push(([start_state], [])) #appends a tuple of the form: ([Path], [moves]) to the queue
    
    #loop while there are still nodes in queue 
    while not frontier.isEmpty():
        #Get the node at the front of the queue
        path, moves = frontier.pop()
        #Append to the visited set the last node on the path up until this point
        visited.add(path[-1])
        #Check if the last node visited is in the set, if so remove it
        if path[-1] in frontier_states:
            frontier_states.remove(path[-1])
        #Check if the node is the goal state, if so return list of moves to this node 
        if problem.isGoalState(path[-1]):
            return moves
        
        #Expand the last node in the path, and for each of the children, add to frontier_states set
        #and frontier queue, if they aren't part of it already
        for (state, move, cost) in problem.getSuccessors(path[-1]):
            if state not in visited and state not in frontier_states:
                frontier_states.add(state)
                frontier.push((path + [state], moves+[move]))  
    raise ValueError("There is no solution")

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    # Get the initial state and check if it is goal
    #All states are in the form of coordinates (x, y), with (0,0) being the lower left corner of gameboard
    start_state = problem.getStartState()
    
    if problem.isGoalState(start_state):
        return []
    
    #initialize priority queue to keep track of nodes being explored 
    frontier = util.PriorityQueue()
    #initialize set to keep track of nodes already visited
    visited = set()
    
    #start by exploring initial state
    frontier.push(([start_state], []), 0) #appends a tuple of the form: ([Path], [moves], cost to this state) to the priority queue
    
    #loop while priority queue is not empty, so there are still nodes to be visited
    while not frontier.isEmpty():
        #get the node with the highest priority 
        path, moves = frontier.pop()
        
        if path[-1] in visited:
            # This happens if it was already visted with a lower cost
            # In theory, you could be checking the queue every time you add
            # but that's a lot of work and this is easy.
            continue
        
        #add the current node to the visited set 
        visited.add(path[-1])
            
        #check if goal reached, if so return list of moves to get there
        if problem.isGoalState(path[-1]):
            return moves

        #Get children of current state, and for each one, if it hasn't been visited already, add to the priority queue 
        for (state, move, cost) in problem.getSuccessors(path[-1]):
            if state not in visited :
                frontier.push((path+[state], moves+[move]), problem.getCostOfActions(moves) + cost)       
    raise ValueError("There is no solution")

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Get the initial state and check if it is goal
    #All states are in the form of coordinates (x, y), with (0,0) being the lower left corner of gameboard
    start_state = problem.getStartState()
    
    if problem.isGoalState(start_state):
        return []
    
    #initialize priority queue to keep track of nodes being explored 
    frontier = util.PriorityQueue()
    #initialize set to keep track of nodes already visited
    visited = set()
    
    #start by exploring initial state
    frontier.push(([start_state], []), 0) #appends a tuple of the form: ([Path], [moves], cost to this state) to the priority queue
    
    #loop while priority queue is not empty, so there are still nodes to be visited
    while not frontier.isEmpty():
        #get the node with the highest priority 
        path, moves = frontier.pop()
        
        if path[-1] in visited:
            # This happens if it was already visted with a lower cost
            # In theory, you could be checking the queue every time you add
            # but that's a lot of work and this is easy.
            continue
        
        #add the current node to the visited set 
        visited.add(path[-1])
            
        #check if goal reached, if so return list of moves to get there
        if problem.isGoalState(path[-1]):
            return moves

        #Get children of current state, and for each one, if it hasn't been visited already, add to the priority queue 
        for (state, move, cost) in problem.getSuccessors(path[-1]):
            if state not in visited :
                #calculate cost of expanding the node (costF) by adding cost of path to the node (costG) 
                # and the calculated cost to goal from the heuristic (costH)
                costG = problem.getCostOfActions(moves) + cost
                costH = heuristic(state, problem)
                costF = costG + costH
                frontier.push((path+[state], moves+[move]), costF)       
    raise ValueError("There is no solution")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
