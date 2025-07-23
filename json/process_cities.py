import json
import csv
import os
from collections import Counter

# Чтение
def read_json(file_path="city.list.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {file_path} поврежден или не является JSON.")
        return []

# Запись
def write_json(data, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Файл {file_path} успешно создан.")
    except Exception as e:
        print(f"Ошибка записи в {file_path}: {e}")

# Подсчет городов
def count_cities(cities):
    return len(cities)

# Словарь с количеством городов по странам
def count_cities_by_country(cities):
    return dict(Counter(city.get("country", "Unknoun") for city in cities))

# Подсчет городов в северном и южном полушариях
def count_hemispheres(cities):
    northern = 0
    southern = 0
    for city in cities:
        coord = city.get("coord")
        if coord and isinstance(coord.get("lat"), (int, float)):
            if coord["lat"] > 0:
                northern += 1
            elif coord["lat"] < 0:
                southern += 1
    return northern, southern

# Создание CSV файла
def create_csv(cities, output_file="cities.csv"):
    try:
        with open(output_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "country", "coordinates"])
            for city in cities:
                coord = city.get("coord", {})
                if all(key in city for key in ["name", "country"]) and all(key in coord for key in ["lat", "lon"]):
                    coordinates = f"{coord['lat']},{coord['lon']}"
                    writer.writerow([city["name"], city["country"], coordinates])
                else:
                    print(f"Пропущен город {city.get('name', 'Unknown')}: осутствуют необходимые поля.")
        print(f"Файл {output_file} успешно создан.")
    except Exception as e:
        print(f"Ошибка создания CSV: {e}")

# JSON для одной страницы
def create_country_json(cities, country_code, output_file="cities.json"):
    filtered_cities = [city for city in cities if city.get("country") == country_code]
    if not filtered_cities:
        print(f"Нет городов для страны {country_code}.")
        return
    write_json(filtered_cities, output_file)

# JSON для каждой страны
def create_json_per_country(cities, output_dir="countries"):
    try:
        os.makedirs(output_dir, exist_ok=True)
        country_cities = {}
        for city in cities:
            country = city.get("country", "Unknown")
            if country not in country_cities:
                country_cities[country] = []
            country_cities[country].append(city)

        for country, cities in country_cities.items():
            output_file = os.path.join(output_dir, f"{country}.json")
            write_json(cities, output_file)
    except Exception as e:
        print(f"Ошибка создания JSON файлов для стран: {e}")

# GeoJSON для одной страны
def create_geojson(cities, country_code, output_file="cities.geojson"):
    filtered_cities = [city for city in cities if city.get("country") == country_code]
    if not filtered_cities:
        print(f"Нет городов для страны {country_code}.")
        return

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for city in filtered_cities:
        coord = city.get("coord", {})
        if all(key in city for key in ["name", "country"]) and all(key in coord for key in ["lat", "lon"]):
            if isinstance(coord["lat"], (int, float)) and isinstance(coord["lon"], (int, float)):
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [coord["lon"], coord["lat"]]
                    },
                    "properties": {
                        "name": city["name"],
                        "country": city["country"],
                        "id": city.get("id"),
                        "state": city.get("state"),
                        "is_capital": city.get("is_capital", False)
                    }
                }
                geojson["features"].append(feature)
            else:
                print(f"Пропущен город {city['name']}: некорректные координаты.")
        else:
            print(f"Пропущен город {city.get('name', 'Unknown')}: отсутствуют необходимые поля.")

    write_json(geojson, output_file)

def main():
    # Чтение данных
    cities = read_json()
    if not cities:
        print("Нет данных для обработки.")
        return

    # 1. Количество городов
    total_cities = count_cities(cities)
    print(f"1. Общее количество городов: {total_cities}")

    # 2. Количество городов по странам
    country_counts = count_cities_by_country(cities)
    print("2. Количество городов по странам:")
    for country, count in sorted(country_counts.items()):
        print(f"   {country}: {count}")

    # 3. Города в северном и южном полушариях
    northern, southern = count_hemispheres(cities)
    print(f"3. Города в северном полушарии: {northern}")
    print(f"   Города в южном полушарии: {southern}")

    # 4. Создание CSV
    create_csv(cities)

    # 5. JSON для одной страны
    create_country_json(cities, "RU")

    # 6. JSON для каждой страны
    create_json_per_country(cities)

    # 7. GeoJSON для одной страны
    create_geojson(cities, "RU")

if __name__ == "__main__":
    main()


