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
      break
    else:
      print("Must be between 2-4 players.")

  else:
    # invalid num try again
    print("Invalid number, try again.")
# print(players)


max_score = 50
player_scores = [0 for _ in range(players)]


# simulate the turns for the players2
while max(player_scores) < max_score:

  for player_idx in range(players):
    print("\nPlayer number:", player_idx + 1, "turn just started!")
    print("Your total score is:", player_scores[player_idx], "\n")

    current_score = 0

    while True:
      # check if player wants to roll
      should_roll = input("Do you want to roll? Press y: ")
      if should_roll.lower() != 'y':
        break
      value = roll()

      # check if value was a 1
      if value == 1:
        print("You rolled a 1, turn DONE!")
        current_score = 0
        break
      else:
        # add to players score
        current_score += value
        print("You rolled a:", value)
      print("Your score:", current_score)

    # individual players score + the value of current turn
    player_scores[player_idx] += current_score
    print('Your total score is: ', player_scores[player_idx])


# exit game once all the turn have completed rolls and max_score reached
# gives us the index of where the winning score is indexed = which players score that is the
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)