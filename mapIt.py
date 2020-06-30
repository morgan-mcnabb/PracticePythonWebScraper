#! python3
# Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    # get address from clipboard
    address = pyperclip.paste

webbrowser.open('https://www.google.com/maps/place/' + address)