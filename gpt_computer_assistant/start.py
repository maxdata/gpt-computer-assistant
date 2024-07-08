import os, sys
import argparse


def start():
    """
    Starts the computer assistant application.

    This function starts the computer assistant application, which includes parsing command-line arguments
    to set the profile, initializing the graphical user interface, and starting the application event loop.

    Command-line Arguments:
    --profile (str): The profile to use for the application.

    Raises:
    ImportError: If the required modules or packages are not found.

    Returns:
    None
    """
    # get --profile argument with library
    
    from gpt_computer_assistant.gpt_computer_assistant import QApplication
    from gpt_computer_assistant.gpt_computer_assistant import MainWindow
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", help="profile to use")
    args = parser.parse_args()
    profile = args.profile
    print("Profile:", profile)

    if profile is not None:
        from .utils.db import set_profile
        set_profile(profile)

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start()