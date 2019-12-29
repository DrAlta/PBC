import itertools
import copy
letter='D'
costs1=[]
templist=['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']

print('def testD(cost1, ecost, rAB, rAC, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE):')
print('    ret=[]')
print('')
for x in templist:
    if letter in x:
        costs1.append(x)

for lvl1 in itertools.combinations(costs1, 1):
    lvl1=lvl1[0]
    costs2=copy.deepcopy(costs1)
    costs2.remove(lvl1)

    print('    if 0 < cost1 and r',lvl1,' >=cost1:', sep='')
    print('        tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)'.replace(lvl1, lvl1+'-cost1'), sep='')
    print('        for x in tail:')
    print("            myadd(x, '",lvl1,"', cost1)", sep='')
    print('            if not(x in ret):')
    print('                ret.append(x)')
    print('    else:')

    for lvl2 in itertools.combinations(costs2, 1):
        lvl2=lvl2[0]
        costs3=copy.deepcopy(costs2)
        costs3.remove(lvl2)
        
        print('        cost2=cost1-r',lvl1, sep='')
        print('        if 0 < cost2 and r',lvl2,' >=cost2 and r',lvl1,'>0: #r',lvl1,' r',lvl2, sep= '')
        print('            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)'.replace(lvl2, lvl2+'-cost2').replace('r'+lvl1, '  0'), sep='')
        print('            for x in tail:')
        print("                myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
        print("                myadd(x, '",lvl2,"', cost2)", sep='')
        print('                if not(x in ret):')
        print('                    ret.append(x)')
        print('        else:')
          
        for lvl3 in itertools.combinations(costs3, 1):
            lvl3=lvl3[0]
            costs4=copy.deepcopy(costs3)
            costs4.remove(lvl3)

            print('            cost3=cost2-r',lvl2, sep='')
            print('            if 0 < cost3 and r',lvl3,' >=cost3 and r',lvl2,'>0: #r',lvl1,' r',lvl2,' r',lvl3, sep='')
            print('                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)'.replace(lvl3, lvl3+'-cost3').replace('r'+lvl2, '  0').replace('r'+lvl1, '  0'), sep='')
            print('                for x in tail:')
            print("                    myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
            print("                    myinsert(x, '",lvl2,"', r",lvl2,")", sep='')
            print("                    myadd(x, '",lvl3,"', cost3)", sep='')
            print('                    if not(x in ret):')
            print('                        ret.append(x)')
            print('            else:')

            for lvl4 in itertools.combinations(costs4, 1):
                lvl4=lvl4[0]
                costs5=copy.deepcopy(costs4)
                costs5.remove(lvl4)
##############
                print('                cost4=cost3-r',lvl3, sep='')
                print('                if 0 < cost4 and r',lvl4,' >=cost4 and r',lvl3,'>0: #r',lvl1,' r',lvl2,' r',lvl3,' r',lvl4, sep='')
#                    #print('t AC BC CD CE')
                print('                    tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)'.replace(lvl4, lvl4+'-cost4').replace('r'+lvl3, '  0').replace('r'+lvl2, '  0').replace('r'+lvl1, '  0'), sep='')
                print('                    for x in tail:')
                print("                        myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                        myinsert(x, '",lvl2,"', r",lvl2,")", sep='')
                print("                        myinsert(x, '",lvl3,"', r",lvl3,")", sep='')
                print("                        myadd(x, '",lvl4,"', cost4)", sep='')
                print('                        if not(x in ret):')
                print('                            ret.append(x)')
                print('                else:')
                print('                    cost5=80+cost4-r',lvl4, sep='')
                print('                    if cost5<=r',letter,":", sep='')
                print('                        tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE,)'.replace('r'+letter+',', 'r'+letter+'-cost5,').replace('r'+lvl4, '  0').replace('r'+lvl3, '  0').replace('r'+lvl2, '  0').replace('r'+lvl1, '  0'), sep='')
                print('                        for x in tail:')
                print("                            myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                            myinsert(x, '",lvl2,"', r",lvl2,")", sep='')
                print("                            myinsert(x, '",lvl3,"', r",lvl3,")", sep='')
                print("                            myinsert(x, '",lvl4,"', r",lvl4,")", sep='')
                print("                            myinsert(x, '",letter,"', cost5)", sep='')
                print('                            if not(x in ret):')
                print('                                ret.append(x)')

####################################3                
print('    if cost1 == 0:')
print('        ret=testE(ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE)')
print('    return(ret)')
print('#####################################################################################################################################')

