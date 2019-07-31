a = int(input(" "));
b = 0;
if ( a > 0):
  for b in range(2,a):
    c = a % b;
    if ( c == 0):
      print("yes");
    else :
      print("no");
else:
  print("no");
