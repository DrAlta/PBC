import math
from random import random

def criticalSuccess(x_in):
    temp = 0.0

    # coefficients
    a = -1.0873391184025034E+08
    b = 1.0873391335155436E+08
    c = 2.1271593562839072E+07
    d = -1.7918341543076949E+01
    Offset = 8.1761532034302249E+00

    temp = d / (1.0 + math.pow(b/(x_in-a), c))
    temp += Offset
    return temp


def severeSuccess(x_in):
    temp = 0.0

    # coefficients
    a = 1.0841258375191873E+02
    b = -1.0842454912883915E+02
    c = 1.9790280143781700E+01
    d = 3.1018186243300512E+01
    Offset = -4.8560935754736878E+00

    temp = d / (1.0 + math.pow(b/(x_in-a), c))
    temp += Offset
    return temp


def normSuccess(x_in):
    temp = 0.0

    # coefficients
    a = -4.2068709979208012E+04
    b = 4.2066999560075230E+04
    c = -8.1103638181765073E+03
    d = 5.5955647463315813E+01
    Offset = 2.8514895378812888E+00

    temp = d / (1.0 + math.pow(b/(x_in-a), c))
    temp += Offset
    return temp


def butSuccess(x_in):
    temp = 0.0

    # coefficients
    a = 1.3247056363590533E+05
    b = -1.3247063211865211E+05
    c = -2.5017433602647052E+04
    d = -7.4314363070982481E+01
    Offset = 8.7715712787763479E+01

    temp = d / (1.0 + math.pow(b/(x_in-a), c))
    temp += Offset
    return temp


def normFailure(x_in):
    temp = 0.0

    # coefficients
    a = 5.2042038910706978E+01
    b = -5.2578138916095156E+01
    c = 9.7132772148806446E+00
    d = 4.2748355254879783E+01
    Offset = 7.0508007094677509E+01

    temp = d / (1.0 + math.pow(b/(x_in-a), c))
    temp += Offset
    return temp


def skillCheck(bl, roll):
    if roll<criticalSuccess(bl):
        return(["Critical Success",roll])
        
    elif roll<severeSuccess(bl):
        return(["Severe Success",roll])
        
    elif roll<normSuccess(bl):
        return(["Success",roll])
        
    elif roll<butSuccess(bl):
        return(["But Success",roll])
        
    elif roll<normFailure(bl):
        return(["Failure",roll])
        
    else:
        return(["Critical Failure",roll])
def skillRoll(bl, mod):
    roll=101*random()
    if roll<=5:
        print("comf")
        roll2=101*random()+mod
        comf=skillCheck(bl,roll2)
        print(comf)
        if comf[0]=='Critical Failure':
            return(['Success', normSuccess(bl)-1])
        elif comf[0]=='Failure':
            return(['Success', normSuccess(bl)-(normFailure(bl)-roll2)])
        elif comf[0]=='But Success':
            return(['Severe Success', severeSuccess(bl)-(butSuccess(bl)-roll2)])
        else:
            return(['Critical Success', criticalSuccess(bl)-(severeSuccess(bl)-roll2)])
    else:
        return(skillCheck(bl,roll+mod))
bl=0
print("critsucc",criticalSuccess(bl),"SeveSucc",severeSuccess(bl),"succ",normSuccess(bl),"butSucc",butSuccess(bl),"fail",normFailure(bl))
print(skillRoll(bl,0))