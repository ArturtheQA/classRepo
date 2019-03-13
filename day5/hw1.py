
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
def hw1_1():
    i = 0
    while i != 20+1:
        print(i+1)
        i = i+1


def hw1_2():
    i = 0
    while i in range(0, 20):
        print(i+1)
        i = i+1


def hw2_1():
    i = 0
    a = int(input("put number"))
    while i != a:
        print(a-i)
        i = i+1


def hw3():
    i = 0
    a = int(input("put number"))
    while i < (a+1):
        print(i*i)
        i = i+1


def hw4():
    i = 2
    dinamicvalue = 2
    result = 0
    while result < 65536+1:
        result = i**dinamicvalue
        print(result)
        i = i+1


def hw5_1():
    a = input("please eneter some word")
    print(len(a))


def hw5_2():
    i = 0
    a = input("please enter some word")
    while i != len(a)+1:
        i = i+1
    print(i)


def hw6_1():
    i = 0
    acount = 0
    a = input("please enter some word")
    while i != len(a)+1:
        i = i+1
        for letter in a:
            if letter == "a":
                acount = acount+1
                break
    
    print(i-1, acount-1)




# def hw7_1():
#     i = {1: "one", 2: 'two', 3: 'three'}
#     u = int(input("please place the #"))
#     print(i[u])


def hw9(states):
    # counter=0
    bigOneName=''
    bigOnePopulation=0
    top5=[]
    time=0
    times=5
    while time != times:
        # while counter <len(states):
            for state in states:
                if states[state] > bigOnePopulation:
                    bigOnePopulation=states[state]
                    bigOneName=state
            # counter=counter+1
            states.pop(bigOneName)
            top5.append(bigOneName)
            bigOneName=''
            bigOnePopulation=0
            time=time+1
    print(top5)


# def hw5_2():
#     i = 0
#     a = input("please enter some word")
#     while i != len(a)+1:
#         i = i+1
#     print(i-1)

# # hw5_2()

# hw9(states)


# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if (year % 4 == 0 and year % 100 != 0)or (year % 100 == 0 and year % 400 == 0):
#         leap = True
#     elif year % 100 == 0:
#         leap = False
    
#     print(leap)

# is_leap(2100)
hw9(states)