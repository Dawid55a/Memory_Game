from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import *
from kivy.core.window import Window
from kivy.clock import Clock
from random import *
import sys
import time

Window.size = (480, 753)
Window.top = True

CARDS_LOCATION_CONST = ["t1", "t2", "t3", "t4",
                        "m1", "m2", "m3", "m4",
                        "lm1", "lm2", "lm3", "lm4",
                        "b1", "b2", "b3", "b4"]
CARDS_SYMBOL = ["@", "!", "#", "$", "%", "|", "&", "?"]

main_interface = None


class MainInterface(ScreenManager):
    cards_dictionary = {}
    first_card_key = ""
    first_card_value = ""
    second_card_key = ""
    second_card_value = ""
    start = None
    end = None

    # color of the cards
    card_color = [131/255, 191/255, 67/255, 1]

    # method creating new schema for the game
    def create_cards(self):
        if self.first_card_value == "" and self.second_card_value == "":
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
                self.ids[card].background_color = self.card_color
                print(card, "is set to --> ", cards_dic[card])  # debugging log

            print("passed all")  # debugging log
            print(cards_location)
            print(CARDS_LOCATION_CONST)

            self.start = time.time()  # start of counting time

            self.cards_dictionary = cards_dic  # passing dictionary to class
            self.first_card_key = ""  # reset card
            self.first_card_value = ""
            self.second_card_key = ""
            self.second_card_value = ""

            # deleting the winner widget
            try:
                main_interface.ids.Game.remove_widget(winn)
                print(main_interface.ids.Game)
            except:
                print(sys.exc_info())
        else:
            pass

    # showing card symbol and initializing check method
    def show_card(self, card):
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

            Clock.schedule_once(lambda dt: MainInterface.check(self, card), 1)

    # checking conditions on chosen cards
    def check(self, card):
        print(card)
        if self.first_card_value == self.cards_dictionary[card]:  # if second card is the same

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

            Clock.schedule_once(lambda dt: MainInterface.winn(self), 0.5)

        elif self.first_card_value != card:  # if second card is different

            self.ids[self.first_card_key].text = ""
            self.ids[self.first_card_key].disabled = False
            self.ids[self.first_card_key].background_color = self.card_color

            self.ids[card].text = ""
            self.ids[card].disabled = False
            self.ids[card].background_color = self.card_color

            self.first_card_value = ""
            self.first_card_key = ""
            self.second_card_key = ""
            self.second_card_value = ""

            print("Wrong ")

    # executing winning sequence
    def winn(self):
        found = 0
        # checking if every field is disabled
        for loc in CARDS_LOCATION_CONST:
            if self.ids[loc].disabled:
                found += 1
        # showing winn label
        if found == 16:
            global winn

            # time of the game
            self.end = time.time()
            your_time = round(self.end - self.start, 2)
            print(your_time)

            winn = Label(
                text="Winn!!!\n" + str(your_time) + "s",
                font_size=80
            )
            main_interface.ids.Game.add_widget(winn)
        print("Founded pairs: ", found)

    # setting color of cards
    def set_color(self, colorpicker):
        print("Chosen color: ", colorpicker.color)
        # print(Game.ids["main"].background_color)
        # print(Game.ids.items())
        # Game.ids["t1"].background_color = self.ids["colorpicker"].color
        # print(root.ids["t1"])


class GameApp(App):

    def build(self):
        global main_interface
        main_interface = MainInterface(transition=CardTransition())
        return main_interface

    Clock.schedule_once(lambda dt: main_interface.create_cards(), 0.5)


if __name__ == "__main__":
    GameApp().run()
