import json
import world
class Saver:

    def __init__(self, world: 'World'):
        self.__world = world


    def save(self):
        f = open("map.txt", "w")
        x = self.__world.get_width()
        y = self.__world.get_height()
        for i in range(x):
            for j in range(y):
                area = self.__world.get_area(i, j)
                f.write(area.get_name())
                f.write("\n")
                f.write(json.dumps(area.get_plants()))
                f.write("\n")
        f.close()

