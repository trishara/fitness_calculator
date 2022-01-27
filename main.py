# Dependencies
import os
import pickle
import sys

from colorama import Fore

# Makes colorama module work in Windows console
os.system("")

# Makes hide/show cursor functions work depending on os
if os.name == 'nt':
    import ctypes


    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]


def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()


hide_cursor()


def calculate_weight_per_week(data) -> float:
    """Reads a list that stores a week's worth of data to calculate and return average weight per week"""

    total = 0
    day = len(data)

    for index, weight in enumerate(data):
        total += weight[2]

    return total / day


def calculate_bodyfat_per_week(data) -> float:
    """Reads a list that stores a week's worth of data to calculate and return average body fat per week"""

    total = 0
    day = len(data)

    for index, body_fat in enumerate(data):
        total += body_fat[3]

    return total / day


def calculate_skeletal_muscle_per_week(data) -> float:
    """Reads a list that stores a week's worth of data to calculate and return average skeletal muscle per week"""

    total = 0
    day = len(data)

    for index, skeletal_muscle in enumerate(data):
        total += skeletal_muscle[4]

    return total / day


def get_weight_loss(weight_averages):
    """Reads a list that stores the weight, body fat, and skeletal muscle averages for each week, gets the number of
    weeks, then reads a list of just the average weight for each week then calculates and prints the average weight
    lost per week and per month"""

    weeks = len(weight_averages)
    weight_diff = []

    for week in range(1, weeks + 1):
        try:
            difference = weight_averages[week - 1] - weight_averages[week]
            weight_diff.append(difference)
        except IndexError:
            break

    total = 0

    for num in weight_diff:
        total = total + num

    weight_loss_per_week = total / len(weight_diff)
    weight_loss_per_week = f"{weight_loss_per_week:.2f}"
    weight_loss_per_week = float(weight_loss_per_week)
    weight_loss_per_month = weight_loss_per_week * 4

    print(
        f"\n{Fore.LIGHTWHITE_EX}                   Average Weight Lost                   Per Week: {Fore.RESET}{Fore.LIGHTMAGENTA_EX}"
        f"{weight_loss_per_week:.2f} lbs{Fore.RESET}{Fore.LIGHTWHITE_EX} | Per Month: {Fore.RESET}{Fore.LIGHTMAGENTA_EX}"
        f"{weight_loss_per_month:.2f} lbs{Fore.RESET}", end="")


def get_bodyfat_loss(bodyfat_averages):
    """Reads a list that stores the weight, body fat, and skeletal muscle averages for each week, gets the number of
    weeks, then reads a list of just the average body fat for each week then calculates and prints the average body fat
    lost per week and per month"""

    weeks = len(bodyfat_averages)
    bodyfat_diff = []

    for week in range(1, weeks + 1):
        try:
            difference = bodyfat_averages[week - 1] - bodyfat_averages[week]
            bodyfat_diff.append(difference)
        except IndexError:
            break

    total = 0

    for num in bodyfat_diff:
        total = total + num

    bodyfat_lost_per_week = total / len(bodyfat_diff)
    bodyfat_lost_per_week = f"{bodyfat_lost_per_week:.2f}"
    bodyfat_lost_per_week = float(bodyfat_lost_per_week)
    bodyfat_lost_per_month = bodyfat_lost_per_week * 4

    print(
        f"\n{Fore.LIGHTWHITE_EX}                   Average Body Fat % Lost               Per Week: {Fore.RESET}{Fore.LIGHTMAGENTA_EX}"
        f"{bodyfat_lost_per_week:.2f}%{Fore.RESET}{Fore.LIGHTWHITE_EX}    | Per Month: {Fore.RESET}{Fore.LIGHTMAGENTA_EX}"
        f"{bodyfat_lost_per_month:.2f}%{Fore.RESET}", end="")


