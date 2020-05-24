import webbrowser
webbrowser.open('www.facebook.com')

# un beep 

import winsound
try:
    x=int(input('inserisci un numero '))
    print('hai scitto il numero {}'.format(x))
    winsound.Beep(3000, 500)
     
except:
    print('inserisci un numero non un testo')
    winsound.Beep(600, 500)
