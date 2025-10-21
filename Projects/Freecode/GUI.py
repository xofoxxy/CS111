import dearpygui.dearpygui as dpg
import threading

class GUI:
    def __init__(self):
        self.current_game = None
        self.game_thread = None
        self.game_queue = None

        dpg.create_context()
        self.main_gui()
        dpg.create_viewport(title='Custom Title', width=600, height=300)
        dpg.setup_dearpygui()
        dpg.set_primary_window("Primary Window", True)
        dpg.show_viewport()
        dpg.start_dearpygui()


    def main_gui(self):
        if not self.current_game:
            with dpg.window(tag="Primary Window"):
                b0 = dpg.add_button(label="crossword", callback=self.crossword)
                b1 = dpg.add_button(tag=100, label="Button 1")
                dpg.add_button(tag="Btn2", label="Button 2")
        else:
            dpg.add_text(f"{self.current_game} is running")

    def crossword(self):
        def start_crossword(user_data):
            list_of_words = user_data
            #TODO generate the crossword using the user_data

        def crossword_initialization():
            print("crossword initialization running")
            with dpg.window(tag="crossword init"):
                with dpg.group() as word_input_group:
                    pass

                def get_words():
                    for item in dpg.get_item_children(word_input_group):
                        print(dpg.get_item_state(item))
                        print(dpg.get_item_state(item)["app_data"])
                    return dpg.get_item_state(word_input_group)["app_data"]

                def word_input_callback(sender, app_data, user_data):
                    print(f"sender: {sender}, app_data: {app_data}, user_data: {user_data}")
                    print(dpg.get_item_state(sender))
                    for item in dpg.get_item_children(word_input_group):
                        if dpg.get_item_state(item)["app_data"] == "":
                            print("empty input already in existence!")
                        else:
                            print("adding new input")
                            word_input()

                def word_input():
                    dpg.add_input_text(label="Enter a word", callback=word_input_callback, parent=word_input_group)
                    print("input added")
                    print(dpg.get_item_children(word_input_group)[1])
                dpg.add_button(label="generate crossword", tag="generate crossword", callback=start_crossword, user_data=get_words())
                word_input()

        print("crossword initialization")
        self.current_game = "crossword initialization beginning"
        crossword_initialization()