def get_skeletal_muscle_gained(skeletal_muscle_averages):
    """Reads a list that stores the weight, body fat, and skeletal muscle averages for each week, gets the number of
    weeks, then reads a list of just the average skeletal muscle for each week then calculates and prints the average
    skeletal muscle lost per week and per month"""

    weeks = len(skeletal_muscle_averages)
    skeletal_muscle_diff = []

    for week in range(1, weeks + 1):
        try:
            difference = skeletal_muscle_averages[week - 1] - skeletal_muscle_averages[week]
            skeletal_muscle_diff.append(difference)
        except IndexError:
            break
    total = 0

    for num in skeletal_muscle_diff:
        total = total + num

    skeletal_muscle_gain_per_week = total / len(skeletal_muscle_diff)
    skeletal_muscle_gain_per_week = f"{skeletal_muscle_gain_per_week:.2f}"
    skeletal_muscle_gain_per_week = float(skeletal_muscle_gain_per_week)
    skeletal_muscle_gain_per_month = skeletal_muscle_gain_per_week * 4

    print(f"\n{Fore.LIGHTWHITE_EX}                   Average Skeletal Muscle Gained        Per Week: {Fore.RESET}"
          f"{Fore.LIGHTMAGENTA_EX}{skeletal_muscle_gain_per_week:.2f} lbs{Fore.RESET}{Fore.LIGHTWHITE_EX} | Per Month: {Fore.RESET}"
          f"{Fore.LIGHTMAGENTA_EX}{skeletal_muscle_gain_per_month:.2f} lbs{Fore.RESET}")


def print_summary(final_data):
    """Prints all calculated data into a table"""

    if final_data:
        weight_averages = []
        bodyfat_averages = []
        skeletal_muscle_averages = []

        for data in final_data:
            weight_averages.append(data[1])
            bodyfat_averages.append(data[2])
            skeletal_muscle_averages.append(data[3])

        print(f'''\n{Fore.LIGHTWHITE_EX}
                                                ┬─┐┌─┐┌─┐┬ ┬┬ ┌┬┐┌─┐
                                                ├┬┘├┤ └─┐│ ││  │ └─┐
                                                ┴└─└─┘└─┘└─┘┴─┘┴ └─┘

       ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~
        |       week       |    weight averages    |    body fat averages    |    skeletal muscle averages    |
       ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~ {Fore.RESET}''')

        output = []

        for data in final_data:
            week = f"{Fore.LIGHTWHITE_EX}|{Fore.RESET}        {Fore.LIGHTMAGENTA_EX}{data[0]}{Fore.RESET}         {Fore.LIGHTWHITE_EX}|{Fore.RESET}"
            weight = f"{Fore.LIGHTMAGENTA_EX}        {data[1]:.2f}{Fore.RESET}{Fore.LIGHTWHITE_EX}        |{Fore.RESET}"
            bodyfat = f"{Fore.LIGHTMAGENTA_EX}         {data[2]:.2f}{Fore.RESET} {Fore.LIGHTWHITE_EX}         |{Fore.RESET}"
            skeletal_muscle = f"{Fore.LIGHTMAGENTA_EX}             {data[3]:.2f}{Fore.RESET}{Fore.LIGHTWHITE_EX}             |{Fore.RESET}"
            output.append((week, weight, bodyfat, skeletal_muscle))

        for data in output:
            print("{: >58} {: >15} {: >20} {: >30}".format(*data))

        print(
            f"{Fore.LIGHTWHITE_EX}       ~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~{Fore.RESET}")

        get_weight_loss(weight_averages)
        get_bodyfat_loss(bodyfat_averages)
        get_skeletal_muscle_gained(skeletal_muscle_averages)

    else:
        print(f"{Fore.LIGHTWHITE_EX}    You do not have any saved files.{Fore.RESET}")
        main()


def load_data(filename) -> list:
    """Load saved data into a list"""

    data = []
    try:
        with open(filename, "rb") as f:
            while True:
                try:
                    data.append(pickle.load(f))
                except EOFError:
                    break

        return data
    except FileNotFoundError:
        data = []
        return data

def save_data(filename, data):
    """Save final data into a file"""

    filename = f"{filename}.txt"

    with open(filename, 'wb') as f:
        for d in data:
            pickle.dump(d, f)


