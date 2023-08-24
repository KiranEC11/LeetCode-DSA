"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

"""

def minion_game(string):
    # your code goes here
    vowels = ['A','E','I','O','U']
    # vowels_kevin = [item for item in string if item in vowels]
    # consonents_stuart = [item for item in string if item not in vowels]
    
    kevin_points=0
    stuart_points = 0
    for i in range(1,len(string)+1):
        letter = string[-i]
        if letter in vowels:
            kevin_points+=i
        else:
            stuart_points+=i
    
    if kevin_points>stuart_points:
        print(f'Kevin {kevin_points}')
    elif stuart_points>kevin_points:
        print(f'Stuart {stuart_points}')
    else:
        print('Draw')