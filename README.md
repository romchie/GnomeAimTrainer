# Gnome Aim Trainer
This is mini point-and-click aim trainer using the gnome meme. The user is given 60 seconds by default, and they have to click the gnome as many times as possible. After each successful click, the gnome will move to a new entirely random spot on the screen. The game tracks your click accuracy on the gnome and gives you a final score upon completion of the game in the terminal (which is once time is up). Note that the hitbox of the gnome is the actual .PNG bounds, not just a rectangle.

### Note
This game uses the [pygame](https://www.pygame.org/docs/) library, so make sure you install it to be able to play the game.

### Help

    optional arguments:
    -h, --help			        show this help message and exit
    -ct, --customtime <value>		give custom runtime where <value> is an integer in seconds
### Examples
Running the game with no optional arguments (runtime defaults to 60 sec)

	python3 main.py

Running the game with a custom time of 30 seconds

    python3 main.py -ct 30

Running the game with a custom time of 2 minutes

    python3 main.py -ct 120
