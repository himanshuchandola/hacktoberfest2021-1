# module

from random import *

import os,sys

os.system("clear")

# isi

guess=""

password=input("Masukan Password > ")

wordlist = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","anjim","subrek"]

while(guess in password):

  Guess=""

  for letter in password:

    guessletter=wordlist[randint(0,25)]

    guess=str(guessletter) + str(guess)

  print("Password crackder >",guess)

print("Selamat sekarang anda sudah menjadi heker pro")

