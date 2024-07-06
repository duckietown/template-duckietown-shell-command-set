from dt_shell import DTCommandAbs, DTShell


class DTCommand(DTCommandAbs):
    help = 'An example command'  # please redefine this help message

    # name = <read-only> a string with the name of the command
    # level = <read-only> integer indicating the level of this command. Follows directory hierarchy
    # commands = <read-only> a dictionary of subcommands

    @staticmethod
    def command(shell: DTShell, args):
        # this function will be invoked when the user presses [Return] and runs the command
        #
        #   shell   is the instance of DTShell hosting this command
        #   args    is a list of arguments passed to the command
        #
        print("This is an example command. Discard it after you instantiate your own command set")

    @staticmethod
    def complete(shell, word, line):
        # this function will be invoked when the user presses the [Tab] key for auto completion.
        #
        #   shell   is the instance of DTShell hosting this command
        #   word    is the right-most word typed in the terminal
        #           (usually the string the user is trying to auto-complete)
        #
        #   return  a list of strings. Each string is a suggestion for the user
        #
        return ['suggestion_1', 'suggestion_2']
