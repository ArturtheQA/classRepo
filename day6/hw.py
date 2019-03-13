# source: https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population
# a dictionary of states and their corresponding population numbers
states = {
    "California": 39557045,
    "Texas": 28701845,
    "Florida": 21299325,
    "New York": 19542209,
    "Pennsylvania": 12807060,
    "Illinois": 12741080,
    "Ohio": 11689442,
    "Georgia": 10519475,
    "North Carolina": 10383620,
    "Michigan": 9998915,
    "New Jersey": 9032873,
    "Virginia": 8517685,
    "Washington": 7535591,
    "Arizona": 7171646,
    "Massachusetts": 6902149,
    "Tennessee": 6770010,
    "Indiana": 6691878,
    "Missouri": 6126452,
    "Maryland": 6042718,
    "Wisconsin": 5813568,
    "Colorado": 5695564,
    "Minnesota": 5611179,
    "South Carolina": 5084127,
    "Alabama": 4887871,
    "Louisiana": 4659978,
    "Kentucky": 4468402,
    "Oregon": 4190713,
    "Oklahoma": 3943079,
    "Connecticut": 3572665,
    "Puerto Rico": 3195153,
    "Utah": 3161105,
    "Iowa": 3156145,
    "Nevada": 3034392,
    "Arkansas": 3013825,
    "Mississippi": 2986530,
    "Kansas": 2911505,
    "New Mexico": 2095428,
    "Nebraska": 1929268,
    "West Virginia": 1805832,
    "Idaho": 1754208,
    "Hawaii": 1420491,
    "New Hampshire": 1356458,
    "Maine": 1338404,
    "Montana": 1062305,
    "Rhode Island": 1057315,
    "Delaware": 967171,
    "South Dakota": 882235,
    " North Dakota": 760077,
    "Alaska": 737438,
    "District of Columbia": 702455,
    "Vermont": 626299,
    "Wyoming": 577737,
    "Guam": 165718,
    "U.S. Virgin Islands": 104914,
    "American Samoa": 55641,
    "Northern Mariana Islands": 55194,
    "Wake Island": 100,
    "Palmyra Atoll": 20,
    "Midway Atoll": 40,
    "Johnston Atoll": 0,
    "Baker Island": 0,
    "Howland Island": 0,
    "Jarvis Island": 0,
    "Kingman Reef": 0,
    "Navassa Island": 0
}

# now, let's reverse the dictionary: population will be the key, and state name will be the value
states_pop_first = {}
for state, population in states.items():
    states_pop_first[population] = state

# now, let's sort the reversed map's keys, so we can get top 5 population numbers
top5_state_pops = sorted(states_pop_first.keys())[::-1][:5]

# since we have top 5 population numbers now, we can access the reversed map using those numbers
for pop in top5_state_pops:
    print(states_pop_first[pop], pop)

abc=['abc',111,222]