a, b = [int(a) for a in input(" ").split()] 
for i in range((a+1),b):
    c = i % 2;
    if (c==0):
    	print(" ",i);
