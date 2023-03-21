#flascards game

import json
import random

try:
    with open('flashcards.json', 'r') as f:
        cards = json.load(f)
except FileNotFoundError:
    cards = {"Hello" : "Bonjour", "Thanks" : "Merci" }


# Prompt the user to enter a question and answer for the flashcard

#print("Welcome to the Flascards game!")
#print("Do you want to enter a new flashcard (1) or play with your cards (2)? (tap q to quit)")

#trouver comment inserer un fichier txt dans lequel ajouter les flashcards

#ajouter une carte
def new_card():
    while True:
        question = input("Enter the recto of your card (tap 'q' to quit) : ")
        if question == 'q':
            return card_menu()
        if question != 'q':
            answer = input("Enter the verso of your card : ")
            cards[question] = answer
            save_card()
            print("New card added")

def save_card():
    with open('flashcards.json', 'w') as f:
        json.dump(cards, f)
        #revoir ces commandes
        
#delete a card
def delete_card():
    while True:
        key_to_delete = input("Enter the question of the card you want to delete (tap r for return) : ")
        if key_to_delete == "r":
            return card_menu()
        if key_to_delete in cards.keys():
            del cards[key_to_delete]
            save_card()
            print("Card is deleted.")
        else:
            print("Card not found.")
#normally this loops until the user tap "r"

#display cards?
def display_cards():
    while True:
        all_cards = list(cards.items())
        print("Here are all your cards : " + str(all_cards)) #add the str bc we can concatenate lst 
        return card_menu()

def modify_card(): #fonctionne
    while True:
            select_card = input("Please enter the recto of the card you want to modify (or r to return) : ")
            if select_card == "r":
                return card_menu()
            if select_card in cards.keys():
                change_card = input("Do you want to modify the recto, the verso or both ? (r, v, b or q to quit)")
                if change_card == "q":
                    return card_menu()
                elif change_card == "r":
                    recto = input("Enter the new recto of your card (or q to quit) : ")
                    if recto == "q":
                        return select_card
                    else: 
                        cards[recto] = cards.pop(select_card)
                        save_card()
                        return modify_card()
                elif change_card == "v":
                    verso = input("Enter the new verso of your card (or q to quit) : ")
                    if verso == "q":
                        return select_card
                    else:
                        cards[select_card] = verso #fonctionne
                        save_card()
                        return modify_card()
                elif change_card == "b":
                    recto1 = input("Enter the new recto of your card : ")
                    verso1 = input("Enter the new verso of your card (or q to quit) : ")
                    if verso1 == "q":
                        return select_card
                    else:
                        cards[recto1] = cards.pop(select_card)
                        cards[recto1] = verso1
                        save_card()
                        return modify_card()
                    
def play_cards(): #semble fonctionner. Attention à ne pas avoir "cards" vide.
    while True: 
        enter_game =input("Do you want to play the Flashcards Game? (y/n) : ")
        if enter_game == "n":
            return main_menu()
        if enter_game == "y":
            while True:
                keys = list(cards.keys())
                random_recto = random.choice(keys)
                print("Recto : " + str(random_recto))
                answer = input("Do you know the answer? If you're ready to see the answer, press 'enter' : ")
                if answer != "q":
                    print("Verso : " + str(cards[random_recto]))
                    again = input("Press 'enter' to show a new card.")
                if answer == "q":
                    return play_cards()
        
          
    
#menu carte
def card_menu():
    while True:
        entering = input("Do you want to : \n c: create a card \n d : delete a previous card \n m : modify a card \n s : show all your cards? (tap q to quit) : ")
        if entering == "q":
            return main_menu()
        if entering == "c":
            return new_card()
        if entering == "d":
            return delete_card()
        if entering == "m":
            return modify_card()
        if entering == "s":
            return display_cards()
        

        
def main_menu():
    while True:
        welcome = input("Welcome to the Flashcard Game! Are you ready to play or do you want to access the card menu? (press p to play, m to access the menu) : ")
        if welcome == "p":
            return play_cards()
        if welcome == "m":
            return card_menu()
        else:
            print("See you soon!")
            break

        

#print(card_menu())

#print(play_cards())

print(main_menu())


#main menu should display : card menu (display all cards, create, delete, modify a card), playing mode, leaving the game