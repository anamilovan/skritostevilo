#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = int(raw_input("Vnesi skrito številko!"))
guess = int(raw_input("Ugani skrito številko!"))
if secret == guess :
    print "Bravo, to je skrita številka!"
else :
    print "Zal to ni skrita številka"