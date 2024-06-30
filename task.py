import csv


def read_file(filename: str) -> list[dict]:
    with open(filename) as file:
        houses = list(csv.DictReader(file))
        for row in houses:
            row["floor_count"] = int(row["floor_count"])
            row["heating_value"] = float(row["heating_value"])
            row["area_residential"] = float(row["area_residential"])
            row["population"] = int(row["population"])
    return houses


def classify_house(floor_count: int) -> str:
    type1 = "Количество этажей должно быть целочисленным значением."
    type2 = "Количество этажей должно быть положительным числом."
    nofloorhouse = 0
    lowfloorhouse = 5
    middlefloorhouse1 = 6
    middlefloorhouse2 = 16
    if not isinstance(floor_count, int):
        raise TypeError(type1)
    if floor_count <= nofloorhouse:
        raise ValueError(type2)
    if floor_count <= lowfloorhouse:
        return "Малоэтажный"
    if middlefloorhouse1 <= floor_count <= middlefloorhouse2:
        return "Среднеэтажный"
    return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    housesclass = []
    for house in houses:
        floor_count = house.get("floor_count")
        if floor_count is not None:
            housesclassification = classify_house(floor_count)
            housesclass.append(housesclassification)
        elif floor_count is None:
            housesclassification = classify_house("None")
            housesclass.append(housesclassification)
    return housesclass


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    count_dict = {}
    for category in categories:
        count_dict[category] = count_dict.setdefault(category, 0) + 1
    return count_dict

def min_area_residential(houses: list[dict]) -> str:
    min_avg_area = float("+inf")
    address = None
    for house in houses:
        current_avg_area = house["area_residential"] / house["population"]
        if current_avg_area < min_avg_area:
            min_avg_area = current_avg_area
            address = house["house_address"]
    return address


if __name__ == "__main__":
    houses_data = read_file("housing_data.csv")
    print("Классификация дома на основе количества этажей:", classify_house(int(input())))
    for category, count in get_count_house_categories(get_classify_houses(houses_data)).items():
        print(f"{category}: {count} домов")

    print(f"Адрес дома с наименьшей средней жилой площадью на одного человека: {min_area_residential(houses_data)}")
