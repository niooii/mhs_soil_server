import random


class SoilInfo:
    coord_x: int = 0
    coord_y: int = 0
    moisture: float = 0
    air_quality: float = 0

    ## message should be recieved in this format:
    def __init__(self, message: str):
        data = message.split(",")
        self.coord_x = int(data[0])
        self.coord_y = int(data[1])
        self.moisture = random.randrange(20, 200)
        self.air_quality = random.randrange(1, 100)


def calculate_goodness(soil_info: SoilInfo) -> float:
    goodness: float = (soil_info.air_quality + soil_info.moisture) / 100
    return goodness
