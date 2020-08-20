# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:11:38 2020

@author: user
"""

d = {}
print ("THE USELESS THING EVER !!!!")


while True :
    print('1.SET ')
    print('2.LIST ALL THE WORD ')
    print('3.ENG TO CH ')
    print('4.CH TO ENG ')
    print('5.TEST ')
    print('6.QUIT ')
    
    option = input(" YOUR NUM : ")
    
    if option == '6' :
        break
    elif option == '1' :
        while True :
            voc = input('YOUR ENG (PRESS 0 TO QUIT):')
            if voc == '0' :
                break
            if voc not in d :
                voc_ch = input("ENTER CH :")
                d[voc] = voc_ch
            else:
                print ("NOPE")
    elif option == '2':
        s = sorted(d)
        print(s)
        for i in s:
            print(i,':',d[i])
            
    elif option == '3':
        while True:
            voc = input ('YOUR CH (PRESS 0 TO QUIT) :')
            if voc == '0':
                break
            if voc in d:
                print(voc,'CH IS : ',d[voc])
            else:
                print("CAN'T FOUND THIS WORD")
                
    elif option == '4':
        while True:
            got = False
            ch = input("YOUR CH (PRESS 0 TO QUIT) :")
            if ch == '0':
                break
            for k,v in d.items():
                if ch == v:
                    print (ch,"ENG IS",k)
                    got = True
            if got == False:
                print("CAN'T FOUND THIS WORD")
                
    elif option == '5':
        s = 0
        for k,v in d.items() :
            print (v,':')
            ans = input()
            if ans == k:
                s += 1
                print ("YEEEA")
            
            else:
                print('NOPE')
        print("YOU GOT",s)
            
            
                
                            
    
    
    