import webbrowser, sys, pyperclip,urllib.parse

sys.argv # ['mapit,py'. '870','Valencia', 'St.' ]

# Check if command line arguments were passed

if len(sys.argv)> 1:
    # number of items in the list
    # ['mapit,py'. '870','Valencia', 'St.' ] -> '870 Valencia St.'
    address = ' '.join(sys.argv[1:])

else: address = pyperclip.paste()

url = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(address)

webbrowser.open(url)




