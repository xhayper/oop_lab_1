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

def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []

    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])

    return aggregation_function(temps)

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
print("\n".join(x["city"] for x in filter(lambda x: x["country"] == "Germany", cities)))

# Print all cities in Spain with a temperature above 12°C

print()
print("City in spain with a temperature above 12°C")
print("\n".join(x["city"] for x in filter(lambda x: x["country"] == "Spain" and float(x["temperature"]) > 12, cities)))

# Count the number of unique countries

print()
print(f"Amount of countries: {aggregate('country', lambda x: len(set(x)), cities)}")

# Print the average temperature for all the cities in Germany

print()
germany_cities = [float(x['temperature']) for x in cities if x['country'] == 'Germany']
print(f"Average temperature in Germany: {sum(germany_cities) / len(germany_cities)}")

# Print the max temperature for all the cities in Italy

print()
italy_cities = [float(x['temperature']) for x in cities if x['country'] == 'Italy']
print(f"Max temperature in Italy: {max(italy_cities)}")