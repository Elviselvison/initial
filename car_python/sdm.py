def is_leap(year):
    leap = False
    
    # Write your logic here
    if (1900<=leap<= 10**5 and (leap%4==0) and (leap%100==0) and (leap%400==0)):
        leap = True
        
    return leap
    

year = int(input('give me a number  '))
is_leap(year)



