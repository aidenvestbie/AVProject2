"""
Road Trip -- Arizona 2020
5 Locations in 5 Days

    by Aiden Vestbie
"""

from itertools import permutations, combinations_with_replacement
from typing import Dict, Any, Tuple

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

HOTEL_BUDGET = 850
days = 5

cityperms = list(permutations(city_temps, days))


def route_temp(route):
    """
    Find the average temperature for any combination of temperatures(route)
    of each order you visit the cities
    """
    temp = 0
    for i in range(len(route)):
        city = route[i]
        temp += city_temps[city][i]
    return temp / len(route)


# Find the route with the highest average temperature
bestroute = max([(route_temp(r), r) for r in cityperms])

hotel_list = list(hotel_rates.keys())
h_combs = list(combinations_with_replacement(hotel_list, days))


def hotel_costs(t):
    """
    Find the cost of the hotels by creating a for loop that adds
    each of the values of the hotel combination 't'
    """
    x = 0
    for i in t:
        x += hotel_rates[i]
    return x


# find the list of hotels that fits the budget
best_hotels = min(h_combs,
                  key=lambda t: HOTEL_BUDGET - hotel_costs(t) if HOTEL_BUDGET >= hotel_costs(t) else HOTEL_BUDGET)

if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())

    print(f'Here is your best route: {bestroute[1]} the average of the daily max temp. is {bestroute[0]}F')

    print(f'To max out your hotel budget, stay at these hotels: {best_hotels}, totaling ${hotel_costs(best_hotels)}')
