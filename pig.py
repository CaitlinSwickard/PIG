# generate random number
import random


# basic roll function
def roll():
  min_val = 1
  max_val = 6
  # random.random integer between 1-6
  roll = random.randint(min_val, max_val)

  return roll
# value = roll()
# print(value)


# input to capture number of players
while True:
  players = input('Enter number of players from 2-4: ')
  # check if input is a num
  if players.isdigit():
    # turn string to int
    players = int(players)
    # check num between 2-4
    if 2 <= players <= 4:
      print("Must be between 2-4 players.")
      break
  else:
    # invalid num try again
    print("invalid number, try again.")
print(players)




# variables
  # max_score
  # player_scores - list of all the scores for players - list comp for unknown size of list

# go through players turns
# while players scores are less than max-score
  # should-roll - input y
  # grab that roll - if that roll = 1 - turn is done
  # else: add the value to players score
# for loop around this while - to get each players index

# max_score exit once all the turn have completed rolls
# exit - with who won




