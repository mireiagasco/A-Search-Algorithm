"""
A* Search Implementation
TDT4136 - Introduction to Artificial Intelligence (NTNU)
"""
__author__ = "Mireia Gasco Agorreta"
__email__ = "mireiagasco271@gmail.com"

from Map import Map_Obj
from queue import PriorityQueue

map = Map_Obj(1)
map.read_map("Samfundet_map_1.csv")
map.fill_critical_positions(1)
map.show_map()

def a_star_search(themap: Map_Obj):
    """A* Search Algorithm

    :param themap: map object
    :return: a new map object with the shortest path from start to goal
    """

    frontier = PriorityQueue()
    start = map.get_start_pos()
    goal = map.get_goal_pos()
    frontier.put(start, 0)

    came_from = dict()
    cost_so_far = dict()

    came_from[tuple(start)] = None
    cost_so_far[tuple(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break

        neighbours_list = map.get_neighbours(current)
        for next in neighbours_list:
            new_cost = cost_so_far[tuple(current)] + map.get_cell_value(next)
            if tuple(next) not in cost_so_far or new_cost < cost_so_far[tuple(next)]:
                cost_so_far[tuple(next)] = new_cost
                priority = new_cost + heuristic_manhattan(goal, next)
                frontier.put(next, priority)
                came_from[tuple(next)] = current

    return came_from, cost_so_far

def heuristic_manhattan(goal, pos) -> int:
    """Heuristic Function
    Calculates the Manhattan distance from the position to the goal.

    Parameters
    ----------
    goal : list[int]
        Coordinates of the goal position
    pos  : list[int]
        Coordinates of the actual position
    """
    return sum(abs(val1-val2) for val1, val2 in zip(goal,pos))

def reconstruct_path(came_from: dict[tuple, int],start: list, goal: list):
    current = goal
    start = start
    goal = goal
    if tuple(goal) not in came_from: # no path was found
        return []
    while current != start:
        map.str_map[current] = 1
        current = came_from[tuple(current)]

came_from, cost_so_far = a_star_search(map)
reconstruct_path(came_from, map.get_start_pos(), map.get_end_goal_pos())
map.show_map()
