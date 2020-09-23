"""Manage my day with a simple python script"""
import webbrowser


def yes_no(question):
    """Leave function until user entered yes"""
    print(question + " (y/N)")
    answer = input()
    while answer != "y":
        print(question)
        answer = input()


def do_mails():
    """Do mails"""
    webbrowser.open("https://outlook.office365.com/mail/")
    webbrowser.open("https://outlook.office365.com/calendar/view/workweek")
    yes_no("Have you done your email?")



pipeline = [
    do_mails,
]


def main():
    """Main function"""
    print("Hi Felix, let's get to work!")
    for task in pipeline:
        task()


if __name__ == "__main__":
    main()
