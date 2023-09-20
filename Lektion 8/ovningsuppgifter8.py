
# 14.1
# kmpermiles = 1.609344
# milesperkm = 0.621371192237334


# def milestokm(indata):
#     length = ""
#     unit = ""
#     for x in indata:
#         if x.isalpha():
#             unit += x
#         elif x.isdigit():
#             length += x

#     if unit == "miles":
#         return f"{length} {unit} motsvarar {float(length) * kmpermiles} km."
#     elif unit == "km":
#         return f"{length} {unit} motsvarar {float(length) * milesperkm} miles."


# print(milestokm(input("Ange distans: ")))
# 14.2
# import ui
# ui.line(False)
# ui.header("Exempel")
# ui.line(True)
# ui.echo("Det här är en ui\nJättefin")
# ui.prompt("Vad vill du göra?")
# ui.line(False)

#14.3
# import random


# def get_even(nums):
#     even = []
#     for x in nums:
#         if x % 2 == 0:
#             even.append(x)
#     return even


# numbers = []
# for x in range(10):
#     numbers.append(random.randint(0, 9))

# print(get_even(numbers))
# print(numbers)

# 14.4
teams = {
    'Brazil': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goalsfor': 0,
        'goalsagainst': 0
            },
    'Serbia': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goalsfor': 0,
        'goalsagainst': 0
            },
    'Switzerland': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goalsfor': 0,
        'goalsagainst': 0
            },
    'CostaRica': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goalsfor': 0,
        'goalsagainst': 0
            }
    }


def add_game(home_team, home_score, away_team, away_score):
    if home_score > away_score:
        teams[home_team]["wins"] += 1
        teams[away_team]["losses"] += 1
    elif home_score < away_score:
        teams[home_team]["losses"] += 1
        teams[away_team]["wins"] += 1
    elif home_score == away_score:
        teams[home_team]["draws"] += 1
        teams[away_team]["draws"] += 1

    teams[home_team]["goalsfor"] += home_score
    teams[away_team]["goalsfor"] += away_score
    teams[away_team]["goalsagainst"] += home_score
    teams[home_team]["goalsagainst"] += away_score


def make_list(dict):
    newlist = []
    for country in dict:
        new_dict = {
            "country": country,
            "wins": teams[country]["wins"],
            "draws": teams[country]["draws"],
            "losses": teams[country]["losses"],
            "goalsfor": teams[country]["goalsfor"],
            "goalsagainst": teams[country]["goalsagainst"],
            "goaldifference": (teams[country]["goalsfor"] -
                               teams[country]["goalsagainst"]),
            "points": (teams[country]["wins"] * 3) + teams[country]["draws"]
        }
        newlist.append(new_dict)
    return newlist


def get_points(e):
    return e["points"]


def sort_list():
    lst_teams.sort(reverse=True, key=get_points)


def print_tabellist(currlist):
    ui_width = 50
    print("-" * ui_width)
    print("| # |", "Nation".ljust(11), "| W | D | L | GF | GA | GD | P |")
    print("-" * ui_width)
    nums = 1
    for x in currlist:
        c = str(x["country"]).ljust(11)
        w = x["wins"]
        d = x["draws"]
        L = x["losses"]
        gf = x["goalsfor"]
        ga = x["goalsagainst"]
        gd = str(x["goaldifference"]).rjust(2)
        p = str(x["points"]).rjust(2)
        nums += 1
        print(f"| {nums} | {c} | {w} | {d} | {L} | {gf}  |"
              f" {ga}  | {gd} | {p} |")
    print("-" * 50)


add_game('CostaRica', 0, 'Serbia', 1)
add_game('Brazil', 1, 'Switzerland', 1)
add_game('Brazil', 2, 'CostaRica', 0)
add_game('Serbia', 1, 'Switzerland', 2)
add_game('Serbia', 0, 'Brazil', 2)
add_game('Switzerland', 2, 'CostaRica', 2)

lst_teams = make_list(teams)
sort_list()
print_tabellist(lst_teams)


# 15.1

# persons = ['Alice', 'Lucas', 'Olivia',
#            'Liam', 'Astrid', 'William']

# persons.sort()
# for x in persons:
#     print(f"[ ] {x}")

# 15.2

# import random

# nums = []
# for x in range(10):
#     nums.append(random.randint(0, 9))

# print("Before sorting: ")
# for x in nums:
#     print(x)
# nums.sort()
# print("After sorting: ")
# for y in nums:
#     print(y)
