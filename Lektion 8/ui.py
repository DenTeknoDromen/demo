import os


def line(dots):
    if dots:
        print("*" * 30)
    else:
        print("-" * 30)


def header(text):
    print(text.upper().center(30))


def echo(text):
    print(text)


def prompt(text):
    return input(f"{text} > ")


def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
