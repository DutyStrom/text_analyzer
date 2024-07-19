"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Boček
email: bocek2@seznam.cz
discord: Seth_Cz#8510
"""

# Registrovaní uživatelé:
#+---------+--------------------+
#|  user   |      password      |
#+---------+--------------------+
#|   bob   |        123         |
#|   ann   |      pass123       |
#|   mike  |    password123     |
#|   liz   |      pass123       |
#+---------+--------------------+

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# import modulů: "sys" - ukončení programu a "string" - řešení interpunkce
import sys
import string

line = "-" * 40   # oddělovací čára
registered_users = {   # dict registrovaných uživatelů
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# vyžádání přihlašovacích údajů od uživatele
username = input("username: ")
password = input("password: ")
print(line)

chck_rgstr = (username, password) in registered_users.items()   # stav registrace uživatele True/False


if not chck_rgstr:   # ukončení programu, pokud není uživatel registrován
    print(
f"""username: {username}
password: {password}
unregistered user, terminating the program..."""
)
    sys.exit()
else:
    print(
f"""Welcome to the app, {username}
We have 3 texts to be analyzed.
{line}"""
)
    try:   # "try" blok, který se provede pokud nenastane ValuError
        choice = int(input("Enter a number btw. 1 and 3 to select: "))   # požadavek na výběr jednoho z TEXTů
        print(line)
        
        if choice not in range(1, 4):   # pokud není volba uživatele v definovaném rozsahu ukončí program
            print(
"""You have to select number btw. 1 and 3!
Terminating the program..."""
)
            sys.exit()
        else:                                  # pokračuje v programu
            text = TEXTS[choice - 1]   # uloží vybraný text z nabídky do variable

            # odstranění interpunkce - Stack Overflow
            table = text.maketrans("", "", string.punctuation)   # překládací tabulka pro "string.translate"
            text_1 = text.translate(table)                       # odstranění interpunkce z textu
        
            text_list = text_1.split()   # vytvoření listu jednotlivých slov z textu bez interpunkce
        
            # variables pro jednotlivá zadání
            number_of_words = len(text_list)    # počet slov
            number_of_title = 0                 # slova začínajících velkým písmenem
            number_of_upper = 0                 # slova jen s velkými písmeny
            number_of_lower = 0                 # slova jen s malými písmeny
            number_of_numerics = 0              # číselné stringy
            sum_of_numerics = 0                 # součet číselných stringů

            # Počítadlo pro jednotlivá zadání
            # prochází "text_list" položku po položce a pokud se shoduje s podmínkou
            # zadání příčte do variables
            for word in text_list:
                if word.istitle():
                    number_of_title += 1
                elif word.isupper():
                    number_of_upper += 1
                elif word.islower():
                    number_of_lower += 1
                elif word.isnumeric():
                    number_of_numerics += 1
                    sum_of_numerics += int(word)

            print(                                                  # výpis výsledků počítadla
f"""There are {number_of_words} words in the selected text.
There are {number_of_title} titlecase words.
There are {number_of_upper} uppercase words.
There are {number_of_lower} lowercase words.
There are {number_of_numerics} numeric strings.
The sum of all the numbers {sum_of_numerics}
{line}"""
)   
            # Sloupcový graf četnosti délek
            length_of_word = [len(word) for word in text_list]   # seznam s délkami jednotlivých slov pro graf

            # hlavička grafu
            print(
f"""{"LEN": >3}|{"OCCURENCES": ^20}|{"NR.": <3}
{line}"""
)        
            # graf
            for i in range(1, max(length_of_word) + 1):
                occ_grph = "*" * length_of_word.count(i)   # "grafické" vyjádření
                nr_grph = length_of_word.count(i)          # číselné vyjádření
                print(f"{str(i): >3}|{occ_grph: <20}|{str(nr_grph): <3}")

    except ValueError:   # "výjimka" - pokud byla zadána jiná hodnota než integer
            print(line)
            print(
"""A number must be selected!
Terminating the program..."""
)
            sys.exit()