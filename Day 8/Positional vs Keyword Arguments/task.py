# Functions with input

#def greet_with_name(firstname,secondname):
   # print(f"Hello {firstname} {secondname}")
    #print(f"How do you do {firstname} {secondname}?")


#greet_with_name(firstname="Divas", secondname="sharma")


def calculate_love_score(boyfriendName, girlfriendName):
    couples = (boyfriendName + girlfriendName).lower()
    true_count = sum(couples.count(ch) for ch in "true")
    love_count = sum(couples.count(ch) for ch in "love")
    love_score = int(str(true_count) + str(love_count))
    print(love_score)

# example call (keep or remove depending on how the grader runs your file)
calculate_love_score('Divas', 'aneet')