def get_data_from_user(filename):
    """Function that gets all data from the user to make calculations such as # of weeks, weight, body fat, and
    skeletal muscle per day, then displays results at the end"""

    print(f"\n{Fore.LIGHTWHITE_EX}    Sounds good. Now how many weeks of data do you have?{Fore.RESET}")

    while True:

        weeks = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

        try:
            weeks = int(weeks)
        except TypeError and ValueError:
            print(f"{Fore.RED}    Invalid input. Please try again.{Fore.RESET}")

        try:
            if weeks == 1:
                print(f"{Fore.RED}    You must enter at least two weeks of data.{Fore.RESET}")
            elif weeks >= 2:
                break
            else:
                pass
        except TypeError:
            pass

    days = 7
    week_data = []
    final_data = []

    for week in range(0, weeks):
        for day in range(0, days):

            print(f"\n{Fore.LIGHTWHITE_EX}    + week {week + 1} | day {day + 1}\n"
                  f"    ===================={Fore.RESET}\n")

            print(f"{Fore.LIGHTWHITE_EX}    Weight: {Fore.RESET}")

            while True:
                weight = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

                try:
                    weight = float(weight)
                except ValueError:
                    pass

                if isinstance(weight, float):
                    break
                else:
                    print(f"{Fore.RED}    Invalid input. Please try again.{Fore.RESET}")

            print(f"{Fore.LIGHTWHITE_EX}    Body Fat %: {Fore.RESET}")

            while True:
                body_fat = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

                try:
                    body_fat = float(body_fat)
                except ValueError:
                    pass

                if isinstance(body_fat, float):
                    break
                else:
                    print(f"{Fore.RED}    Invalid input. Please try again.{Fore.RESET}")

            print(f"{Fore.LIGHTWHITE_EX}    Skeletal Muscle (lb): {Fore.RESET}")

            while True:
                skeletal_muscle = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

                try:
                    skeletal_muscle = float(skeletal_muscle)
                except ValueError:
                    pass

                if isinstance(skeletal_muscle, float):
                    break
                else:
                    print(f"{Fore.RED}    Invalid input. Please try again.{Fore.RESET}")

            while True:
                print(f"\n{Fore.LIGHTWHITE_EX}    + week {week + 1} day {day + 1} | "
                      f"weight: {Fore.RESET}{Fore.LIGHTMAGENTA_EX}"
                      f"{weight}{Fore.RESET}{Fore.LIGHTWHITE_EX} | body fat: "
                      f"{Fore.RESET}{Fore.LIGHTMAGENTA_EX}{body_fat}%{Fore.RESET}"
                      f"{Fore.LIGHTWHITE_EX} | skeletal muscle: {Fore.RESET}"
                      f"{Fore.LIGHTMAGENTA_EX}{skeletal_muscle} lb{Fore.RESET}"
                      f"\n\n")

                week_data.append((week + 1, day + 1, weight, body_fat, skeletal_muscle))
                break

        final_data.append((week + 1, calculate_weight_per_week(week_data), calculate_bodyfat_per_week(week_data),
                           calculate_skeletal_muscle_per_week(week_data)))

        week_data = []

    if save:
        save_data(filename, final_data)

    print_summary(final_data)


def load_existing_file() -> str:
    """Pull all save files in a directory, then display it for user to select which file to load"""

    global filename

    files = os.listdir(r"C:\Users\...\....\fitness_calculator")

    text_files = []

    for file in files:

        if ".txt" in file:
            text_files.append(file)

    id = 0
    save_files = []
    ids = []

    for file in text_files:
        id += 1
        save_files.append((id, file))
        ids.append(id)

    if not save_files:
        filename = ""
        return filename
    else:
        print(f"\n{Fore.LIGHTWHITE_EX}    Choose which file you want to load:{Fore.RESET}")

        for index, tuple in enumerate(save_files):
            print(
                f"        {Fore.LIGHTWHITE_EX}[{Fore.RESET}{Fore.LIGHTMAGENTA_EX}{tuple[0]}{Fore.RESET}{Fore.LIGHTWHITE_EX}]{Fore.RESET}"
                f"{Fore.LIGHTMAGENTA_EX} {tuple[1]}{Fore.RESET}")

        while True:

            x = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

            try:
                x = int(x)

                if x not in ids:
                    print(f"{Fore.RED}    You did make a valid selection. Please try again.{Fore.RESET}")
                else:
                    for index, tuple in enumerate(save_files):
                        if x == tuple[0]:
                            filename = tuple[1]
                            break
                    break
            except ValueError:
                print(f"{Fore.RED}    You did make a valid selection. Please try again.{Fore.RESET}")

        return filename


