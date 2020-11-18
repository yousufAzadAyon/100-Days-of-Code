travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name, visit_count, cities_visited):
    new_item ={}
    new_item["country"] = name
    new_item["visits"] = visit_count
    new_item["cities"] = cities_visited
    travel_log.append(new_item)

add_new_country("Spain", 2, ["cordova", "madrid"])

print(travel_log)