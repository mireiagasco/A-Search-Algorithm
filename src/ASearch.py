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
    frontier.put((0, start))

    came_from = dict()
    cost_so_far = dict()

    came_from[tuple(start)] = None
    cost_so_far[tuple(start)] = 0

    while not frontier.empty():
        current = frontier.get()[1]
        if current == goal:
            # Goal reached
            break

        neighbours_list = map.get_neighbours(current)
        for next in neighbours_list:
            new_cost = cost_so_far[tuple(current)] + map.get_cell_value(next)
            if tuple(next) not in cost_so_far or new_cost < cost_so_far[tuple(next)]:
                came_from[tuple(next)] = current
                cost_so_far[tuple(next)] = new_cost
                priority = new_cost + heuristic_manhattan(goal, next)
                frontier.put((priority, next))


    return came_from

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

def reconstruct_path(map: Map_Obj, came_from):
    """ Method to reconstruct the shortest path.
    Modifies the map to show the path in yellow
    :param map: the map
    :param came_from: output of the a_star_search()
    :return: a list with the path
    """

    start = map.get_start_pos()
    goal = map.get_end_goal_pos()
    current = came_from[tuple(goal)]
    path = []
    if tuple(goal) not in came_from:
        return []
    while current != start:
        path.append(current)
        map.str_map[tuple(current)] = 1
        current = came_from[tuple(current)]
    return path.reverse()


came_from = a_star_search(map)
reconstruct_path(map, came_from)
map.show_map()
