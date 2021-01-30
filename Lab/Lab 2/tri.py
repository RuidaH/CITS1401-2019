"""
A Program to classify Triangles.
CITS1401
Beware: there may be errors
"""

def tri(side1, side2, side3):

   if (side1==side2):
      if (side1 == side3):
         print("It is equilateral.")
      else:
         print("It is isosceles.")
   else:
      if (side1 == side3):
         print("It is isosceles.")
      else:
         if (side2 == side3):
            print("It is isosceles.")
         else:
            if (side1 >= side2 + side3):
               print("No such triangle.")
            else:
               if (side2 >= side1 + side3):
                  print("No such triangle.")
               else:
                  if (side3 >= side1 + side2):
                     print("No such triangle.")
                  else:
                     if (side1 <= 0):
                        print("No such triangle.")
                     elif (side2 <=0):
                        print("No such traingle.")
                     elif (side3 <= 0):
                        print("No such triangle.")
                     else:
                        print("It is scalene.")
