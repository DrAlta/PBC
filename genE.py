import itertools
import copy
letter='D'
costs1=['AE', 'BE', 'CE', 'DE']

print('def testE(cost1, rAB, rAC, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE):')
print('    ret=[]')
print('')

for lvl1 in itertools.combinations(costs1, 1):
    lvl1=lvl1[0]
    costs2=copy.deepcopy(costs1)
    costs2.remove(lvl1)

    print('    if 0 < cost1 and r',lvl1,' >=cost1:', sep='')
    print('        print("',lvl1,'")')
    print('        x=dict()')
    print("        myadd(x, '",lvl1,"', cost1)", sep='')
    print('        if not(x in ret):')
    print('            ret.append(x)')
    print('        print(ret)')
    print('    else:')

    for lvl2 in itertools.combinations(costs2, 1):
        lvl2=lvl2[0]
        costs3=copy.deepcopy(costs2)
        costs3.remove(lvl2)
        
        print('        cost2=cost1-r',lvl1, sep='')
        print('        if 0 < cost2 and r',lvl2,' >=cost2 and r',lvl1,'>0: #r',lvl1,' r',lvl2, sep= '')
        print('            print("',lvl1,lvl2,'")')
        print('            x=dict()')
        print("            myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
        print("            myadd(x, '",lvl2,"', cost2)", sep='')
        print('            if not(x in ret):')
        print('                ret.append(x)')
        print('        else:')
          
        for lvl3 in itertools.combinations(costs3, 1):
            lvl3=lvl3[0]
            costs4=copy.deepcopy(costs3)
            costs4.remove(lvl3)

            print('            cost3=cost2-r',lvl2, sep='')
            print('            if 0 < cost3 and r',lvl3,' >=cost3 and r',lvl2,'>0: #r',lvl1,' r',lvl2,' r',lvl3, sep='')
            print('                print("',lvl1,lvl2,lvl3,'")')
            print('                x=dict()')
            print("                myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
            print("                myinsert(x, '",lvl2,"', r",lvl2,")", sep='')
            print("                myadd(x, '",lvl3,"', cost3)", sep='')
            print('                if not(x in ret):')
            print('                    ret.append(x)')
            print('            else:')

            for lvl4 in itertools.combinations(costs4, 1):
                lvl4=lvl4[0]
                costs5=copy.deepcopy(costs4)
                costs5.remove(lvl4)
##############
                print('                cost4=cost3-r',lvl3, sep='')
                print('                if 0 < cost4 and r',lvl4,' >=cost4 and r',lvl3,'>0: #r',lvl1,' r',lvl2,' r',lvl3,' r',lvl4, sep='')
                print('                    print("',lvl1,lvl2,lvl3,lvl4,'")')

#                    #print('t AC BC CD CE')
                print('                    x=dict()')
                print("                    myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                    myinsert(x, '",lvl2,"', r",lvl2,")", sep='')
                print("                    myinsert(x, '",lvl3,"', r",lvl3,")", sep='')
                print("                    myadd(x, '",lvl4,"', cost4)", sep='')
                print('                    if not(x in ret):')
                print('                        ret.append(x)')
                print('                else:')
                print('                    cost5=80+cost4-r',lvl4, sep='')
                print('                    if cost5<=r',letter,":", sep='')
                print('                        print("',lvl1,lvl2,lvl3,lvl4,'lvl5")')
                print('                        x=dict()')
                print("                        myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                        myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                        myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                        myinsert(x, '",lvl1,"', r",lvl1,")", sep='')
                print("                        myinsert(x, '",letter,"', cost5)", sep='')
                print('                        if not(x in ret):')
                print('                            ret.append(x)')

####################################3                
print('    return(ret)')
#               testE(cost1, rAB, rAC, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE)
print('for x in testE(   10,   0,   0,   0,   1,   0,   0,   0,  0,   0,   0,  0,  0,  0,  0,  9):')
print('    print(x)')