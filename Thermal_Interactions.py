#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 19:11:58 2022

@author: jaredechternach
"""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import pandas as pd
np.set_printoptions(suppress=True)

SystemA=input('Is System A an Einstein Solid? y/n: ')
SystemB=input('Is System B an Einstein Solid? y/n: ')

###########################################################################################################################

#Einstein Solids
if SystemA=='y' and SystemB=='y':
    energya=int(input('Enter the Energy for System A: '))
    energyb=int(input('Enter the Energy for System B: '))
    numbera=int(input('Enter the Number of Particles in SYstem A: '))
    numberb=int(input('Enter the Number of Particles in System B: '))

    totalE=energya+energyb
     


    def microstate(N,E):
        microstate=[]
        for x in range(E+1):
            microstate1 = factorial(x+N-1)/(factorial(x)*factorial(N-1))
            microstate.append(int(microstate1))
        return microstate

    microEa=microstate(numbera, totalE)
    microEb=microstate(numberb,totalE)
    microEa.reverse()

    totalmicro=[]
    for i in range(len(microEa)):
        totalmicro.append(microEa[i]*microEb[i])

    Pa1=[]
    for x in totalmicro:
        y=x/sum(totalmicro)
        Pa1.append(y)

    Pa=np.around(Pa1,6)
    Ea=[]
    Eb=[]
    for i in range(len(microEa)):
        Ea.append(totalE-i)
        Eb.append(i)


    data={'\u03A9''a':microEa, 'Eb':Eb, '\u03A9''b':microEb, '\u03A9''a''\u03A9''b':totalmicro,'P(a)':Pa}
    df=pd.DataFrame(data,index=Ea).rename_axis('Ea',axis=1)
    print(' ' '\n''\n\n\n')
    print(df)
    print(' ' '\n''\n\n\n')
    index=0
    for x in Pa:
        if x==max(Pa):
            i=index
            print('The state with the highest probability is Ea='+str(Ea[i])+', Eb='+str(Eb[i])+', with a probability of ' +str(Pa[i])+'.')
            index+=1
        else:
            index+=1
    print(' ' '\n''\n\n\n')

    plt.scatter(Ea,Pa,marker='.')
    plt.xlabel('Ea')
    plt.ylabel('P(a)')

###########################################################################################################################

#Einstein Solid and Magnetic System
elif (SystemA=='y' and SystemB=='n'):
    energya=int(input('Enter the Energy for System A: '))
    energyb=int(input('Enter the Energy for System B: '))
    numbera=int(input('Enter the Number of Particles in System A: '))
    numberb=int(input('Enter the Number of Spins in System B: '))
    energyfield=int(input('Enter the Energy for the Outside Magnetic Field: '))

    totalE=energya+energyb
    Eamax=2*totalE-energyfield
    Ea=[]
    Eb=[]
    if abs(Eamax)<=numberb:
        for a in range(Eamax+1):
            for b in range(-totalE+energyfield,totalE+1):
                if a+b==totalE:
                    Ea.append(a)
                    Eb.append(b)
        #print(Ea,Eb)
        n=[]
        for x in Eb:
            n1=0.5*(numberb-(x/0.5))
            n.append(int(n1))

        #print(n)
        microEa=[]
        for x in Ea:
            microEa1=factorial(x+numbera-1)/(factorial(x)*factorial(numbera-1))
            microEa.append(int(microEa1))

        spin=[]
        for x in n:
            spin1=factorial(numberb)/(factorial(x)*factorial(numberb-x))
            spin.append(int(spin1))

        microEb=spin

        totalmicro=[]
        for i in range(len(microEa)):
            totalmicro.append(microEa[i]*microEb[i])
        
        Pa1=[]
        for x in totalmicro:
            y=x/sum(totalmicro)
            Pa1.append(y)

        Pa=np.around(Pa1,6)


        data={'\u03A9''a':microEa, 'Eb':Eb, 'n':n,'\u03A9''b':microEb, '\u03A9''a''\u03A9''b':totalmicro,'P(a)':Pa}
        df=pd.DataFrame(data,index=Ea).rename_axis('Ea',axis=1)
        print('\n\n')
        print(df)
        print('\n')
        index=0
        for x in Pa:
            if x==max(Pa):
                i=index
                print('The state with the highest probability is Ea='+str(Ea[i])+', Eb='+str(Eb[i])+', with a probability of ' +str(Pa[i])+'.')
                index+=1
            else:
                index+=1

        plt.scatter(Ea,Pa,marker='.')
        plt.xlabel('Ea')
        plt.ylabel('P(a)')
        
    else:
        print('\n\n')
        print('System B does not have enough spins! Make sure the number of spins')
        print('is greater than or equal to 2*(Ea+Eb) minus the energy')
        print('of the External Field.')

#############################################################################################################################

#Magnetic Systems
elif (SystemA=='n' and SystemB=='n'):
    energya=int(input('Enter the Energy for System A: '))
    energyb=int(input('Enter the Energy for System B: '))
    numbera=int(input('Enter the Number of Spins in System A: '))
    numberb=int(input('Enter the Number of Spins in System B: '))
    energyfield=int(input('Enter the Energy for the Outside Magnetic Field: '))

    Emax=energya+energyb+energyfield
    #print(Emax)
    Ea=[]
    Eb=[]
    for a in range(-abs(Emax),abs(Emax)+1,2):
        for b in range(-2*abs(Emax),2*abs(Emax)+1):
            if a+b==Emax:
                
                Ea.append(a)
                Eb.append(b)
            
    #print(Ea,Eb)

    if abs(Emax)<=numbera and 2*abs(Emax)<=numberb:
        na=[]
        for x in Ea:
            n1=(numbera/2-(x/2))
            na.append(int(n1))

        nb=[]
        
        for x in Eb:
            n2=(numberb/2-(x/2))
            nb.append(int(n2))

        #print(na,nb)
        microspina=[]

        for x in na:
            spin1=factorial(numbera)/(factorial(x)*factorial(numbera-x))
            microspina.append(int(spin1))


        microspinb=[]
        for x in nb:
            spin2=factorial(numberb)/(factorial(x)*factorial(numberb-x))
            microspinb.append(int(spin2))
       
        totalmicro=[]
        for i in range(len(microspina)):
            totalmicro.append(microspina[i]*microspinb[i])

        Pa1=[]
        for x in totalmicro:
            y=x/sum(totalmicro)
            Pa1.append(y)

        Pa=np.around(Pa1,6)

        data={'na':na,'\u03A9''a':microspina, 'Eb':Eb, 'nb':nb,'\u03A9''b':microspinb, '\u03A9''a''\u03A9''b':totalmicro,'P(a)':Pa}
        df=pd.DataFrame(data,index=Ea).rename_axis('Ea',axis=1)
        pd.options.display.max_columns=None
        pd.set_option('display.width', 1000)
        print(' ' '\n''\n\n\n')
        print(df)
        print(' ' '\n''\n')
        index=0
        for x in Pa:
            if x==max(Pa):
                i=index
                print('The state with the highest probability is Ea='+str(Ea[i])+', Eb='+str(Eb[i])+', with a probability of ' +str(Pa[i])+'.')
                index+=1
            else:
                index+=1
                

        plt.scatter(Ea,Pa,marker='.')
        plt.xlabel('Ea')
        plt.ylabel('P(a)')

    elif abs(Emax)>numbera:
        print('\n')
        print('System A does not have enough spins! Make sure the number of spins is greater than or equal to the Total Energy.')

    elif 2*abs(Emax)>numberb:
        print('\n')
        print('System B does not have enough spins! Make sure the number of spins is greater than or equal to twice the Total Energy.')

#####################################################################################################################
#Magnetic System and Einstein Solid
else:
    print('I have not written the code for this system. If you really want, re-run the code')
    print('and select yes and then no for the first two prompts.')
    



    
    