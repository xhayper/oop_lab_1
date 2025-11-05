import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("City in Germany")
city_in_germany = []
for city in cities:
    if city["country"] == "Germany":
        city_in_germany.append(city["city"])
print("\n".join(city_in_germany))

# Print all cities in Spain with a temperature above 12°C

print()
print("City in spain with a temperature above 12°C")
city_in_spain_above_12 = []
for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        city_in_spain_above_12.append(city["city"])
print("\n".join(city_in_spain_above_12))

# Count the number of unique countries

print()
countries = []
for city in cities:
    if city["country"] in countries:
        continue
    countries.append(city["country"])
print(f"Count of countries: {len(countries)}")

# Print the average temperature for all the cities in Germany

print()
temperature_in_germany = 0
city_in_germany = 0
for city in cities:
    if city["country"] == "Germany":
        temperature_in_germany += float(city["temperature"])
        city_in_germany += 1
print(f"Average temperature in Germany: {temperature_in_germany / city_in_germany}")

# Print the max temperature for all the cities in Italy

print()
max_temperature = 0
max_temperature_name = ""
for city in cities:
    if city["country"] != "Italy":
        continue

    if float(city["temperature"]) <= max_temperature:
        continue

    max_temperature = float(city["temperature"])
    max_temperature_name = city["city"]
print(f"{max_temperature_name} is the hottest city in Italy with temperature of {max_temperature}")