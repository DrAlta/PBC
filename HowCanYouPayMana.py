import pdb
def myadd(xhash, xkey, x):
 #   print("adding ",xkey, "=",x," to ",xhash)
    if xkey in xhash:
        xhash.update({xkey: x})
    else:
        if x >0:
            xhash.update({xkey: x})
        else:
            xhash.update({xkey+'z': x})
  #  print("now:", xhash)

def myinsert(xhash, xkey, x):
   # print("inserting ",xkey, "=",x," to ",xhash)

    if xkey in xhash:
        print("key ", xkey, " already exists as",xhash[xkey]," !") 

    assert not( xkey in xhash), "key %s already exists !" % xkey
    if x >0:
        xhash.update({xkey: x})
    else:
        xhash.update({xkey+'z': x})
    #print("now:", xhash)

def testD(cost1, ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE, rBD, rBE,  rDE, rA, rB, rC, rD, rE):
    return([dict()])

def testC(cost1, dcost, ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE,rBD, rBE,  rDE, rA, rB, rC, rD, rE):
    print(cost1, dcost, ecost,'AC=', rAC, rAB, rAD, rAE, ' BC=', rBC, rCD, rCE,rBD, rBE,  rDE, rA, rB, rC, rD, rE)

#    assert rBC ==5
    ret=[]
    
    if 0 < cost1 and rAC >=cost1:
        #print('t AC')
        tail=testD(dcost, ecost, rAB, rAC-cost1, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'AC', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rAC
        if 0 < cost2 and rBC >=cost2 and rAC>0: #rAC rBC
            #print('t AC BC')
            tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost2, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AC', rAC)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rCD >=cost3 and rBC>0: #rAC rBC rCD
                #print('t AC BC CD')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,rCD-cost3, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rCE >=cost4 and rCD>0: #rAC rBC rCD rCE
                    #print('t AC BC CD CE')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rC:
                        #print('t AC BC CD CE C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC #rAC rBC rCE
            if 0 < cost3 and rCE >=cost3 and rBC>0: #rAC rBC rCE
                #print('t AC BC CE')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD, rCE-cost3,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rCD >=cost4 and rCE>0: #rAC rBC rCE rCD
                    #print('t AC BC CE CD')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rC:
                        #print('t AC BC CE CD C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rCD >=cost2 and rAC>0:#rAC rCD
            #print('t AC CD')
            tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD-cost2, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AC', rAC)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rBC >=cost3 and rCD>0: #rAC rCD rBC
                #print('t AC CD BC')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE,   0, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rAC rCD rBC rCE
                if 0 < cost4 and rCE >=cost4 and rBC>0: #rAC rCD rBC rCE
                    #print('t AC CD BC CE')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rC:
                        #print('t AC CD BC CE C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD #rAC rCD rCE
            if 0 < cost3 and rCE >=cost3 and rCD>0: #rAC rCD rCE
                #print('t AC CD CE')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE,   0, rCE-cost3,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE #rAC rCD rCE rBC
                if 0 < cost4 and rBC >=cost4 and rCE>0: #rAC rCD rCE rBC
                    #print('t AC CD CE BC')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rC:
                        #print('t AC CD CE BC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rCE >=cost2 and rAC>0: #rAC rCE
            #print('t AC CE')
            tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD, rCE-cost2,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AC', rAC)
                myadd(x, 'CE', cost2)
                print('ret=', ret, " x=",x)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rBC >=cost3 and rCE>0: #rAC rCE rBC
                #print('t AC CE BC')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE, rCD,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'BC', cost3)
                    print('ret=', ret, " x=",x)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rAC rCE rBC rCD
                if 0 < cost4 and rCD >=cost4 and rBC>0: #rAC rCE rBC rCD
                    #print('t AC CE BC CD')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rC:
                        #print('t AC CE BC CD C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rCD >=cost3 and rCE>0: #rAC rCE rCD
                #print('t AC CE CD')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD-cost3,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD #rAC rCE rCD rBC
                if 0 < cost4 and rBC >=cost4 and rCD>0: #rAC rCE rCD rBC
                    #print('t AC CE CD BC')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rC:
                        #print('t AC CE CD BC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBC >=cost1: #rBC
        #print('t BC')
        tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost1, rBD, rBE, rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BC', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBC
        if 0 < cost2 and rAC >=cost2 and rBC>0: #rBC rAC
            #print('t BC AC')
            tail=testD(dcost, ecost, rAB, rAC-cost2, rAD, rAE,   0, rBD, rBE, rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'AC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAC
            if 0 < cost3 and rCD >=cost3 and rAC>0: #rBC rAC rCD
                #print('t BC AC CD')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost3, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD #rBC rAC rCD rCE
                if 0 < cost4 and rCE >=cost4 and rCD>0: #rBC rAC rCD rCE
                    #print('t BC AC CD CE')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rC:
                        #print('t BC AC CD CE C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAC
            if 0 < cost3 and rCE >=cost3 and rAC>0: #rBC rAC rCE
                #print('t BC AC CE')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD, rCE-cost3,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE #rBC rAC rCE rCD
                if 0 < cost4 and rCD >=cost4 and rCE>0: #rBC rAC rCE rCD
                    #print('t BC AC CE CD')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rC:
                        #print('t BC AC CE CD C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rCD >=cost2 and rBC>0:#rBC rCD
            #print('t BC CD')
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD-cost2, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rAC >=cost3 and rCD>0: #rBC rCD rAC
                #print('t BC CD AC')
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE,   0, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC #rBC rCD rAC rCE
                if 0 < cost4 and rCE >=cost4 and rAC>0: #rBC rCD rAC rCE
                    #print('t BC CD AC CE')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AC', rAC)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rC:
                        #print('t BC CD AC CE C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD #rBC rCD rCE
            if 0 < cost3 and rCE >=cost3 and rCD>0: #rBC rCD rCE
                #print('t BC CD CE')
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE,   0, rCE-cost3,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE #rBC rCD rCE rAC
                if 0 < cost4 and rAC >=cost4 and rCE>0: #rBC rCD rCE rAC
                    #print('t BC CD CE AC')
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'AC', cost3)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        #print('t BC CD CE AC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rCE >=cost2 and rBC>0:#rBC rCE
            #print('t BC CE')
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD, rCE-cost2,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'CE', cost2)
                print("ret=", ret, " x=", x)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rAC >=cost3 and rCE>0: #rBC rCE rAC
                #print('t BC CE AC')
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE, rCD,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC #rBC rCE rAC rCD
                if 0 < cost4 and rCD >=cost4 and rAC>0: #rBC rCE rAC rCD
                    #print('t BC CE AX CD')#hereZZZ
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AC', rAC)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rC:
                        #print('t BC CE AC CD C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE #rBC rCE rCD
            if 0 < cost3 and rCD >=cost3 and rCE>0: #rBC rCE rCD
                #print('t BC CE CD')
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD-cost3,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD #rBC rCE rCD rAC
                if 0 < cost4 and rAC >=cost4 and rCD>0: #rBC rCE rCD rAC
                    #print('t BC CE CD AC')
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'AC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        #print('t BC CE CD AC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

    if 0 < cost1 and rCD >=cost1: #rCD
        #print('t CD')
        tail=testD(dcost, ecost, rAC, rAB, rAD, rAE, rBC, rCD-cost1, rCE, rBD, rBE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'CD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rCD
        if 0 < cost2 and rAC >=cost2 and rCD>0:#rCD rAC
            #print('t CD AC')
            tail=testD(dcost, ecost, rAC-cost2, rAB, rAD, rAE, rBC,   0, rCE, rBD, rBE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'AC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAC
            if 0 < cost3 and rBC >=cost3 and rAC>0: #rCD rAC rBC
                #print('t CD AC BC')
                tail=testD(dcost, ecost,   0, rAB, rAD, rAE, rBC-cost3,   0, rCE, rBD, rBE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rCD rAC rBC rCE
                if 0 < cost4 and rCE >=cost4 and rBC>0: #rCD rAC rBC rCE
                    #print('t CD AC BC CE')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rC:
                        #print('t CD AC BC CE C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAC
            if 0 < cost3 and rCE >=cost3 and rAC>0: #rCD rAC rCE
                #print('t CD AC CE')
                tail=testD(dcost, ecost,   0, rAB, rAD, rAE, rBC,   0, rCE-cost3, rBD, rBE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE #rCD rAC rCE rBC
                if 0 < cost4 and rBC >=cost4 and rCE>0: #rCD rAC rCE rBC
                    #print('t CD AC CE BC')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rC:
                        #print('t CD AC CE BC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBC >=cost2 and rCD>0:#rCD rBC
            #print('t CD BC')
            tail=testD(dcost, ecost, rAC, rAB, rAD, rAE, rBC-cost2,   0, rCE, rBD, rBE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAC >=cost3 and rBC>0: #rCD rBC rAC
                #print('t CD BC AC')
                tail=testD(dcost, ecost, rAC-cost3, rAB, rAD, rAE,   0,   0, rCE, rBD, rBE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC #rCD rBC rAC rCE
                if 0 < cost4 and rCE >=cost4 and rAC>0: #rCD rBC rAC rCE
                    #print('t CD BC AC CE')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AC', rAC)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rC:
                        #print('t CD BC AC CE C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rCE >=cost3 and rBC>0: #rCD rBC rCE
                #print('t CD BC CE')
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE,   0, rCE-cost3,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE #rCD rBC rCE rAC
                if 0 < cost4 and rAC >=cost4 and rCE>0: #rCD rBC rCE rAC
                    #print('t CD BC CE AC')
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'AC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        #print('t CD BC CE AC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rCE >=cost2 and rCD>0:#rCD rCE
            #print('t CD CE')
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,   0, rCE-cost2,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rAC >=cost3 and rCE>0: #rCD rCE rAC
                #print('t CD CE AC')
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE, rBC, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC #rCD rCE rAC rBC
                if 0 < cost4 and rBC >=cost4 and rAC>0: #rCD rCE rAC rBC
                    #print('t CD CE AC BC')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AC', rAC)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rC:
                        #print('t CD CE AC BC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE #rCD rCE rBC
            if 0 < cost3 and rBC >=cost3 and rCE>0: #rCD rCE rBC
                #print('t CD CE BC')
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rCD rCE rBC rAC
                if 0 < cost4 and rAC >=cost4 and rBC>0: #rCD rCE rBC rAC
                    #print('t CD CE BC AC')
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'AC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        #print('t CD CE BC AC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

    if 0 < cost1  and rCE >=cost1 :
        #print('t CE')
        tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE-cost1,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'CE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rCE
        if 0 < cost2 and rAC >=cost2 and rCE>0:#rCE rAC
            #print('t CE AC')
            tail=testD(dcost, ecost, rAB, rAC-cost2, rAD, rAE, rBC, rBD, rBE, rCD,   0,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'AC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAC
            if 0 < cost3 and rBC >=cost3 and rAC>0: #rCE rAC rBC
                #print('t CE AC BC')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE, rCD,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rCE rAC rBC rCD
                if 0 < cost4 and rCD >=cost4 and rBC>0: #rCE rAC rBC rCD
                    #print('t CE AC BC CD')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rC:
                        #print('t CE AC BC CD C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            if 0 < cost3 and rCD >=cost3 and rAC>0: #rCE rAC rCD
                #print('t CE AC CD')
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD-cost3,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD #rCE rAC rCD rBC
                if 0 < cost4 and rBC >=cost4 and rCD>0: #rCE rAC rCD rBC
                    #print('t CE AC CD BC')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AC', rAC)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rC:
                        #print('t CE AC CD BC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBC >=cost2 and rCE>0:#rCE rBC
            #print('t CE BC')
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2, rBD, rBE, rCD,   0,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAC >=cost3 and rBC>0: #rCE rBC rAC
                #print('t CE BC AC')
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE, rCD,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC #rCE rBC rAC rCD
                if 0 < cost4 and rCD >=cost4 and rAC>0: #rCE rBC rAC rCD
                    #print('t CE BC AC CD')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AC', rAC)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rC:
                        #print('t CE BC AC CD C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            if 0 < cost3 and rCD >=cost3 and rBC>0: #rCE rBC rCD
                #print('t CE BC CD')
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD-cost3,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD #rCE rBC rCD rAC
                if 0 < cost4 and rAC >=cost4 and rCD>0: #rCE rBC rCD rAC
                    #print('t CE BC CD AC')
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'AC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        #print('t CE BC CD AC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rCD >=cost2 and rCE>0:#rCE rCD
            #print('t CE CD')
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD-cost2,   0,  rDE, rA, rB, rC, rD, rE) 
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rAC >=cost3 and rCD>0: #rCE rCD rAC
                #print('t CE CD AC')
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE, rBC, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC #rCE rCD rAC rBC
                if 0 < cost4 and rBC >=cost4 and rAC>0: #rCE rCD rAC rBC
                    #print('t CE CD AC BC')
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AC', rAC)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rC:
                        #print('t CE CD AC BC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rBC >=cost3 and rCD>0: #rCE rCD rBC
                #print('t CE CD BC')
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rCE rCD rBC rAC
                if 0 < cost4 and rAC >=cost4 and rBC>0: #rCE rCD rBC rAC
                    #print('t CE CD BC AC')
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE) 
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'AC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        #print('t CE CD BC AC C')
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE, 0, rBD, rBE,   0,   0,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
    if cost1 == 0:
        ret=testC(ccost, dcost, ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE,rBD, rBE,  rDE, rA, rB, rC, rD, rE)
    print("End testC")
    return(ret)

###############################################################################################################################3

def testB(cost1, ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE):
    ret=[]
    
    if 0 < cost1 and rAB >=cost1:
        tail=testC(ccost, dcost, ecost, rAB-cost1, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'AB', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rAB
        if 0 < cost2 and rBC >=cost2 and rAB>0: #rAB rBC
            print('AB BC')
            tail=testC(ccost, dcost, ecost, 0, rAC, rAD, rAE, rBC-cost2, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AB', rAB)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rBD >=cost3 and rBC>0: #rAB rBC rBD
                print("AB BC BD")
                tail=testC(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, rBD-cost3, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    print("")
                    myinsert(x, 'AB', rAB)

                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rBE >=cost4 and rBD>0: #rAB rBC rBD rBE
                    tail=testC(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, rBE-cost4,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AB', rAB)

                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC #rAB rBC rBE
            if 0 < cost3 and rBE >=cost3 and rBC>0: #rAB rBC rBE
                tail=testC(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, rBD, rBE-cost3,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)

                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rBD >=cost4 and rBE>0: #rAB rBC rBE rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AB', rAB)

                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBD >=cost2 and rAB>0:#rAB rBD
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost2, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AB', rAB)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rBC >=cost3 and rBD>0: #rAB rBD rBC
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3,   0, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rAB rBD rBC rBE
                if 0 < cost4 and rBE >=cost4 and rBC>0: #rAB rBD rBC rBE
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BD', rBD)

                        myinsert(x, 'BC', rBC)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD #rAB rBD rBE
            if 0 < cost3 and rBE >=cost3 and rBD>0: #rAB rBD rBE
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC,   0, rBE-cost3,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE #rAB rBD rBE rBC
                if 0 < cost4 and rBC >=cost4 and rBE>0: #rAB rBD rBE rBC
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBE >=cost2 and rAB>0: #rAB rBE
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD, rBE-cost2,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AB', rAB)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rBC >=cost3 and rBE>0: #rAB rBE rBC
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3, rBD,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rAB rBE rBC rBD
                if 0 < cost4 and rBD >=cost4 and rBC>0: #rAB rBE rBC rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BE', rBE)

                        myinsert(x, 'BC', rBC)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rBD >=cost3 and rBE>0: #rAB rBE rBD
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD-cost3,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD #rAB rBE rBD rBC
                print('AB BE BD BC', rBC)
                if 0 < cost4 and rBC >=cost4 and rBD>0: #rAB rBE rBD rBC
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

    if 0 < cost1 and rBC >=cost1: #rBC
        #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,      rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost1, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BC', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBC
        if 0 < cost2 and rAB >=cost2 and rBC>0: #rBC rAB
            #print("t BC AB")
            #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB-cost2, rAC, rAD, rAE,   0, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            testy=True
            for x in tail:
                if testy:
                    testy=False
                    myadd(x, 'test', 8)
                    x.update({'dog':9})
            print('end')
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'AB', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAB
            if 0 < cost3 and rBD >=cost3 and rAB>0: #rBC rAB rBD
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost3, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD #rBC rAB rBD rBE
                if 0 < cost4 and rBE >=cost4 and rBD>0: #rBC rAB rBD rBE
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAB
            if 0 < cost3 and rBE >=cost3 and rAB>0: #rBC rAB rBE
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD, rBE-cost3,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE #rBC rAB rBE rBD
                if 0 < cost4 and rBD >=cost4 and rBE>0: #rBC rAB rBE rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBD >=cost2 and rBC>0:#rBC rBD
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD-cost2, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rAB >=cost3 and rBD>0: #rBC rBD rAB
                #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0,   0, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB #rBC rBD rAB rBE
                if 0 < cost4 and rBE >=cost4 and rAB>0: #rBC rBD rAB rBE
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AB', rAB)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD #rBC rBD rBE
            if 0 < cost3 and rBE >=cost3 and rBD>0: #rBC rBD rBE
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0,   0, rBE-cost3,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE #rBC rBD rBE rAB
                if 0 < cost4 and rAB >=cost4 and rBE>0: #rBC rBD rBE rAB
                    #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'AB', cost3)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBE >=cost2 and rBC>0:#rBC rBE
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE-cost2,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rAB >=cost3 and rBE>0: #rBC rBE rAB
                #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0, rBD,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB #rBC rBE rAB rBD
                if 0 < cost4 and rBD >=cost4 and rAB>0: #rBC rBE rAB rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AB', rAB)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE #rBC rBE rBD
            if 0 < cost3 and rBD >=cost3 and rBE>0: #rBC rBE rBD
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD-cost3,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD #rBC rBE rBD rAB
                if 0 < cost4 and rAB >=cost4 and rBD>0: #rBC rBE rBD rAB
                    #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'AB', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

    if 0 < cost1 and rBD >=cost1:
        #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,      rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost1, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBD
        if 0 < cost2 and rAB >=cost2 and rBD>0:#rBD rAB
            #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB-cost2, rAC, rAD, rAE, rBC,   0, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'AB', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAB
            if 0 < cost3 and rBC >=cost3 and rAB>0: #rBD rAB rBC
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3,   0, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rBD rAB rBC rBE
                if 0 < cost4 and rBE >=cost4 and rBC>0: #rBD rAB rBC rBE
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAB
            if 0 < cost3 and rBE >=cost3 and rAB>0: #rBD rAB rBE
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC,   0, rBE-cost3,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE #rBD rAB rBE rBC
                if 0 < cost4 and rBC >=cost4 and rBE>0: #rBD rAB rBE rBC
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBC >=cost2 and rBD>0:#rBD rBC
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2,   0, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAB >=cost3 and rBC>0: #rBD rBC rAB
                #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0,   0, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB #rBD rBC rAB rBE
                if 0 < cost4 and rBE >=cost4 and rAB>0: #rBD rBC rAB rBE
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AB', rAB)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rBE >=cost3 and rBC>0: #rBD rBC rBE
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0,   0, rBE-cost3,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE #rBD rBC rBE rAB
                if 0 < cost4 and rAB >=cost4 and rBE>0: #rBD rBC rBE rAB
                    #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'AB', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBE >=cost2 and rBD>0:#rBD rBE
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,       rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE-cost2,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rAB >=cost3 and rBE>0: #rBD rBE rAB
                #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE, rBC,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB #rBD rBE rAB rBC
                if 0 < cost4 and rBC >=cost4 and rAB>0: #rBD rBE rAB rBC
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AB', rAB)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE #rBD rBE rBC
            if 0 < cost3 and rBC >=cost3 and rBE>0: #rBD rBE rBC
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rBD rBE rBC rAB
                if 0 < cost4 and rAB >=cost4 and rBC>0: #rBD rBE rBC rAB
                    #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BC', rBC)
                        myadd(x, 'AB', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

    if 0 < cost1  and rBE >=cost1 :
        #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD,      rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE-cost1,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBE
        if 0 < cost2 and rAB >=cost2 and rBE>0:#rBE rAB
            #def testC(ccost, dcost, ecost, rAB      , rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB-cost2, rAC, rAD, rAE, rBC, rBD,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'AB', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAB
            if 0 < cost3 and rBC >=cost3 and rAB>0: #rBE rAB rBC
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3, rBD,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rBE rAB rBC rBD
                if 0 < cost4 and rBD >=cost4 and rBC>0: #rBE rAB rBC rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AB', rAB)

                        myinsert(x, 'BC', rBC)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            if 0 < cost3 and rBD >=cost3 and rAB>0: #rBE rAB rBD
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD-cost3,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD #rBE rAB rBD rBC
                if 0 < cost4 and rBC >=cost4 and rBD>0: #rBE rAB rBD rBC
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AB', rAB)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBC >=cost2 and rBE>0:#rBE rBC
            #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2, rBD,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAB >=cost3 and rBC>0: #rBE rBC rAB
                #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0, rBD,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB #rBE rBC rAB rBD
                if 0 < cost4 and rBD >=cost4 and rAB>0: #rBE rBC rAB rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'AB', rAB)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            if 0 < cost3 and rBD >=cost3 and rBC>0: #rBE rBC rBD
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD-cost3,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD #rBE rBC rBD rAB
                if 0 < cost4 and rAB >=cost4 and rBD>0: #rBE rBC rBD rAB
                    #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'AB', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)

        if 0 < cost2 and rBD >=cost2 and rBE>0:#rBE rBD
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,       rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost2,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'BD', cost2)
                        if not(x in ret):
                            ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rAB >=cost3 and rBD>0: #rBE rBD rAB
                #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE, rBC,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB #rBE rBD rAB rBC
                if 0 < cost4 and rBC >=cost4 and rAB>0: #rBE rBD rAB rBC
                    #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AB', rAB)
                        myadd(x, 'BC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBC
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rBC >=cost3 and rBD>0: #rBE rBD rBC
                #def testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,       rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC #rBE rBD rBC rAB
                if 0 < cost4 and rAB >=cost4 and rBC>0: #rBE rBD rBC rAB
                    #def testC(ccost, dcost, ecost,       rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'BD', rBD)

                        myinsert(x, 'BC', rBC)
                        myadd(x, 'AB', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testc(ccost, dcost, ecost, 0, rAC, rAD, rAE, 0, 0, 0,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)

                            if not(x in ret):
                                ret.append(x)
    if cost1 == 0:
        ret=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
    return(ret)
#        ret=t bc cc dc ec, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
x=testB(10, 1, 0, 0,  10,   0,   0,   0,   5,   6,   4,  0, 0, 0 ,0,0,4,0,0)
for y in x:
    print(x.count(y), "=", y)
