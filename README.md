# PIG
### A Multiplayer Dice Game

## RULES
The goal of the dice game Pig is to be the first player to score 50 points or more. Players take turns rolling a die and adding the total of each roll to their turn total. A player can choose to "hold" at any time, which ends their turn and adds their turn total to their score. However, if a player rolls a 1, their turn ends immediately and they score nothing.

### Project Layout
1. Create a way to roll the dice - random number generator between 1 - 6
2. Ask user if they want to roll again or stop their turn
3. If they stop their turn, add points to total score
4. Constant check on total score of either player to see if score is > 50
5. If score >= 50, stop the game and tell the player they won
