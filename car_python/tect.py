class Triangle:
    def __init__(self,a,b,c,h):
        self.a, self.b, self.c, self.h = a,b,c,h # attributi 

    
    def area(self):
        return self.a*self.b/2


    
    def perimeter(self):
        return self.a+ self.b+ self.c


    def print_info(self):
        print("area del triangolo = 2.f%" % self.area())   
        print("il perimetro del triangolo = 2.f%" % self.perimeter())
        





   
 







