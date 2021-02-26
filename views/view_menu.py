import pyfiglet


class ViewMenu:

    line = (100*":")

    @staticmethod
    def print_welcome_page():

        welcome_message = pyfiglet.figlet_format("CHESS SCORES MANAGER")
        print(welcome_message)
        print(ViewMenu.line)
        print("AUTHOR : ALEXANDRE MERANCIENNE")
        print(ViewMenu.line)
        print("\nCHOOSE OPTION NUMBER: \n")

    @staticmethod
    def return_first_choice_welcome_page():
        option_choice = input(("Generate Tournament [1]"
                              + "    Search Player [2]"
                              + "    Search Tournament [3]"
                              + "    Quit Program [4]\n\n").center(80))
        while str(option_choice) not in "1234":
            print("Choose a number between 1 and 4.")
            option_choice = input(("Generate Tournament [1]"
                                  + "    Search Players [2]"
                                  + "    Search Tournament [3]"
                                  + "    Quit Program [4]\n\n").center(80))
            continue
        return option_choice

    @staticmethod
    def quit_current_page():
        quit_current_page = input("Return to Main Page ? [Y/N]\n")
        while quit_current_page not in "yYnN":
            quit_current_page = input("Return to Main Page ? [Y/N]\n")
            continue
        return quit_current_page

    @staticmethod
    def print_first_option():
        start_tournament = pyfiglet.figlet_format("NEW TOURNAMENT",
                                                  font="digital")
        print(start_tournament)

    @staticmethod
    def quit_program():
        print("\nThank you for using Chess Scores Manager !")
