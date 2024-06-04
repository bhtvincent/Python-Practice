# ----------------------------------------------------------------------
# Name:        Game
# Purpose:     Create a game with animation and tkinter
# ----------------------------------------------------------------------
"""
GUI game application with animation in tkinter.

Two-player game with Spartan images. Use the arrow keys to control one
player, and WASD to control the other player. The objective of the game
is to avoid the other player's "trail" that their icon leaves behind,
while remaining in bounds.
"""
import os
import tkinter
import argparse
import sys


class Game:
    """
    Class to support a GUI with animated images.

    Argument:
    parent: (tkinter.Tk) the root window object
    parent: (tkinter.Tk) the root window object
    canvas: (tkinter.Canvas) A Canvas widget defining the race area.
    trail_coordinates: set of traveled coordinates
    game_end: boolean stating game end
    speed: default speed 3
    color: default color green
    go: boolean game running
    """
    player1_left = True
    player1_right = False
    player1_up = False
    player1_down = False

    player2_left = False
    player2_right = True
    player2_up = False
    player2_down = False

    trail_coordinates = set()
    game_end = False

    speed = 3
    color = 'green'

    def __init__(self, parent):
        parent.title('CS 122')
        self.parent = parent
        # create a START button and associate it with the start method
        start_button = tkinter.Button(parent, text='START', width=20,
                                      command=self.start)
        start_button.grid()  # register it with a geometry manager

        self.message = tkinter.Label(parent, text="Score: 0")
        self.message.grid()

        # create a Canvas widget for the animated objects
        self.canvas = tkinter.Canvas(parent, width=800, height=600,
                                     background=self.color)

        self.spartan_image = tkinter.PhotoImage(file='spartan.png')
        self.player1 = self.canvas.create_image(700, 300,
                                                image=self.spartan_image)
        self.player2 = self.canvas.create_image(100, 300,
                                                image=self.spartan_image)
        self.count = 0
        self.canvas.grid()

    def start(self):
        """
        This method is invoked when the user presses the START button.
        The user can press the start button again to restart the game.
        :return: None
        """
        if self.game_end:
            self.restart_program()
        self.update_label()
        self.game_end = False
        self.animate()

    def animate(self):
        """
        Animates the two player objects recursively by calling self.drive
        after every 20 milliseconds
        :return: None
        """
        if not self.game_end:
            self.drive1(self.player1, self.speed)
            self.drive2(self.player2, self.speed)
            self.parent.after(20, self.animate)  # Try again in 1 ms.

    def game_over(self, winner):
        """
        Displays the end screen with the winner and score
        :param winner: player who won
        :return: None
        """
        self.game_end = True
        self.canvas.delete("all")
        self.canvas.create_text(400, 300, font=("Purisa", 40),
                                text="Game Over. {} wins.".format(
                                    winner), fill="black")
        self.canvas.create_text(400, 400, font=("Purisa", 30),
                                text=winner + "'s score was: {}".format(
                                    self.count - 1), fill="black")

    def update_label(self):
        """
        Updates the score board based on how long the game continues
        :return: None
        """
        if not self.game_end:
            self.message.configure(text='Score: {}'.format(self.count))
            self.message.after(1000, self.update_label)
            self.count += 1

    def drive1(self, car, distance):
        """
         Moves player1, leaves a trail behind them, checks collisions,
         and changes direction based on user input
        :param car: player 1
        :param distance: distance traveled each iteration
        :return: None
        """
        x, y = self.canvas.coords(car)
        coordinates = (x, y)
        if coordinates in self.trail_coordinates:
            self.game_over("Player 1")
            self.game_end = True
        self.canvas.create_oval(x-5,y-5,x,y, fill="yellow")

        self.trail_coordinates.add(coordinates)

        if 0 < x < 800 and 0 < y < 600:  # move player 1
            if self.player1_left:
                self.canvas.move(car, -1 * distance, 0)
            elif self.player1_right:
                self.canvas.move(car, 1 * distance, 0)
            elif self.player1_down:
                self.canvas.move(car, 0, 1 * distance)
            elif self.player1_up:
                self.canvas.move(car, 0, distance * -1)
        else:
            self.game_over("Player 1")
            self.game_end = True

    def drive2(self, car, distance):  # move player2
        """
        Moves player2, leaves a trail behind them, checks collisions,
         and changes direction based on user input
        :param car: player2
        :param distance: distance traveled each iteration
        :return: None
        """
        x, y = tuple(self.canvas.coords(car))
        coordinates = (x, y)
        if coordinates in self.trail_coordinates:
            self.game_over("Player 2")
            self.game_end = True
        self.canvas.create_oval(x - 5, y - 5, x, y, fill="blue")

        self.trail_coordinates.add(coordinates)

        if 0 < x < 800 and 0 < y < 600:
            if self.player2_left:
                self.canvas.move(car, -1 * distance, 0)
            elif self.player2_right:
                self.canvas.move(car, 1 * distance, 0)
            elif self.player2_down:
                self.canvas.move(car, 0, 1 * distance)
            elif self.player2_up:
                self.canvas.move(car, 0, distance * -1)
        else:
            self.game_over("Player 2")
            self.game_end = True

    def restart_program(self):
        """Restarts the current program.  Creates a new window with
        the game
        """
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def left_key(self, event):
        """
        Change direction to left for player 1
        :param event: left button clicked
        :return: None
        """
        if not self.player1_right:
            self.remove_direction1()
            self.player1_left = True

    def right_key(self, event):
        """
        Change direction to right for player 1
        :param event: right button clicked
        :return: None
        """
        if not self.player1_left:
            self.remove_direction1()
            self.player1_right = True

    def up_key(self, event):
        """
        Change direction to up for player 1
        :param event: up button clicked
        :return: None
        """
        if not self.player1_down:
            self.remove_direction1()
            self.player1_up = True

    def down_key(self,event):
        """
        Change direction to down for player 1
        :param event: down button clicked
        :return: None
        """
        if not self.player1_up:
            self.remove_direction1()
            self.player1_down = True

    def a_key(self, event):
        """
        Change direction to left for player 2
        :param event: a button clicked
        :return: None
        """
        if not self.player2_right:
            self.remove_direction2()
            self.player2_left = True

    def d_key(self, event):
        """
        Change direction to right for player 2
        :param event: d button clicked
        :return: None
        """
        if not self.player2_left:
            self.remove_direction2()
            self.player2_right = True

    def w_key(self, event):
        """
        Change direction to up for player 2
        :param event: w button clicked
        :return: None
        """
        if not self.player2_down:
            self.remove_direction2()
            self.player2_up = True

    def s_key(self,event):
        """
        Change direction to down for player 2
        :param event: s button clicked
        :return: None
        """
        if not self.player2_up:
            self.remove_direction2()
            self.player2_down = True

    def remove_direction1(self):
        """
        Resets direction for player1
        :return: None
        """
        self.player1_left = False
        self.player1_right = False
        self.player1_up = False
        self.player1_down = False

    def remove_direction2(self):
        """
        Resets direction for player2
        :return: None
        """
        self.player2_left = False
        self.player2_right = False
        self.player2_up = False
        self.player2_down = False


