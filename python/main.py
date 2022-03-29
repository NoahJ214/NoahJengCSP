# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
from week0 import keypad, ship, swap, tree
from week1 import datalists, fibonacci
from week2 import factorial, math, palindrome, oop_math

main_menu = [
    ["Swap", swap.run],
    ["Tree", tree.run],
    ["Fibonacci", fibonacci.run],
    ["Datalists", datalists.datalists_run],
    ["Factorial", factorial.factorial_run],
    ["Palindrome", palindrome.run],
    ["Factors", math.factors],
    ["OOP Math", oop_math.factors]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Ship", "ship.py"],
    ["Keypad", "keypad.py"]
]

math_sub_menu = [
    ["Fibonacci", "fibonacci.py"],
    ["Factorial", factorial.factorial_run],
    ["Factors", math.factors],
    ["OOP Math", oop_math.factors]
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  


def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op


    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try: 
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()