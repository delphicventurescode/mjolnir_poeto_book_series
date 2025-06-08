import random

# Sample words for each category
nouns = {
    "domo": "domoj",        # house - houses (plural)
    "libro": "libroj",      # book - books
    "kato": "katoj",       # cat - cats
}

verbs = {
    "kuri": "kuris",        # run - ran (past tense)
    "manĝi": "manĝis",     # eat - ate
    "vidi": "vidis",       # see - saw
}

adjectives = {
    "bona": "bonega",       # good - excellent (adjective form, intensified)
    "granda": "grandega",   # big - very big
    "rapida": "rapide",     # quick - quickly (adverb form for fun)
}

def play_game():
    print("Saluton! Bonvenon al la ludo Malsamaj Formoj!")
    print("Vi ricevos bazvorton kaj devos doni ĝian ĝustan formon.")
    print("Por substantivoj, donu la pluralon.")
    print("Por verboj, donu la pasintan tempon.")
    print("Por adjektivoj, donu la plifortigitan formon aŭ adverbon.")
    print("Vi havas 3 provojn por ĉiu vorto.\n")

    score = 0
    rounds = 5

    for _ in range(rounds):
        category = random.choice(["noun", "verb", "adjective"])
        
        if category == "noun":
            word, correct = random.choice(list(nouns.items()))
            print(f"Substantivo: {word}")
            expected = "plural form"
        elif category == "verb":
            word, correct = random.choice(list(verbs.items()))
            print(f"Verbo: {word}")
            expected = "past tense"
        else:
            word, correct = random.choice(list(adjectives.items()))
            print(f"Adjektivo: {word}")
            expected = "plifortigita formo aŭ adverbo"

        tries = 3
        while tries > 0:
            guess = input(f"Doni la {expected}: ").strip().lower()
            if guess == correct:
                print("Bone! Vi ĝuste respondis.\n")
                score += 1
                break
            else:
                tries -= 1
                if tries > 0:
                    print(f"Malsukcesis. Provu denove. Restas {tries} provo(j).")
                else:
                    print(f"Malĝuste. La ĝusta respondo estis: '{correct}'.\n")

    print(f"Ludo finita! Via poentaro: {score} el {rounds}")

if __name__ == "__main__":
    play_game()
