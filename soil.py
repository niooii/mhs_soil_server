import random


class SoilInfo:
    moisture: float = 0
    temperature: float = 0
    air_quality: float = 0

    ## message should be recieved in this format:
    def __init__(self, message: str):
        print(f"recv message: {message}")
        data = message.split(",")
        self.temperature = float(data[0])
        self.moisture = float(data[1])


def calculate_goodness(soil_info: SoilInfo) -> float:
    # print    print(f"INDEX: {index}")

    if soil_info.temperature > 40 or soil_info.temperature < 10 or soil_info.moisture == 0:
        return 0

    TempFactor = abs(soil_info.temperature - 26.5) / 20.0
    MoistureFactor = abs(soil_info.moisture - 400.0) / 500.0

    goodness: float = (Lerp(1, 0, TempFactor) + Lerp(1, 0, MoistureFactor)) / 2
    return goodness


def Lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t
