import random

words_dictionary=['ironman', 'capitanmarvel','loki','thor','spiderman']
def guess_word():
  word=random.choice(words_dictionary)
  return word

word=guess_word()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def greet_user():
  print('Hi this is a hangman game \n')
  name=input('Enter your name :  ' )
  print(f'\nWelcom {name}')  
  start=input('\nSay start to run game:  ')
  if start == 'start' or 'Start' or 'START':
    print('\n**Now Play**\n\n')  
greet_user()    



def play(word):
  list_guesses=[]
  list_words=[]
  tries=6

  while True:
    failed=0
    for letter in word:
      if letter in list_guesses:
        print(letter,end=" ")
        
      else:
        print('-',end="")
        failed+=1  
  #------------------------           
    if failed == 0 or word in list_words :
        print(f'\n\nYou win the game , word is {word}')   
        break
    if tries == 0 :
        print(f'\n\nYou lose the game , word is  {word}')   
        break
  #------------------------ 
    guess=input('Enter a letter or word: ')
    if len(guess) == 0  :
       print('You should write one letter or word:   ')
    else:
       list_guesses.append(guess)   
    if  guess in word:
       print('**Correct**') 
    else:
       print('It\'s not Correct')
       tries-=1 
       print(display_hangman(tries))  
    if len(guess)==len(word):
       list_words.append(guess) 


  #-----------------------   
play(word)
  
    
     


print('\n\nIf you wanna play again say y ?') 

while True:
   answer=input('yes or no: ')
   if answer == 'yes':
      word=guess_word()
      play(word)
   else :
      print('** Good Luck **') 
      break 
