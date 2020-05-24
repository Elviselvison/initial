n = int(input().strip())
if (n%2!=0):
        
    print('Weird')
    break
    if n in range(2,5):
        print('Not Weird')
    elif n in range(6,20):
        print('Weird')
    elif n in range(21,100):
        print('Not Weird')