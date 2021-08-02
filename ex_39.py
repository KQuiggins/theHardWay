# create a mapping of state to abbreviation

states = {'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'}

# Mapping of cities
cities = {"CA": "San Francisco", "MI": "Detroit", "FL": "Jacksonville"}

# Add some cities to our dict
cities['OR'] = "Portland"
cities["NY"] = "New York"

print('-' * 10)

# Print out some cities
print(f"NY State has: {cities['NY']}")
print(f"OR State has: {cities['OR']}")

# Print every state abbreviation
print("-" * 10)
for state, abbrev in states.items():
    print(f'{state} is abbreviated {abbrev}')

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print(f'{abbrev} has the city {city}')

print('-' * 10)
for state, abbrev in states.items():
    print(f'{state} state is abbreviated {abbrev} and has city {cities[abbrev]}')

print("-" * 10)
state = states.get("Texas", None)
if not state:
    print("Sorry, no Texas")

city = cities.get("TX", "Does not exist")
print(f"The city for the state 'TX' is: {city}")
