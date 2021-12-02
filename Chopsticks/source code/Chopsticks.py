#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) Jordan Memphis Leef. All Rights Reserved.
# View the LICENSE.md on GitHub

__all__ = ["__title__", "__version__", "__author__", "__license__", "__copyright__"]
__title__ = "Chopsticks"
__version__ = "1.0"
__author__ = "Jordan Memphis Leef"
__license__ = "Freeware"
__copyright__ = "Copyright (C) Jordan Memphis Leef"

from colorama import Fore, Style
import random
import msvcrt
import ctypes
import time
import sys
import os

def clear_screen(time_set: int = 1) -> None:
    """Clear the screen."""
    time.sleep(time_set)
    os.system('cls')

def reverse_hand(hand: list) -> list:
    return [[j[::-1] for j in i] for i in hand]

def how_to_play() -> None:
    """The rule book for the game."""
    clear_screen(0)
    print("Gameplay")
    print("Each player starts with two hands with one finger on each. The player can attack the opponent's hand with the amount of fingers they have on the hand the player is attacking with, or split the hand to move")
    print("fingers from one hand to another or to resurrect an empty or 'dead' hand.")
    print("The goal of the game is to remove all of the opponent's hand before they remove yours.\n")
    print("Rules")
    print("1. When attacking, you must use the total fingers of that hand.")
    print("2. When receiving, you must add the total amount of fingers to your hand. If it is equal to or greater than five, it is removed.")
    print("3. When splitting, you cannot move fingers to another of your hands if it is equal to or greater than five. You cannot move the same amount of fingers into an empty hand.")
    print("\nPress any key to continue...")
    msvcrt.getch()

