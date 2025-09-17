import random
from inputimeout import inputimeout, TimeoutOccurred
import json
import datetime

def main():
    print('---Welcome to our quiz game---')
    what = input('Do you wish to play? (y/n): ')
    if what == 'y':
        print('Please answer the questions using what you already know. Keep in mind you have 8 seconds to answer for each question!')
        begin()
    else:
        print('Thank you for your time!')
    
quiz_data = []

class Card:
    def __init__(self, question, answer, options, category):
        self.question = question
        self.answer = answer
        self.options = options
        self.category = category

    def shuffle(self):
        random.shuffle(self.options)

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, flashcard):
        self.cards.append(flashcard)

    def remove_flashcard(self, flashcard):
        self.cards.remove(flashcard)

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        return iter(self.cards) #to iterate through cards
    
class WrongQuest(Deck):
    def __init__(self):
        super().__init__()
        self.wrong_quest = []

    def shuffle(self):
        super().shuffle()

class Play:
    def __init__(self, deck, wrong_deck):
        self.deck = deck
        self.wrong_deck = wrong_deck
        self.score = 0
        self.streak = 0
        self.best_streak = 0

    def play(self):
        self.score = 0
        self.wrong_deck.wrong_quest.clear()
        for card in self.deck.cards:
            card.shuffle()
            print(f'Q: {card.question}')
            for n, opt in enumerate(card.options):
                print(f'{n + 1}. {opt}')
            try: 
                user_answer = inputimeout(prompt = 'Your answer: ', timeout=8)
                if user_answer.lower().strip() == card.answer.lower().strip():
                    print('You are correct!')
                    self.score += 1
                    self.streak += 1
                    self.best_streak = max(self.best_streak, self.streak)
                    print(f'Current streak: {self.streak}')
                else:
                    print('This is not the right choice.')
                    self.wrong_deck.wrong_quest.append(card)
                    self.streak = 0
            except TimeoutOccurred:
                print('!! Time is out !!')
                self.wrong_deck.wrong_quest.append(card)
                self.streak = 0
        print('>-------------------<')
        print(f'Your final score is {self.score}.')
        print('~------~')
        print(f'Your best streak was {self.best_streak}.')
        print('>-------------------<')

        quiz_data.append({'right_questions': self.score, 'best_streak': self.best_streak, 'date': str(datetime.datetime.now())})

deck = Deck()
wrong = WrongQuest()

with open('/workspaces/python-projt/questions.json', 'r') as file:
    data = json.load(file)

questions = [Card(item['question'], item['answer'], item['options'], item['category']) for item in data]

for question in questions:
    deck.add_card(question)

game = Play(deck, wrong)

def category_deck(category):
    deck = Deck()
    for card in questions:
        if card.category.lower() == category.lower():
            deck.add_card(card)
    return deck

def begin():
    while True:
        mode = input('Do you want to play the questions of a specific category or all? (easy/medium/hard/all) ').lower().strip()
        if mode not in ['easy', 'medium', 'hard', 'all']:
            print('Please choose a valid option.')
        elif mode == 'all':
            current_deck = deck
        else:
            current_deck = category_deck(mode)

        game = Play(current_deck, wrong)
        game.play()

        again = input('Do you want to play again? (y/n) ').lower().strip()
        if again == 'y':
            which = input('Start over or focus on the wrong ones(over/wrong): ').lower().strip()
            if which == 'over':
                wrong.wrong_quest.clear()
                current_deck.shuffle()
                for card in questions:
                    card.shuffle()
            elif which == 'wrong':
                try_again(wrong)
            else:
                print('Write a valid category.')
        else:
            break

def try_again(wrong_deck):
    wrong_deck.cards = list(wrong_deck.wrong_quest)
    secgame = Play(wrong_deck, wrong_deck)
    while True: 
        secgame.play()
        again = input('Play wrong ones again? (y/n): ').lower().strip()
        if again != 'y':
            return

if __name__ == '__main__':
    main()
    with open('/workspaces/python-projt/quizdata.json', 'w') as file:
        json.dump(quiz_data, file, indent=4)