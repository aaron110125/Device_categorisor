
import logging


class BaseBuilding(object):
    """
    Base class for all buildings.
    """

    def __init__(self):
        self.corner_stone = "Cornerstone to come with a solution for the base of the building"
        logging.info('This is the base building class')
        print('This is the base building class')

class BaseBuilding_second(object):
    """
    Base class for the second building
    """

    def __init__(self):
        self.second_corner_stone = "Cornerstone to come with a solution for the base of the second building"
        logging.info('This is the base building class for the second building')
        print('This is the base building class for the second building')

class BaseBuilding_derieved(BaseBuilding, BaseBuilding_second):
    """
    Derived class for all buildings
    """

    def __init__(self):
        BaseBuilding.__init__(self)
        BaseBuilding_second.__init__(self)
        logging.info('This is the derived class for all buildings')
        print('This is the derived class for all buildings')

    def display_all_buildings(self):
        """
        Display all buildings
        """
        print(self.corner_stone + " and " + self.second_corner_stone)

citadel = BaseBuilding_derieved()
citadel.display_all_buildings()
