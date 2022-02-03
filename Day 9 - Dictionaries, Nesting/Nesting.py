
#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a dictionary...
travel_log = {
    "France":["Paris","lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"]
}
#Nesting a dictionary in a dictionary.
trabel_times = {
    "France":
    {"cities_visited": ["Paris", "lille","Dijon"],"total_visits":12},
    "Germany":
    {"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits": 10}
     }
#Nesting a dictionary in a list.
trabel_times = [
    {
    "Country":"France",
    "cities_visited": ["Paris", "lille","Dijon"],
    "total_visits":12
    },
    {
    "country": "Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"],
    "total_visits": 10
    },
]

