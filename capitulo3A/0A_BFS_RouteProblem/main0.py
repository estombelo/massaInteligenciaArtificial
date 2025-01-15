from Algortimos0 import *
from Map0 import Map
from RoutProblem0 import RouteProblem

romania = Map(
    {('O', 'Z'):  71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118,
     ('L', 'T'): 111, ('L', 'M'):  70, ('D', 'M'): 75, ('C', 'D'): 120, ('C', 'R'): 146,
     ('C', 'P'): 138, ('R', 'S'):  80, ('F', 'S'): 99, ('B', 'F'): 211, ('B', 'P'): 101,
     ('B', 'G'):  90, ('B', 'U'):  85, ('H', 'U'): 98, ('E', 'H'):  86, ('U', 'V'): 142,
     ('I', 'V'):  92, ('I', 'N'):  87, ('P', 'R'): 97},
    {'A': ( 76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294),
     'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
     'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
     'S': (187, 463), 'T': ( 83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)})

r1 = RouteProblem('A', 'B', map=romania)
print('*' * 30)
print("Lista definitiva de Estados e ações utilizando breadth_first_bfs():")
print( r1 )
solution_node = breadth_first_bfs(r1)
print( path_states( solution_node ) )
print( path_actions( solution_node ) )

print('*' * 30)
print("Lista definitiva de Estados utilizando uniform_cost_search():")
print( r1 )
solution_node = uniform_cost_search(r1)
print( path_states( solution_node ) )
print( path_actions( solution_node ) )

print('*' * 30)
print("Lista definitiva de Estados utilizando depth_first_bfs():")
print( r1 )
solution_node = depth_first_bfs(r1)
print( path_states( solution_node ) )
print( path_actions( solution_node ) )

print('*' * 30)
print("Lista definitiva de Estados utilizando depth_limited_search():")
print( r1 )
solution_node = depth_limited_search(r1)
print( path_states( solution_node ) )
print( path_actions( solution_node ) )

print('*' * 30)
print("Lista definitiva de Estados utilizando iterative_deepening_search():")
print( r1 )
solution_node = iterative_deepening_search(r1)
print( path_states( solution_node ) )
print( path_actions( solution_node ) )