def create_and_save_file() -> str:
    """Function that creates a save file and allows user to name it"""

    global filename, weeks, save
    save = True

    print(f"\n{Fore.LIGHTWHITE_EX}    Great! What do you want the name of your file to be?{Fore.RESET}")

    while True:

        filename = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

        for i in filename:
            if i == " ":
                filename = filename.replace(" ", "_")
            elif i == ".":
                filename = filename.replace(".", "")
            elif i == "/":
                filename = filename.replace("/", "")
            elif i == "\\":
                filename = filename.replace("\\", "")

        break

    return filename


def enter_data_no_save() -> None:
    """Returns an empty filename and tells the get_user_data() function that user doesn't want to save data"""

    global filename, weeks, save
    filename = None
    save = False

    return filename


def main():
    """Shows main menu where user can choose what they want to do"""

    print(f'''{Fore.LIGHTWHITE_EX}
    
    Welcome to {Fore.LIGHTMAGENTA_EX}Trisha's Fitness Calculator{Fore.RESET}! {Fore.LIGHTWHITE_EX}
    
    You will prompted to enter your {Fore.LIGHTMAGENTA_EX}daily weight{Fore.RESET}{Fore.LIGHTWHITE_EX} and {Fore.RESET}{Fore.LIGHTMAGENTA_EX}body composition.{Fore.RESET}{Fore.LIGHTWHITE_EX}
    
    If you have missing data on a specific day, simply use the data from the previous day. 
   
    However, it is recommended that you don't do this more than once or it will greatly
    affect the accuracy of your results.{Fore.RESET}
''')

    print(f"{Fore.LIGHTWHITE_EX}    Type [{Fore.RESET}{Fore.LIGHTMAGENTA_EX}Y{Fore.RESET}{Fore.LIGHTWHITE_EX}] "
          f"to continue: {Fore.RESET}")

    while True:

        x = input(f"{Fore.LIGHTMAGENTA_EX}    >> {Fore.RESET}")

        if x == "y" or x == "Y":
            break
        else:
            print(f"{Fore.RED}    Invalid input. Please try again.{Fore.RESET}")

    print(f'''{Fore.LIGHTWHITE_EX}
    Let's get started! First, what are you trying to do?

        {Fore.RESET}{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}{Fore.LIGHTWHITE_EX} I want to [{Fore.RESET}{Fore.LIGHTMAGENTA_EX}v{Fore.RESET}{Fore.LIGHTWHITE_EX}]iew results from an existing save file
        {Fore.RESET}{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}{Fore.LIGHTWHITE_EX} I am entering [{Fore.RESET}{Fore.LIGHTMAGENTA_EX}n{Fore.RESET}{Fore.LIGHTWHITE_EX}]ew data and want to start a new save file
        {Fore.RESET}{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}{Fore.LIGHTWHITE_EX} I want to [{Fore.RESET}{Fore.LIGHTMAGENTA_EX}e{Fore.RESET}{Fore.LIGHTWHITE_EX}]nter data without saving it{Fore.RESET}\n''')

    while True:

        s = input(f"    {Fore.LIGHTMAGENTA_EX}>> {Fore.RESET}")

        if s == "v" or s == "V":
            print_summary((load_data(load_existing_file())))
            break
        elif s == "n" or s == "N":
            get_data_from_user(create_and_save_file())
            break
        elif s == "e" or s == "E":
            get_data_from_user(enter_data_no_save())
            break
        else:
            print(f"{Fore.RED}    Invalid input. Please try again.{Fore.RESET}")

# Start the program
main()
