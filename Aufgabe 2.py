# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:27:53 2019

@author: Julian
"""

#Lösung: Alea jacta est
"""
Lösung gesucht mit Konsoleneingabe:
for i in range(1,27):
    caesar("Hslh qhjah lza",i)
"""
def caesar(satz,zahl):
    a_bet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#Wandelt alle Buchstaben in Großbuchstaben um.
    satz = satz.upper() 
    
#Hier wird entschlüsselt
    x = list(satz)
    if zahl >= 0:
        for i in range(len(x)):
            if x[i] in a_bet:
              for j in range(len(a_bet)):
                if x[i] in a_bet[j]:
                    ausgabe = a_bet[j - zahl]
#Gibt die Entschlüsselung aus, end = '' bewirkt, dass alle Buchstaben in einer 
#Zeil geschrieben werden.
                    print(ausgabe, end = '')
            else:
                 print(x[i], end = '')
#Hier wird verschlüsselt

#wenn man bei dieser Form: ausgabe = a_bet[j - zahl] in a_bet[j + zahl]
#stehen würde, erreicht das Programm das Ende der Liste --> out of range. Daher
#wird von der Länge a_bet die Zahl abgezogen und so der Buchstabe von rechts 
#nach links gesucht. Mit diesem Trick erreicht das Programm nie das Ende der 
#Liste.
    else:
        
        for i in range(len(x)):
            if x[i] in a_bet:
              for j in range(len(a_bet)):
                if x[i] in a_bet[j]:
                    ausgabe = a_bet[j - (len(a_bet) + zahl)]
                    print(ausgabe, end = '')
            else:
                 print(x[i], end = '')
       
    print()