def get_arguments():
    """
    Gets the arguments for speed, color, and verbose.  Default
    values selected if not specified.
    :return: speed,color,verbose
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('speed',
                        help='What speed would you like?',
                        type=int,
                        nargs='?',
                        default=3)
    parser.add_argument('color', help='What background color?',
                        choices=['red', 'pink', 'white', 'green'],
                        nargs='?',
                        default='green')
    parser.add_argument('-v', '--verbose', help='Print details?',
                        action='store_true')
    arguments = parser.parse_args()
    speed = arguments.speed
    color = arguments.color
    verbose = arguments.verbose
    return speed, color, verbose


def main():
    speed, color, verbose = get_arguments()
    if verbose:
        print(f'Starting a game with a speed of {speed} and a background '
              f'color of {color}')
    Game.color = color
    Game.speed = speed
    root = tkinter.Tk()  # create the GUI aplication main window
    race_app = Game(root)  # instantiate our Nascar object
    root.bind('<Left>', race_app.left_key)
    root.bind('<Right>', race_app.right_key)
    root.bind('<Up>', race_app.up_key)
    root.bind('<Down>', race_app.down_key)
    root.bind('<a>', race_app.a_key)
    root.bind('<d>', race_app.d_key)
    root.bind('<w>', race_app.w_key)
    root.bind('<s>', race_app.s_key)

    root.mainloop()  # enter the main event loop and wait


if __name__ == '__main__':
    main()