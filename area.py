import plant_species as ps

class Area:
    def __init__(self, name: str, areas: list['Area'], plants: dict):
        self.__name = name
        self.__plants = plants
        self.__areas = areas
        return

    def get_name(self) -> str:
        return self.__name

    def change_number_of_plants(self, plant_species: str, num: int):
        self.__plants[plant_species] = num
        print(plant_species + ": " + str(num))
        print(self.__plants)
        print(self)

    def get_plants(self) -> dict[str:int]:
        return self.__plants

    def get_areas(self) -> list['Area']:
        return self.__areas



# <area.Area object at 0x0000029FDD6ED110>
# <area.Area object at 0x0000029FDD6ED110>
