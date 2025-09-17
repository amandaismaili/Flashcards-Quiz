# python-projt
# A command-line quiz using python
- This is a quiz featuring object oriented programming
- Using this quiz the user can answer questions, review his score, go over the quiz again etc

## Features
- Read each question followed by four options, one of which is the correct answer
- User can see the current streak, best streak and the overall score of the correct answers throughout the quiz
- If mistakes are made, user can request to redo the quiz but using only the questions answered wrong
- User can retake the whole quiz again
- All questions are divided into easy, medium and hard category, therefore the user can request for mini quizes based on difficulty
- The questions are stored into an external JSON file
- Data about each quiz taken is stored into another JSON file (features involved: best streak, score, date and time when quiz was taken)
- There ae three main classes, Card with is used for individual question 'cards', Deck which offers the features of adding, removing and shuffling cards, Play which deals with the game's logic
- There is also a sub class for Deck, WrongQuest, which inherits from Deck the methods which will be used for the deck of wrong questions

## Requirements
- python 3
- no external libraries (this program already uses datetime, re , json)

## How to run
- Download or clone the respiratory
- Make sure you use python ver 3
- Run: bash python todolsit.py