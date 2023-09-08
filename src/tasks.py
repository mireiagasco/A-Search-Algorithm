from src.ASearch import a_star_search, reconstruct_path
from src.Map import Map_Obj

map1 = Map_Obj(1)
map1.read_map("Samfundet_map_1.csv")
map1.fill_critical_positions(1)

map2 = Map_Obj(2)
map2.read_map("Samfundet_map_2.csv")
map2.fill_critical_positions(2)

map3 = Map_Obj(3)
map3.read_map("Samfundet_map_2.csv")
map3.fill_critical_positions(3)

map4 = Map_Obj(4)
map4.read_map("Samfundet_map_Edgar_full.csv")
map4.fill_critical_positions(4)

# -> Task 1
map1.show_map()
came_from = a_star_search(map1)
reconstruct_path(map1, came_from)
map1.show_map()

# -> Task 2
map2.show_map()
came_from = a_star_search(map2)
reconstruct_path(map2, came_from)
map2.show_map()

# -> Task 3
map3.show_map()
came_from = a_star_search(map3)
reconstruct_path(map3, came_from)
map3.show_map()

# -> Task 4
map4.show_map()
came_from = a_star_search(map4)
reconstruct_path(map4, came_from)
map4.show_map()