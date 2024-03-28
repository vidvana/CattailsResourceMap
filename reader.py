import area
import world
from pathlib import Path
import json

class Reader:

    def __init__(self):
        pass

    def read(self) -> 'World':
        filename = "map.txt"
        my_file = Path(filename)
        if my_file.is_file():
            # print("File found!")
            file = open(filename, 'r')
            lines = file.readlines()
            world_width, world_height = 10, 10
            areas = [[None for i in range(world_width)] for i in range(world_height)]
            col, row = 0, 0
            for i in range(len(lines)//2):
                name = lines[i*2].strip('\n')
                plants = json.loads(lines[i*2+1])
                areas[col][row] = area.Area(name, [], plants)
                col += 1
                if col == 10:
                    row += 1
                    col = 0
        else:
            areas = []
        return world.World(areas)
        pass