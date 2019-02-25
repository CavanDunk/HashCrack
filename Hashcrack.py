# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:29:34 2019

@author: C15ni
"""
#Cavan Dunkley
#CSC 4980/6980
#
import urllib
import hashlib
import time
import sys

def crack():
    #hass = raw_input("Enter hash. \n>")  # type: str
    count = 0
    #crac = input("enter hash. \n>")
   # with urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt') as url:
        #site = url.read()
    passwords = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read())
    for paws in passwords.split('\n'):

        guess = hashlib.sha1(bytes(paws)).hexdigest()
        if guess == sys.argv[1]:
            return "The password is " + str(paws) +"\nWe went through "+str(count)+" passwords"
            print(count)
            quit()
        else:
            count=count+1
    return None
def salt():
    count = 0
    correct = ""
    passwords = str(urllib.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read())
    for paws in passwords.split('\n'):
        guess = hashlib.sha1(paws).hexdigest()
        if guess == sys.argv[2]:
            correct = str(paws)
            print(correct)
    for paws in passwords.split('\n'):
         concat_guess = hashlib.sha1(correct+paws).hexdigest()
         guess_concat = hashlib.sha1(paws+correct).hexdigest()
         if concat_guess == sys.argv[1]:
             print("The password is "+ str(paws) +" and took " + str(count) + " number of tries")
             quit()
         elif guess_concat == sys.argv[2]:
            print("The password is "+ str(paws)+ "and took "+str(count) + " number of tries")
            quit()
         else:
             count=count+1
    print(count) 
def gradproblem():
    grad = input("Please enter the hash for the grad Problem\n")
    count = 0
    blank = " "
    Passwords = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read(),'utf-8') 
    for paws in Passwords.split('\n'):
        for space in Passwords.split('\n'):
            guess = hashlib.sha1(bytes(paws+blank+space,'utf_8')).hexdigest()
            #guess2 = hashlib.sha1(bytes(space+blank+paws,'utf_8')).hexdigest()
            if guess == grad:
                print(paws)
                quit()
           # elif guess2 == grad:
               # print(paws)
                #quit()
            else:
                count=count+1
                print(count)
def undergrad():

    #response = raw_input("Is this a salted hash (y or n)\n")
    if len(sys.argv) == 2:
        start = time.time()
        answer = crack()
        end = time.time()
        print(answer)
        print("The program took " + str(end-start)+ "seconds to find the password")
    elif len(sys.argv) == 3:
        start = time.time()
        answer = salt()
        print(answer)
        end= time.time()
        print("The program took " + str(end-start)+ "seconds to find the password")
    return None
def main():
    undergrad()
    #gradproblem()

main()