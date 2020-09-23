"""Flows for development"""
import webbrowser


def yes_no(question):
    """Leave function until user entered yes"""
    print(question + " [y/N]")
    answer = input()
    while answer != "y":
        print(question)
        answer = input()


def module_testing():
    """Module testing"""
    yes_no("Have you created a module test?")


def integration():
    """Integrate the module"""
    yes_no("Have you integrated the module?")


def integration_testing():
    """Integration test"""
    yes_no("Have you created an integration test?")


def development():
    """Develop a feature"""
    yes_no("Have you created a new module and developed the feature?")


def wireframe():
    """Create wireframes"""
    webbrowser.open("https://wireframe.cc")
    webbrowser.open("https://github.com/felixbaron/star-trader/issues/")
    yes_no("Have you added the issue to the project and added a wireframe?")


def file_an_issue():
    """File an issue"""
    yes_no("Please file an issue with: ./scripts/open-issue")


def push():
    """Push the feature to Github"""
    yes_no("Have you pushed the commit to Github?")


def uat():
    """User acceptance testing"""
    yes_no("Have you conducted UAT (expected results vs. actual results)?")


pipeline = [
    file_an_issue,
    wireframe,
    module_testing,
    development,
    integration_testing,
    push,
    uat,
]


def main():
    """Main function"""
    print("Hi Felix, let's get started!")
    for task in pipeline:
        task()


if __name__ == "__main__":
    main()
