def simple_generator(num=3):
 
    for k in range(1,num):
        yield k*2


for k in simple_generator(8):
    print(k)
