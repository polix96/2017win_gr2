###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#!/usr/bin/env python2.7
from random import gauss

fname="data.txt"
number=0


class Plane:
    def __init__(self):
        self.orientation=0

    def turbulation(self):
        self.orientation = gauss(20, 15)

    def correction(self):
        self.orientation -= (self.orientation / 4)



if __name__=="__main__":

  plane_1=Plane()

  while (1):
    choice1 = raw_input("The plane takes off, please choose from below:\n1 - Start the simulation of the flight.\n2 - Exit.\n")
    if(choice1=="1" or choice1=="2" ):
      break
    else:
      print("Wrong input")
      continue


  file=open(fname,'w+')
  file.truncate()

  if(choice1=="1"):
    while(1):
      number+=1
      plane_1.turbulation()
      print('Orientation of plane = ', plane_1.orientation)
      file.write(str(number) + '. Orientation = ' + str(plane_1.orientation))
      plane_1.correction()
      print('After correction, orientation =', plane_1.orientation)
      file.write(', after correlation = '+str(plane_1.orientation)+'\n')
      while(1):
        s = raw_input("\n1 - Continue.\n2 - Exit.\n")
        if(s=="1" or s=="2"):
          break
          print("Wrong input")
        if(s!="1" or s!="2"):
          continue
      if (s=="2"):
        print("Goodbye\nAll data is saved in file - data.txt.")
        break


  if(choice1=="2"):
    print("Goodbye!\nAll data is saved in file - data.txt.")