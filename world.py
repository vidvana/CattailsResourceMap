import area

class World:
    __areas = []
    __width = 10
    __height = 10
    def __init__(self, areas: list):
        length = len(areas)
        if length > 0:
            self.__areas = areas
        else: # this branch is executed only if the Saver class can't find the specified file with save
            # row 1 (starting from 1)
            World.__areas.append([
                area.Area("Shady Corner", [], {
                    'Blackberries':1,
                     'Catnip':1,
                     'Goldenseal':1,
                     'Lavender':1,
                     'Licorice Root':1,
                     'Marigold':1,
                     'Raspberries':1,
                     'Snake Lily':1,
                     'Valerian':1,
                     'Winter Blueberries':1
                }),
                area.Area("Walking Trail", [], {
                    'Blackberries':1,
                     'Catnip':0,
                     'Goldenseal':1,
                     'Lavender':0,
                     'Licorice Root':1,
                     'Marigold':1,
                     'Raspberries':1,
                     'Snake Lily':0,
                     'Valerian':1,
                     'Winter Blueberries':1
                }),
                area.Area("Graveyard", [], {
                    'Blackberries':1,
                     'Catnip':0,
                     'Goldenseal':1,
                     'Lavender':0,
                     'Licorice Root':1,
                     'Marigold':1,
                     'Raspberries':1,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Cairn Grove", [], {
                    'Blackberries':1,
                     'Catnip':0,
                     'Goldenseal':1,
                     'Lavender':0,
                     'Licorice Root':1,
                     'Marigold':1,
                     'Raspberries':1,
                     'Snake Lily':0,
                     'Valerian':1,
                     'Winter Blueberries':1
                }),
                area.Area("North Plains", [], {
                    'Blackberries':1,
                     'Catnip':0,
                     'Goldenseal':1,
                     'Lavender':0,
                     'Licorice Root':1,
                     'Marigold':1,
                     'Raspberries':1,
                     'Snake Lily':0,
                     'Valerian':1,
                     'Winter Blueberries':1
                }),
                area.Area("The Mountain Domain", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Sentinel Woods", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland Northwest", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland North", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland Lake", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 2 (starting from 1)
            World.__areas.append([
                area.Area("Canyon Plains", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Canyon Prairie", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Canyon Cliffs", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Oak Wood", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("River Corner", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("River Loop", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Lone Sentinel", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland Central", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 3 (starting from 1)
            World.__areas.append([
                area.Area("Canyon Ruins", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Canyon Mesas", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Canyon Creek", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Tomb Creek", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("River Bend", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Central Field", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Blossom Lake", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland Corner", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland South", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Highland Southeast", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 4 (starting from 1)
            World.__areas.append([
                area.Area("Flower Plains", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest Lake", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest Eaves", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest North", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest Outskirts", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Central Lake", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Central Bend", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie North", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie Copse", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie Border North ", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 5 (starting from 1)
            World.__areas.append([
                area.Area("Western Field", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Abandoned Cottage", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("The Fairywood", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Woodland Eyot", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Hallowed Garden", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("River Central", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie Quarry", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie Border Center", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 6 (starting from 1)
            World.__areas.append([
                area.Area("Forest West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("The Forest Colony", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest Central", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Woodland Corner", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Riverspan", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Sacred Temple", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("River Islet", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie Corner", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie South", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Prairie Border South", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 7 (starting from 1)
            World.__areas.append([
                area.Area("Fallen Giant", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest South", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Forest Southeast", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rushing Rocks", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("South Woodland", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Orchard", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Wetland Source", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Swamp Border West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Sunken Stones", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Swamp Border East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 8 (starting from 1)
            World.__areas.append([
                area.Area("Rumbling Stones West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rumbling Stones Central", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rumbling Stones Bridge", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rumbling Stones East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rumbling Corner", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("South Moor", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Wetland Border Northwest", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Wetland Bog", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("The Mystic Colony", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Swamp East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 9 (starting from 1)
            World.__areas.append([
                area.Area("Overstones West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Overstones Central", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Delta", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Overstones East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rumbling Stones South", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Mossy Field", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Wetland Border West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Weepingroot", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Swamp Lakes", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Swamp Cliffs", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
            ])
            # row 10 (starting from 1)
            World.__areas.append([
                area.Area("Beach West", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Beach Central", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rivermouth", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Beach East", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Rumbling Overpass", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Southern Cliffs", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Wetland Border Southwest", [], {
                    'Blackberries':0,
                     'Catnip':0,
                     'Goldenseal':0,
                     'Lavender':0,
                     'Licorice Root':0,
                     'Marigold':0,
                     'Raspberries':0,
                     'Snake Lily':0,
                     'Valerian':0,
                     'Winter Blueberries':0
                }),
                area.Area("Wetland Outskirts", [], {
                    'Blackberries':1,
                     'Catnip':1,
                     'Goldenseal':1,
                     'Lavender':1,
                     'Licorice Root':1,
                     'Marigold':1,
                     'Raspberries':1,
                     'Snake Lily':1,
                     'Valerian':1,
                     'Winter Blueberries':1
                }),
                area.Area("Swamp South", [], {
                    'Blackberries':2,
                     'Catnip':2,
                     'Goldenseal':2,
                     'Lavender':2,
                     'Licorice Root':2,
                     'Marigold':2,
                     'Raspberries':2,
                     'Snake Lily':2,
                     'Valerian':2,
                     'Winter Blueberries':2
                }),
                area.Area("Swamp Corner", [], {
                    'Blackberries':3,
                     'Catnip':4,
                     'Goldenseal':4,
                     'Lavender':4,
                     'Licorice Root':4,
                     'Marigold':4,
                     'Raspberries':4,
                     'Snake Lily':4,
                     'Valerian':4,
                     'Winter Blueberries':4
                }),
            ])
        return



    def get_width(self):
        return World.__width

    def get_height(self):
        return World.__height

    def get_area(self, x: int, y: int):
        return self.__areas[y][x]

    def change_area_no_of_plants(self, x: int, y: int, species: str, quantity: int):
        self.__areas[y][x].change_number_of_plants(species, quantity)
