def lung_pa(f):
    b = []
    # posso usare anche append 
    c= []
    for i in f:
        b+=[len(i)]
        c.append(len(i))
    print(b)
    print(c)

f= ['ciao', 'ragazzi']
lung_pa(f)