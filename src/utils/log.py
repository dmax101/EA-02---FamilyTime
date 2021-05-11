class Log:
    @staticmethod
    def info(message, arg=None, loc=""):
        if loc == "":
            loc = "main"

        if arg == None:
            print('[{}] {}'.format(loc, message))
        elif arg == 'success':
            print('\x1b[0;30;42m[{}] {}\x1b[0m'.format(loc, message))
        elif arg == 'error':
            print('\x1b[0;30;41m[{}] {}\x1b[0m'.format(loc, message))
        elif arg == 'warning':
            print('\x1b[0;30;43m[{}] {}\x1b[0m'.format(loc, message))
        else:
            print('\x1b[0;30;41m[{}] Wrong argument!\x1b[0m')
            print('[{}] {}'.format(loc, message))