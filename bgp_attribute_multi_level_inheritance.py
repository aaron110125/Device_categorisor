import logging
class BGPBaseAttributes(object):

    # declaring init method with base constructor
    def __init__(self, weight):
        logging.info('Prefer path with highest weight. Default routes weight is 0')
        self.weight = weight

    # to find out the weight of a particular path
    def get_weight(self):
        return self.weight


class DerievedchildBGPAttribute(BGPBaseAttributes):
    # Constructor for DerievedBGPAttribute class
    def __init__(self, weight, local_preference):
        BGPBaseAttributes.__init__(self, weight)
        logging.info('Prefer path with highest local_preference')
        self.local_preference = local_preference


    # to find out the local preference of a specified path 
    def get_local_preference(self):
        return self.local_preference

#Inherited or Sub class 

class GrandDerievedBGPAttribute(DerievedchildBGPAttribute):
    # Constructor for GrandDerievedBGPAttribute class

    def __init__(self, weight, local_preference, orginate):
        DerievedchildBGPAttribute.__init__(self, weight, local_preference)
        logging.info('Local router with attribute 0.0.0.0 is introduced')
        self.orginate  = orginate

    #To find the originate in the local path
    def get_orginate(self):
        return self.orginate

bgpattributes = GrandDerievedBGPAttribute("25", "34", "0.0.0.0")
print(bgpattributes.get_weight(), bgpattributes.get_local_preference(), bgpattributes.get_orginate())

