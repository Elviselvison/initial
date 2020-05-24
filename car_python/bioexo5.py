'''
Enumerate is a built-in function of Python. Its usefulness can not be summarized in a single line. 
Yet most of the newcomers and even some advanced programmers are unaware of it. It allows us to loop
 over something and have an automatic counter '''

for i, testo in enumerate( 'abcdefghi'):
  #  print('La lettera %s è %s' % (i+1, testo ))
  print('La lettera %a è %s' % (i+1, testo ))
    # leggere la stringa da tastiera

x= input("inserisci una stringa   ")

for i, testo in enumerate(x):
    print('La lettera %a è %s' % (i+1, testo ))


my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list,1):
    print(c, value)
