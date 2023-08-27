# WELCOME TO PIG

## Game rules

The objective of Pig is to be the first player to earn 100 points.

This is achieved by rolling the dice (D6) and adding the rolled values.

Players are permitted to roll as many times as they’d like during their turn, but beware of rolling a 1! Doing so will cost you all the points you’ve collected during your turn.

If you’ve racked up the points and don’t want to risk rolling a 1, you may choose to hold and keep the numbers you’ve accumulated during your turn.
It will be up to you to decide if the risk is worth it! Once a player reaches 100 points, the game ends and that player is the winner.

## Requirements and recommendations

- Requires Python version 3.8 or higher
- Functioning keyboard with alphanumeric keys.
- Given that the program uses ASCII art, it is highly recommended running this in a fullscreen terminal.
- Your smart fridge could run this program, so I'm not even gonna list hardware requirements.

## Usage

- Import and use it as follows:

```Python
>>> from pig_JoseEscauriza import main

>>> main()
```

Once running, the player will first be prompted to enter their name.

Afterwards a menu will be displayed, prompting the user to pick from one of its 4 options:

1. ROLL - Rolls the dice, if the dice lands in 1 the turn is forfeit, otherwise the player sees the menu again.

2. HOLD - Player's current score (a.k.a turn score) is passed onto the player's global score, thereby being held safe.

3. VIEW POINTS - Player will see their global score displayed on screen, afterwards the menu is shown again (turn is NOT lost).

4. EXIT - Quit the program.