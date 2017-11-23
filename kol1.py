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
from time import sleep

fname = "data.txt"
number = 0


class Plane:
    def __init__(self, type_of_plane):
        self.type_of_the_plane = type_of_plane

    def get_name_of_the_plane(self):
        print(self.type_of_the_plane)


class Simulation(Plane):
    def __init__(self, type_of_plane):
        Plane.__init__(self, type_of_plane)
        self.orientation_of_the_plane = 0

    def turbulation(self):
        self.orientation_of_the_plane = gauss(20, 15)

    def tilt_correction(self):
        if self.orientation_of_the_plane > 25:
            self.orientation_of_the_plane = self.orientation_of_the_plane - \
                                            (((self.orientation_of_the_plane / 360) / 10) * 360)
        else:
            self.orientation_of_the_plane = self.orientation_of_the_plane - \
                                            (((self.orientation_of_the_plane / 360) / 5) * 360)

    def get_orientation_of_the_plane(self):
        print(self.orientation_of_the_plane)


if __name__ == "__main__":

    file1 = open(fname, 'w+')
    file1.truncate()

    plane_1 = Simulation("88")
    while 1:
        choice1 = raw_input("The plane takes off, please choose from below:\n1 - "
                            "Start the simulation of the flight.\n2 - Exit.\n")
        if choice1 == "1" or choice1 == "2":
            break
        else:
            print("Wrong input")
            continue

    if choice1 == "1":
        type_plane = raw_input("Please enter the type of the plane.\n")
        plane_1.type_of_the_plane = type_plane
        while 1:
            number += 1
            plane_1.turbulation()
            print("Current information: ")
            plane_1.get_orientation_of_the_plane()
            print("\n")
            file1.write(str(number) + '. Orientation = ' + str(plane_1.orientation_of_the_plane))
            plane_1.tilt_correction()
            print("After correction: ")
            plane_1.get_orientation_of_the_plane()
            file1.write(', after correction = ' + str(plane_1.orientation_of_the_plane) + '\n')
            while 1:
                s = raw_input("\n1 - Continue.\n2 - Exit.\n")
                if s == "1" or s == "2":
                    break
                print("Wrong raw_input")
                if s != "1" or s != "2":
                    continue
            if s == "2":
                print("Goodbye\nAll data is saved in file - data.txt.")
                break

    if choice1 == "2":
        print('Goodbye!\nAll data is saved in file - data.txt.')