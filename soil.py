import random


class SoilInfo:
    coord_x: int = 0
    coord_y: int = 0
    moisture: float = 0
    temperature: float = 0
    air_quality: float = 0

    ## message should be recieved in this format:
    def __init__(self, message: str):
        data = message.split(",")
        self.coord_x = int(data[0])
        self.coord_y = int(data[1])
        print(f"{self.coord_x}, {self.coord_y}")
        self.temperature = float(data[2])
        self.moisture = float(data[3])


def calculate_goodness(soil_info: SoilInfo) -> float:
    print(f"calculating goodness for values:\n "
          f"temperature: {soil_info.temperature}\n"
          f"moisture: {soil_info.moisture}\n"
          f"air quality: {soil_info.air_quality}")
    goodness: float = soil_info.temperature / float(10)
    return goodness
