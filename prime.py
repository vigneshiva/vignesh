a = int(input(" "));
if ( a > 1):
  for b in range(2,a):
    c = a % b;
    if ( c == 0):
      print("no");
      break
  else:
       print("yes");
else:
  print("no");
