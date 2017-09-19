#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def main():

    secret = random.randint(1,1000)

    while True:
        guess = int(raw_input("Ugani skrito številko! Je med 1 in 1000"))
        if secret == guess :
            print "Bravo, to je skrita številka!"
            break
        elif secret < guess :
            print "Zal to ni skrita številka, skrita številka je manjša"
        elif secret > guess :
            print "Zal to ni skrita številka, skrita številka je večja"

if __name__ == '__main__':
        main()