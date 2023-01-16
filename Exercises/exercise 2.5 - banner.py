
def banner(text):
    """Print the text as a banner"""
    n = len(text)
    print('***' + '*' * n + '***')
    print('*  ' + text    + '  *')
    print('***' + '*' * n + '***')


def create_banner(text, c = '*', max_length = None):
    """A more generic function to create a banner

    arguments:
       text - the text to put in the banner
       c - the surrounding character. Default = '*'
       max_length - the maximal length of the banner. Default = no limit"""

    if max_length is None:
        n = len(text)
    else:
        n = max_length - 6
        text = text[:n-3] + '...'

    s  = c * (n + 6) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 6)
    return s

def print_banner(text, **kwargs):
    """Print the created banner"""
    print(kwargs)
    print(create_banner(text, **kwargs))


# ----------------------------------------------------------

if __name__ == '__main__':

    name = input('Wat is jouw naam? : ')

    banner(name)

    settings = {'c': '+', 'max_length': 20}

    print_banner(name, **settings)
