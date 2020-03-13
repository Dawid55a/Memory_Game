from kivy.app import App
from kivy.uix.screenmanager import *
from kivy.core.window import Window
from kivy.clock import Clock

from random import *

from kivy.uix.widget import Widget

Window.size = (480, 753)

CARDS_LOCATION_CONST = ["t1", "t2", "t3", "t4",
                        "m1", "m2", "m3", "m4",
                        "lm1", "lm2", "lm3", "lm4",
                        "b1", "b2", "b3", "b4"]
CARDS_SYMBOL = ["@", "!", "#", "$", "%", "^", "&", "*"]


class Game(Screen):
    cards_dictionary = {}
    first_card_key = ""
    first_card_value = ""
    second_card_key = ""
    second_card_value = ""
    points = 0

    def create_cards(self):  # method creating new schema for the game

        cards_dic = {}
        cards_location = [x for x in CARDS_LOCATION_CONST]

        for i in range(len(CARDS_SYMBOL)):  # loop randomizing position
            loc1 = choice(cards_location)
            loc2 = choice(cards_location)
            print("1 pętla:", loc1, loc2)
            while loc1 == loc2:  # checking if position is the same
                loc2 = choice(cards_location)
                print("2 pętla:", loc1, loc2)

            cards_dic[loc1] = CARDS_SYMBOL[i]  # assigning values to positions
            cards_dic[loc2] = CARDS_SYMBOL[i]

            cards_location.remove(loc1)  # removing from temporary list
            cards_location.remove(loc2)

            print(cards_location)
        print(cards_dic)

        for card in cards_dic.keys():  # reset cards
            self.ids[card].disabled = False
            self.ids[card].background_color = [1, 0.5, 0.3, 1]
            print(card, "is set to --> ", cards_dic[card])  # debugging log

        print("passed all")  # debugging log
        print(cards_location)
        print(CARDS_LOCATION_CONST)

        self.cards_dictionary = cards_dic  # passing dictionary to class
        self.first_card_key = ""  # reset card
        self.first_card_value = ""
        self.second_card_key = ""
        self.second_card_value = ""

    def show_card(self, card):  # showing card symbol
        if self.first_card_value == "":  # if first card is not chosen

            self.first_card_value = self.cards_dictionary[card]
            self.first_card_key = card

            self.ids[card].text = self.cards_dictionary[card]
            self.ids[card].background_color = [0.2, 0.8, 0.2, 1]
            self.ids[card].disabled = True

            print("First card is chosen: ", card)

        elif self.second_card_value == "":  # if first card is chosen
            self.second_card_value = self.cards_dictionary[card]
            self.second_card_key = card

            self.ids[card].text = self.cards_dictionary[card]
            self.ids[card].background_color = [0.2, 0.8, 0.2, 1]
            self.ids[card].disabled = True

            print("Second card is chosen: ", card)

            print(card)

            Clock.schedule_once(lambda dt: Game.check(self, card), 1)

    def check(self, card):
        print(card)
        if self.first_card_value == self.cards_dictionary[card]:  # if second card is the same
            self.points += 1

            self.ids[card].text = ""
            self.ids[self.first_card_key].text = ""
            self.ids[card].background_color = [0, 0, 0, 0.8]
            self.ids[self.first_card_key].background_color = [0, 0, 0, 0.8]
            self.ids[card].disabled = True
            self.ids[self.first_card_key].disabled = True

            self.first_card_key = ""
            self.first_card_value = ""
            self.second_card_key = ""
            self.second_card_value = ""

            print("Good ")

            Clock.schedule_once(lambda dt: Game.winn(self), 0.5)

        elif self.first_card_value != card:  # if second card is different

            self.ids[self.first_card_key].text = ""
            self.ids[self.first_card_key].disabled = False
            self.ids[self.first_card_key].background_color = [1, 0.5, 0.3, 1]

            self.ids[card].text = ""
            self.ids[card].disabled = False
            self.ids[card].background_color = [1, 0.5, 0.3, 1]

            self.first_card_value = ""
            self.first_card_key = ""
            self.second_card_key = ""
            self.second_card_value = ""

            print("Wrong ")

    def winn(self):
        found = 0
        for loc in CARDS_LOCATION_CONST:
            if self.ids[loc].disabled == True:
                found += 1
            if found == 2:
                self.add_widget(Winn())

        print("Founded pairs: ", found)


class Winn(Widget):
    pass


# code for different sizes (too lazy aaaand don't work ¯\_(ツ)_/¯)
#    def get_id(self, card):
#        for id, widget in card.parent.ids.items():
#            if widget.__self__ == card:
#                return id
root = None


class SettingsScreen(Screen):
    def set_color(self, colorpicker):
        print("Chosen color: ", colorpicker.color)
        # print(Game.ids["main"].background_color)
        # print(Game.ids.items())
        # Game.ids["t1"].background_color = self.ids["colorpicker"].color
        # print(root.ids["t1"])

    pass


class GameApp(App):

    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(Game(name="Game"))
        sm.add_widget(SettingsScreen(name="Settings"))
        return sm

    # trying to init building the game
    # def on_start(self):
    #     cards_dic = {}
    #     cards_location = [x for x in CARDS_LOCATION_CONST]
    #
    #     for i in range(len(CARDS_SYMBOL)):  # loop randomizing position
    #         loc1 = choice(cards_location)
    #         loc2 = choice(cards_location)
    #         print("1 pętla:", loc1, loc2)
    #         while loc1 == loc2:  # checking if position is the same
    #             loc2 = choice(cards_location)
    #             print("2 pętla:", loc1, loc2)
    #
    #         cards_dic[loc1] = CARDS_SYMBOL[i]  # assigning values to positions
    #         cards_dic[loc2] = CARDS_SYMBOL[i]
    #
    #         cards_location.remove(loc1)  # removing from temporary list
    #         cards_location.remove(loc2)
    #
    #         print(cards_location)
    #     print(cards_dic)
    #
    #     # for card in cards_dic.keys():  # reset cards
    #     #     Game.ids[card].disabled = False
    #     #     Game.ids[card].background_color = [1, 0.5, 0.3, 1]
    #     #     print(card, "is set to --> ", cards_dic[card])  # debugging log
    #
    #     print("passed all")  # debugging log
    #     print(cards_location)
    #     print(CARDS_LOCATION_CONST)
    #
    #     Game.cards_dictionary = cards_dic  # passing dictionary to class
    #     Game.first_card_key = ""  # reset card
    #     Game.first_card_value = ""
    #     Game.second_card_key = ""
    #     Game.second_card_value = ""


if __name__ == "__main__":
    GameApp().run()