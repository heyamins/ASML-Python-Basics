
def banner(text, c = '*'):
    """Print the text as a banner"""
    n = len(text)
    print(c * (n + 6))
    print(c + '  ' + text    + '  ' + c)
    print(c * (n + 6))


def create_banner(text, c = '*'):
    """Create a banner"""
    n = len(text)
    s = c * (n + 6) + '\n'
    s += c + '  ' + text + '  ' + c + '\n'
    s += c * (n + 6)
    return s

def print_banner(*args, **kwargs):
    print(create_banner(*args, **kwargs))


def f():
    banner('Testing', '#')




if __name__ == '__main__':

    banner('Testing')
