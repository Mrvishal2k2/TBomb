from colorama import Fore, Style


class IconicDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ → ]" + Style.RESET_ALL
        self.STDS = "     "


class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ SUCCESS ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ FAILURE ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ WARNING ]"\
            + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ SECTION ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ COMMAND ]" + Style.RESET_ALL
        self.STDS = "           "


class MessageDecorator(object):
    def __init__(self, attr):
        ICON = IconicDecorator()
        STAT = StatusDecorator()
        if attr == "icon":
            self.PASS = ICON.PASS
            self.FAIL = ICON.FAIL
            self.WARN = ICON.WARN
            self.HEAD = ICON.HEAD
            self.CMDL = ICON.CMDL
            self.STDS = ICON.STDS
        elif attr == "stat":
            self.PASS = STAT.PASS
            self.FAIL = STAT.FAIL
            self.WARN = STAT.WARN
            self.HEAD = STAT.HEAD
            self.CMDL = STAT.CMDL
            self.STDS = STAT.STDS

    def SuccessMessage(self, RequestMessage):
        print(f"{self.PASS} {Style.RESET_ALL}{RequestMessage}")

    def FailureMessage(self, RequestMessage):
        print(f"{self.FAIL} {Style.RESET_ALL}{RequestMessage}")

    def WarningMessage(self, RequestMessage):
        print(f"{self.WARN} {Style.RESET_ALL}{RequestMessage}")

    def SectionMessage(self, RequestMessage):
        print(
            (
                (f"{self.HEAD} {Fore.CYAN}{Style.BRIGHT}" + RequestMessage)
                + Style.RESET_ALL
            )
        )

    def CommandMessage(self, RequestMessage):
        return f"{self.CMDL} {Style.RESET_ALL}{RequestMessage}"

    def GeneralMessage(self, RequestMessage):
        print(f"{self.STDS} {Style.RESET_ALL}{RequestMessage}")

