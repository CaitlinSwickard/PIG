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

# set up an "input" to enter the num of players 2-4
# while true -break put if input is a valid number
# check to make sure it is a valid number .isdigit/int

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




