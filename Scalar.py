# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:42:19 2019

@author: Julian
"""

# Uebungsaufgaben 2 / Aufgabe 1 / Skalarprodukt berechnen

#print("Eingabe der Vekroten: scalar([Zahl1,Zahl2,Zahl3,...],[Zahl3,Zahl4,Zahl5,...])")
def scalar(vec1,vec2):

    if len(vec1)==len(vec2):
            
        scalar = 0
        for i in range(len(vec1)):
            scalar += vec1[i] * vec2[i]
        return(scalar)
    else:
        print("Länge der Vektoren muss gleich lang sein")
        return(False)