# Global constant declaration
PY_VER = "3.8.3" # The version of Python used to code the program
SW_MAXIMISE = 3 # Set the command prompt to open in maximized window
EMPTY_HAND = ["                      "] * 14 # Set the empty hand
BOT_LFT_HAND = {0: EMPTY_HAND, 1:
            [["                      "],
             ["               ▄▄     "],
             ["              █  █    "],
             ["              █  █    "],
             ["         ▄▄▄▀▀█  █    "],
             ["     ▄▀▀█  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  ▀      █   "],
             ["     █            █   "],
             ["     █            █   "],             
             ["     █            █   "],
             ["      █          █    "],
             ["       █        █     "],
             ["       ▀▀▀▀▀▀▀▀▀▀     "]], 2:

            [["            ▄▄        "],
             ["           █  █▄▄     "],
             ["           █  █  █    "],
             ["           █  █  █    "],
             ["         ▄▄█  █  █    "],
             ["     ▄▀▀█  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  ▀      █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["      █          █    "],
             ["       █        █     "],
             ["       ▀▀▀▀▀▀▀▀▀▀     "]], 3:

            [["            ▄▄        "],
             ["         ▄▄█  █▄▄     "],
             ["        █  █  █  █    "],
             ["        █  █  █  █    "],
             ["        █  █  █  █    "],
             ["     ▄▀▀█  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  ▀      █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["      █          █    "],
             ["       █        █     "],
             ["       ▀▀▀▀▀▀▀▀▀▀     "]], 4:

            [["            ▄▄        "],
             ["         ▄▄█  █▄▄     "],
             ["        █  █  █  █    "],
             ["      ▄▄█  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  ▀      █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["      █          █    "],
             ["       █        █     "],
             ["       ▀▀▀▀▀▀▀▀▀▀     "]], 5:

            [["            ▄▄        "],
             ["         ▄▄█  █▄▄     "],
             ["        █  █  █  █    "],
             ["      ▄▄█  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █ ▄▄▄"],
             ["     █  █  ▀     █▀  █"],
             ["     █              █ "],
             ["     █             █  "],
             ["     █            █   "],
             ["      █          █    "],
             ["       █        █     "],
             ["       ▀▀▀▀▀▀▀▀▀▀     "]]} # Set bottom left hand
TOP_LFT_HAND = {0: EMPTY_HAND, 1:
            [["       ▄▄▄▄▄▄▄▄▄▄     "],
             ["       █        █     "],
             ["      █          █    "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █  █  ▄      █   "],
             ["     █  █  █  █  █    "],
             ["     ▀▄▄█  █  █  █    "],
             ["         ▀▀▀▄▄█  █    "],
             ["              █  █    "],
             ["              █  █    "],
             ["               ▀▀     "],
             ["                      "]], 2:

            [["       ▄▄▄▄▄▄▄▄▄▄     "],
             ["       █        █     "],
             ["      █          █    "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █  █  ▄      █   "],
             ["     █  █  █  █  █    "],
             ["     ▀▄▄█  █  █  █    "],
             ["         ▀▀█  █  █    "],
             ["           █  █  █    "],
             ["           █  █  █    "],
             ["           █  █▀▀     "],
             ["            ▀▀        "]], 3:

            [["       ▄▄▄▄▄▄▄▄▄▄     "],
             ["       █        █     "],
             ["      █          █    "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █  █  ▄      █   "],
             ["     █  █  █  █  █    "],
             ["     ▀▄▄█  █  █  █    "],
             ["        █  █  █  █    "],
             ["        █  █  █  █    "],
             ["        █  █  █  █    "],
             ["         ▀▀█  █▀▀     "],
	     ["            ▀▀        "]], 4:

            [["       ▄▄▄▄▄▄▄▄▄▄     "],
             ["       █        █     "],
             ["      █          █    "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █            █   "],
             ["     █  █  ▄      █   "],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     ▀▄▄█  █  █  █    "],
             ["        █  █  █  █    "],
             ["         ▀▀█  █▀▀     "],
	     ["            ▀▀        "]], 5:

            [
             ["       ▄▄▄▄▄▄▄▄▄▄     "],
             ["       █        █     "],
             ["      █          █    "],
             ["     █            █   "],
             ["     █             █  "],
             ["     █              █ "],
             ["     █  █  ▄     █▄  █"],
             ["     █  █  █  █  █ ▀▀▀"],
             ["     █  █  █  █  █    "],
             ["     █  █  █  █  █    "],
             ["     ▀▄▄█  █  █  █    "],
             ["        █  █  █  █    "],
             ["         ▀▀█  █▀▀     "],
	     ["            ▀▀        "]]} # Set top left hand
BOT_RGT_HAND = {0: EMPTY_HAND, 1: reverse_hand(BOT_LFT_HAND[1]), 2: reverse_hand(BOT_LFT_HAND[2]), 3: reverse_hand(BOT_LFT_HAND[3]), 4: reverse_hand(BOT_LFT_HAND[4]), 5: reverse_hand(BOT_LFT_HAND[5])} # Set bottom right hand
TOP_RGT_HAND = {0: EMPTY_HAND, 1: reverse_hand(TOP_LFT_HAND[1]), 2: reverse_hand(TOP_LFT_HAND[2]), 3: reverse_hand(TOP_LFT_HAND[3]), 4: reverse_hand(TOP_LFT_HAND[4]), 5: reverse_hand(TOP_LFT_HAND[5])} # Set top right hand

# Global variable declaration
player_hand = None
player_action = None
enemy_hand = None
amount = None

class Player:
    def __init__(self) -> None:
        self.name = None
        self.hand = {'left_hand': 1, 'right_hand': 1}

    def display_hands(self, vertical_pos: str, spacing: int = 9) -> None:
        """Displays the player's hands."""
        separator = " "*spacing
        hands = []

        # Set vertical positioning for the hands
        while not hands:
            if vertical_pos == 'top':
                for left_hand, right_hand in zip(TOP_LFT_HAND[self.hand['left_hand']], TOP_RGT_HAND[self.hand['right_hand']]):
                    hands.append("".join(left_hand) + separator + "".join(right_hand))
            elif vertical_pos == 'bottom':
                for left_hand, right_hand in zip(BOT_LFT_HAND[self.hand['left_hand']], BOT_RGT_HAND[self.hand['right_hand']]):
                    hands.append("".join(left_hand) + separator + "".join(right_hand))

            # Display the hands         
            for i in hands:
                print("".join(i))

    def reset_hands(self) -> None:
        self.hand = {'left_hand': 1, 'right_hand': 1}

class Game:
    def __init__(self) -> None:
        self.game_mode = None
        self.players = []
        self.player1 = None
        self.player2 = None
        self.is_computer_player = False
        self.winner = None

    def set_game_mode(self) -> None:
        """Set the game mode."""
        while not self.game_mode:
            clear_screen(0)

            try:
                print(f"{Style.BRIGHT}{__title__} v{__version__}\nWritten in Python {PY_VER}\nDeveloped by {__author__}\n\n[1] Play vs computer\n[2] Play vs human\n[3] Watch computer play each other\n[4] How to play\n[5] Exit")
                user_input = int(input("\nSelection: "))

                if user_input == 1:
                    self.game_mode = 'singleplayer'
                elif user_input == 2:
                    self.game_mode = 'multiplayer'
                elif user_input == 3:
                    self.game_mode = 'zero_player'
                elif user_input == 4:
                    how_to_play()
                elif user_input == 5:
                    sys.exit(0)
                else:
                    clear_screen(0)
                    print(f"{__title__} v{__version__}\nWritten in Python {PY_VER}\nDeveloped by {__author__}\n\n[1] Play vs computer\n[2] Play vs human\n[3] Watch computer play each other\n[4] How to play\n[5] Exit\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                    clear_screen(0.5)
                    self.set_game_mode()
            except ValueError:
                clear_screen(0)
                print(f"{__title__} v{__version__}\nWritten in Python {PY_VER}\nDeveloped by {__author__}\n\n[1] Play vs computer\n[2] Play vs human\n[3] Watch computer play each other\n[4] How to play\n[5] Exit\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                clear_screen(0.5)
                self.set_game_mode()

    def get_players(self) -> None:
        """Get a list of players."""
        clear_screen(0)
        player1 = Player()
        player2 = Player()

        if self.game_mode != 'zero_player':
            player1.name = input("Player 1 Name: ")
            self.players.append({'human': player1})
        else:
            player1.name = "Computer 1"
            player2.name = "Computer 2"
            self.players.append({'computer': player1})
            self.players.append({'computer': player2})
        
        if self.game_mode == 'singleplayer':
            player2.name = "Computer"
            self.players.append({'computer': player2})

        elif self.game_mode == 'multiplayer':
            clear_screen(0)
            player2.name = input("Player 2 Name: ")
            self.players.append({'human': player2})

    def display_game(self) -> None:
        """Display the game."""
        clear_screen(0)
        print(f"                      {self.player2.name}                      ")
        print(f"            {self.player2.hand['left_hand']}                            {self.player2.hand['right_hand']}           ")
        self.player2.display_hands('top')
        self.player1.display_hands('bottom')
        print(f"            {self.player1.hand['left_hand']}                            {self.player1.hand['right_hand']}           ")
        print(f"                      {self.player1.name}                      ")

    def turn_handler(self, action: str = "select_hand") -> None:
        """Handle the turns for each player."""
        global player_hand, enemy_hand, player_action, amount
        self.display_game()

        if action == "select_hand":
            try:
                if self.is_computer_player:
                    if self.player1.hand['left_hand'] > 0 and self.player1.hand['right_hand'] > 0:
                        player_hand = random.randint(1, 2)
                    elif self.player1.hand['left_hand'] > 0:
                        player_hand = 1
                    elif self.player1.hand['right_hand'] > 0:
                        player_hand = 2
                else:
                    player_hand = int(input(f"\n{self.player1.name}'s Turn\n\nSelect your hand [1] Left [2] Right\n\nSelection: "))

                if player_hand == 1:
                    if self.player1.hand['left_hand'] > 0:
                        self.turn_handler("select_action")
                    else:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nSelect your hand [1] Left [2] Right\n\nSelection: {Fore.RED}Cannot choose empty hand!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler()
                elif  player_hand == 2:
                    if self.player1.hand['right_hand'] > 0:
                        self.turn_handler("select_action")
                    else:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nSelect your hand [1] Left [2] Right\n\nSelection: {Fore.RED}Cannot choose empty hand!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler()
                else:
                    self.display_game()
                    print(f"\n{self.player1.name}'s Turn\n\nSelect your hand [1] Left [2] Right\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                    clear_screen(0.5)
                    self.turn_handler()
            except ValueError:
                self.display_game()
                print(f"\n{self.player1.name}'s Turn\n\nSelect your hand [1] Left [2] Right\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                clear_screen(0.5)
                self.turn_handler()

        elif action == "select_action":
            self.display_game()

            try:
                if self.is_computer_player:
                    if self.player1.hand['left_hand'] == 4 and self.player1.hand['right_hand'] == 4 or self.player1.hand['left_hand'] == 1 and self.player1.hand['right_hand'] == 0 or self.player1.hand['left_hand'] == 0 and self.player1.hand['right_hand'] == 1:
                        player_action = 1
                    elif self.player1.hand['left_hand'] >= 1 and self.player1.hand['right_hand'] == 4:
                        player_action = 1
                    elif self.player1.hand['right_hand'] >= 1 and self.player1.hand['left_hand'] == 4:
                        player_action = 1
                    elif self.player1.hand['left_hand'] == 4 and self.player1.hand['right_hand'] >= 1:
                        player_action = 1
                    elif self.player1.hand['right_hand'] == 4 and self.player1.hand['left_hand'] >= 1:
                        player_action = 1
                    elif self.player1.hand['left_hand'] >= 1 or self.player1.hand['right_hand'] >= 1:
                        player_action = random.randint(1, 2)

                else:
                    player_action = int(input(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: "))

                if player_action == 1:
                    self.turn_handler("attack")
                elif player_action == 2:
                    self.turn_handler("split")
                else:
                    self.display_game()
                    print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                    clear_screen(0.5)
                    self.turn_handler(action)
            except ValueError:
                self.display_game()
                print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                clear_screen(0.5)
                self.turn_handler(action)

        elif action == "attack":
            try:
                if self.is_computer_player:
                    if self.player2.hand['left_hand'] > 0 and self.player2.hand['right_hand'] > 0:
                        enemy_hand = random.randint(1, 2)
                    elif self.player2.hand['left_hand'] > 0:
                        enemy_hand = 1
                    elif self.player2.hand['right_hand'] > 0:
                        enemy_hand = 2
                else:
                    enemy_hand = int(input(f"\n{self.player1.name}'s Turn\n\nSelect enemy's hand [1] Left [2] Right\n\nSelection: "))

                if player_hand == 1 and enemy_hand == 1:
                    if self.player2.hand['left_hand'] > 0:
                        self.player2.hand['left_hand'] += self.player1.hand['left_hand']

                        if self.player2.hand['left_hand'] >= 5:
                            self.player2.hand['left_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['left_hand'] = 0
                        elif self.player2.hand['right_hand'] >= 5:
                            self.player2.hand['right_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['right_hand'] = 0
                        else:
                            self.display_game()
                            clear_screen(1)
                    else:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nSelect enemy's hand [1] Left [2] Right\n\nSelection: {Fore.RED}Cannot attack empty hand!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler(action)
                elif player_hand == 1 and enemy_hand == 2:
                    if self.player2.hand['right_hand'] > 0:
                        self.player2.hand['right_hand'] += self.player1.hand['left_hand']

                        if self.player2.hand['left_hand'] >= 5:
                            self.player2.hand['left_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['left_hand'] = 0
                        elif self.player2.hand['right_hand'] >= 5:
                            self.player2.hand['right_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['right_hand'] = 0
                        else:
                            self.display_game()
                            clear_screen(1)
                    else:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nSelect enemy's hand [1] Left [2] Right\n\nSelection: {Fore.RED}Cannot attack empty hand!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler(action)
                elif player_hand == 2 and enemy_hand == 1:
                    if self.player2.hand['left_hand'] > 0:
                        self.player2.hand['left_hand'] += self.player1.hand['right_hand']

                        if self.player2.hand['left_hand'] >= 5:
                            self.player2.hand['left_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['left_hand'] = 0
                        elif self.player2.hand['right_hand'] >= 5:
                            self.player2.hand['right_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['right_hand'] = 0
                        else:
                            self.display_game()
                            clear_screen(1)
                    else:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nSelect enemy's hand [1] Left [2] Right\n\nSelection: {Fore.RED}Cannot attack empty hand!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler(action)
                elif player_hand == 2 and enemy_hand == 2:
                    if self.player2.hand['right_hand'] > 0:
                        self.player2.hand['right_hand'] += self.player1.hand['right_hand']

                        if self.player2.hand['left_hand'] >= 5:
                            self.player2.hand['left_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['left_hand'] = 0
                        elif self.player2.hand['right_hand'] >= 5:
                            self.player2.hand['right_hand'] = 5
                            self.display_game()
                            clear_screen(1)
                            self.player2.hand['right_hand'] = 0
                        else:
                            self.display_game()
                            clear_screen(1)
                    else:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nSelect enemy's hand [1] Left [2] Right\n\nSelection: {Fore.RED}Cannot attack empty hand!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler(action)
            except ValueError:
                self.display_game()
                print(f"\n{self.player1.name}'s Turn\n\nSelect enemy's hand [1] Left [2] Right\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                clear_screen(0.5)
                self.turn_handler(action)

        elif action == "split":
            if self.player1.hand['left_hand'] == 4 and self.player1.hand['right_hand'] == 4:
                self.display_game()
                print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: {Fore.RED}Cannot split to create a full hand!{Fore.WHITE}")
                clear_screen(0.5)
                self.turn_handler()
            elif self.player1.hand['left_hand'] == 1 and self.player1.hand['right_hand'] == 0 or self.player1.hand['left_hand'] == 0 and self.player1.hand['right_hand'] == 1:
                self.display_game()
                print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nAmount: {Fore.RED}Cannot transfer one finger into empty hand!{Fore.WHITE}")
                clear_screen(0.5)
                self.turn_handler()
            elif player_hand == 1 and self.player1.hand['right_hand'] <= 4:
                if self.player1.hand['left_hand'] == 1 and self.player1.hand['right_hand'] == 4:
                    self.display_game()
                    print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: {Fore.RED}Cannot split to create a full hand!{Fore.WHITE}")
                    clear_screen(0.5)
                    self.turn_handler()
                else:
                    try:
                        if self.is_computer_player:
                            if self.player1.hand['left_hand'] == 4 and self.player1.hand['right_hand'] == 0:
                                amount = random.randint(1, 3)
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 4 and self.player1.hand['right_hand'] < 3 or self.player1.hand['left_hand'] == 3 and self.player1.hand['right_hand'] >= 0:
                                amount = random.randint(1, 2)
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 4 and (self.player1.hand['right_hand'] == 3 or self.player1.hand['right_hand'] == 2):
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 1 and self.player1.hand['right_hand'] == 2:
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 2 and self.player1.hand['right_hand'] == 1:
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 2 and self.player1.hand['right_hand'] == 0 or self.player1.hand['left_hand'] == self.player1.hand['right_hand'] == 1:
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                        else:
                            amount = int(input(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: "))

                        if amount == self.player1.hand['left_hand'] == 1 and self.player1.hand['right_hand'] == 4:
                            self.display_game()
                            print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Cannot split to create a full hand!{Fore.WHITE}")
                            clear_screen(0.5)
                            self.turn_handler()
                        elif self.player1.hand['left_hand'] == 4 and self.player1.hand['right_hand'] == 0:
                            if 0 < amount < 4:
                                self.player1.hand['right_hand'] += amount
                                self.player1.hand['left_hand'] -= amount
                                self.display_game()
                                clear_screen(1)
                            else:
                                self.display_game()
                                print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                                clear_screen(0.5)
                                self.turn_handler(action)
                        elif self.player1.hand['left_hand'] == 3 and self.player1.hand['right_hand'] == 0:
                            if 0 < amount < 3:
                                self.player1.hand['right_hand'] += amount
                                self.player1.hand['left_hand'] -= amount
                                self.display_game()
                                clear_screen(1)
                            else:
                                self.display_game()
                                print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                                clear_screen(0.5)
                                self.turn_handler(action)
                        elif self.player1.hand['left_hand'] == 2 and self.player1.hand['right_hand'] == 0:
                            if 0 < amount < 2:
                                self.player1.hand['right_hand'] += amount
                                self.player1.hand['left_hand'] -= amount
                                self.display_game()
                                clear_screen(1)
                            else:
                                self.display_game()
                                print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                                clear_screen(0.5)
                                self.turn_handler(action)
                        elif amount == self.player1.hand['left_hand'] == 4:
                            self.display_game()
                            print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Cannot split to create a full hand!{Fore.WHITE}")
                            clear_screen(0.5)
                            self.turn_handler()
                        elif 0 < amount <= self.player1.hand['left_hand'] < 4:
                            self.player1.hand['right_hand'] += amount
                            self.player1.hand['left_hand'] -= amount
                            self.display_game()
                            clear_screen(1)
                        else:
                            self.display_game()
                            print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                            clear_screen(0.5)
                            self.turn_handler(action)
                    except ValueError:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler(action)
            elif player_hand == 2 and self.player1.hand['left_hand'] <= 4:
                if self.player1.hand['right_hand'] == 1 and self.player1.hand['left_hand'] == 4:
                    self.display_game()
                    print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: {Fore.RED}Cannot Split to create a full hand!{Fore.WHITE}")
                    clear_screen(0.5)
                    self.turn_handler()
                else:
                    try:
                        if self.is_computer_player:
                            if self.player1.hand['left_hand'] == 0 and self.player1.hand['right_hand'] == 4:
                                amount = random.randint(1, 3)
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['right_hand'] == 4 and self.player1.hand['left_hand'] < 3 or self.player1.hand['right_hand'] == 3 and self.player1.hand['left_hand'] >= 0:
                                amount = random.randint(1, 2)
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['right_hand'] == 4 and (self.player1.hand['left_hand'] == 3 or self.player1.hand['left_hand'] == 2):
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 2 and self.player1.hand['right_hand'] == 1:
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 1 and self.player1.hand['right_hand'] == 2:
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                            elif self.player1.hand['left_hand'] == 0 and self.player1.hand['right_hand'] == 2 or self.player1.hand['left_hand'] == self.player1.hand['right_hand'] == 1:
                                amount = 1
                                self.display_game()
                                clear_screen(1)
                        else:
                            amount = int(input(f"\n{self.player1.name}'s Turn\n\nTransferring to right hand\n\nAmount: "))

                        if amount == self.player1.hand['right_hand'] == 1 and self.player1.hand['left_hand'] == 4:
                            self.display_game()
                            print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Cannot split to create a full hand!{Fore.WHITE}")
                            clear_screen(0.5)
                            self.turn_handler()
                        elif self.player1.hand['right_hand'] == 4 and self.player1.hand['left_hand'] == 0:
                            if 0 < amount < 4:
                                self.player1.hand['left_hand'] += amount
                                self.player1.hand['right_hand'] -= amount
                                self.display_game()
                                clear_screen(1)
                            else:
                                self.display_game()
                                print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                                clear_screen(0.5)
                                self.turn_handler(action)
                        elif self.player1.hand['right_hand'] == 3 and self.player1.hand['left_hand'] == 0:
                            if 0 < amount < 3:
                                self.player1.hand['left_hand'] += amount
                                self.player1.hand['right_hand'] -= amount
                                self.display_game()
                                clear_screen(1)
                            else:
                                self.display_game()
                                print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                                clear_screen(0.5)
                                self.turn_handler(action)
                        elif self.player1.hand['right_hand'] == 2 and self.player1.hand['left_hand'] == 0:
                            if 0 < amount < 2:
                                self.player1.hand['left_hand'] += amount
                                self.player1.hand['right_hand'] -= amount
                                self.display_game()
                                clear_screen(1)
                            else:
                                self.display_game()
                                print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                                clear_screen(0.5)
                                self.turn_handler(action)
                        elif amount == self.player1.hand['right_hand'] == 4:
                            self.display_game()
                            print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Cannot split to create a full hand!{Fore.WHITE}")
                            clear_screen(0.5)
                            self.turn_handler()
                        elif 0 < amount <= self.player1.hand['right_hand'] < 4:
                            self.player1.hand['left_hand'] += amount
                            self.player1.hand['right_hand'] -= amount
                            self.display_game()
                            clear_screen(1)
                        else:
                            self.display_game()
                            print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                            clear_screen(0.5)
                            self.turn_handler(action)
                    except ValueError:
                        self.display_game()
                        print(f"\n{self.player1.name}'s Turn\n\nTransferring to left hand\n\nAmount: {Fore.RED}Invalid Amount!{Fore.WHITE}")
                        clear_screen(0.5)
                        self.turn_handler(action)
            else:
                self.display_game()
                print(f"\n{self.player1.name}'s Turn\n\nAction [1] Attack [2] Split\n\nSelection: {Fore.RED}Cannot split into empty hand!{Fore.WHITE}")
                clear_screen(0.5)
                self.turn_handler()

    def end_game(self) -> None:
        """End the game."""
        self.display_game()
        print(f"{Fore.GREEN}\n{self.winner} Wins!{Fore.WHITE}")

        try:
            user_input = int(input("Play again?\n[1] Yes\n[2] No\n\nSelection: "))

            if user_input == 1:
                self.player1.reset_hands()
                self.player2.reset_hands()
                self.players.reverse()
                self.run()
            elif user_input == 2:
                clear_screen(1)
                main()
            else:
                self.display_game()
                print(f"{Fore.GREEN}\n{self.winner} Wins!{Fore.WHITE}")
                print(f"Play again?\n[1] Yes\n[2] No\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
                clear_screen(0.5)
                self.end_game()
        except ValueError:
            self.display_game()
            print(f"{Fore.GREEN}\n{self.winner} Wins!{Fore.WHITE}")
            print(f"Play again?\n[1] Yes\n[2] No\n\nSelection: {Fore.RED}Invalid Selection!{Fore.WHITE}")
            clear_screen(0.5)
            self.end_game()

    def run(self) -> None:
        """Run the game."""
        while True:           
            for player in self.players:
                for p1, p2 in zip(self.players[self.players.index(player)].items(), self.players[self.players.index(player) - 1].items()):
                    self.player1 = p1[1]
                    self.player2 = p2[1]

                    if p1[0] == 'computer':
                        self.is_computer_player = True
                    else:
                        self.is_computer_player = False

                    if self.player1.hand['left_hand'] == 0 and self.player1.hand['right_hand'] == 0:
                        self.winner = self.player2.name
                        self.end_game()
                    elif self.player2.hand['left_hand'] == 0 and self.player2.hand['right_hand'] == 0:
                        self.winner = self.player1.name
                        self.end_game()

                    self.turn_handler()

def main():
    """The program."""
    # Create title bar
    ctypes.windll.kernel32.SetConsoleTitleW(f"{__title__} v{__version__}")

    # Cause the command prompt to open in maximize window by default
    user32 = ctypes.WinDLL('user32')
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, SW_MAXIMISE)

    # Disable QuickEdit and Insert mode by default
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

    # Start the game
    game = Game()
    game.set_game_mode()
    game.get_players()
    game.run()

if __name__ == '__main__':
    main()