import pdb
def myadd(xhash, xkey, x):
 #   print("adding ",xkey, "=",x," to ",xhash)
    if xkey in xhash:
        xhash.update({xkey: xhash[xkey]+x})
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

def testE(cost1, rAB, rAC, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE):
    ret=[]

    if 0 < cost1 and rAE >=cost1:
        tail=[dict()]
        for x in tail:
            myadd(x, 'AE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rAE
        if 0 < cost2 and rBE >=cost2 and rAE>0: #rAE rBE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'AE', rAE)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rCE >=cost3 and rBE>0: #rAE rBE rCE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'AE', rAE)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rDE >=cost4 and rCE>0: #rAE rBE rCE rDE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rDE >=cost3 and rBE>0: #rAE rBE rDE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'AE', rAE)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rCE >=cost4 and rDE>0: #rAE rBE rDE rCE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAE
        if 0 < cost2 and rCE >=cost2 and rAE>0: #rAE rCE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'AE', rAE)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rBE >=cost3 and rCE>0: #rAE rCE rBE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'AE', rAE)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rDE >=cost4 and rBE>0: #rAE rCE rBE rDE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rDE >=cost3 and rCE>0: #rAE rCE rDE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'AE', rAE)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rBE >=cost4 and rDE>0: #rAE rCE rDE rBE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAE
        if 0 < cost2 and rDE >=cost2 and rAE>0: #rAE rDE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'AE', rAE)
                myadd(x, 'DE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rDE
            if 0 < cost3 and rBE >=cost3 and rDE>0: #rAE rDE rBE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'AE', rAE)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rCE >=cost4 and rBE>0: #rAE rDE rBE rCE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rDE
            if 0 < cost3 and rCE >=cost3 and rDE>0: #rAE rDE rCE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'AE', rAE)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rBE >=cost4 and rCE>0: #rAE rDE rCE rBE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBE >=cost1:
        tail=[dict()]
        for x in tail:
            myadd(x, 'BE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBE
        if 0 < cost2 and rAE >=cost2 and rBE>0: #rBE rAE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'AE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAE
            if 0 < cost3 and rCE >=cost3 and rAE>0: #rBE rAE rCE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'AE', rAE)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rDE >=cost4 and rCE>0: #rBE rAE rCE rDE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAE
            if 0 < cost3 and rDE >=cost3 and rAE>0: #rBE rAE rDE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'AE', rAE)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rCE >=cost4 and rDE>0: #rBE rAE rDE rCE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBE
        if 0 < cost2 and rCE >=cost2 and rBE>0: #rBE rCE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rAE >=cost3 and rCE>0: #rBE rCE rAE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'AE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAE
                if 0 < cost4 and rDE >=cost4 and rAE>0: #rBE rCE rAE rDE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AE', rAE)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rDE >=cost3 and rCE>0: #rBE rCE rDE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rAE >=cost4 and rDE>0: #rBE rCE rDE rAE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'AE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBE
        if 0 < cost2 and rDE >=cost2 and rBE>0: #rBE rDE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'DE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rDE
            if 0 < cost3 and rAE >=cost3 and rDE>0: #rBE rDE rAE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'AE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAE
                if 0 < cost4 and rCE >=cost4 and rAE>0: #rBE rDE rAE rCE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AE', rAE)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rDE
            if 0 < cost3 and rCE >=cost3 and rDE>0: #rBE rDE rCE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rAE >=cost4 and rCE>0: #rBE rDE rCE rAE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'AE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rCE >=cost1:
        tail=[dict()]
        for x in tail:
            myadd(x, 'CE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rCE
        if 0 < cost2 and rAE >=cost2 and rCE>0: #rCE rAE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'AE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAE
            if 0 < cost3 and rBE >=cost3 and rAE>0: #rCE rAE rBE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'AE', rAE)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rDE >=cost4 and rBE>0: #rCE rAE rBE rDE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAE
            if 0 < cost3 and rDE >=cost3 and rAE>0: #rCE rAE rDE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'AE', rAE)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rBE >=cost4 and rDE>0: #rCE rAE rDE rBE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCE
        if 0 < cost2 and rBE >=cost2 and rCE>0: #rCE rBE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rAE >=cost3 and rBE>0: #rCE rBE rAE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'AE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAE
                if 0 < cost4 and rDE >=cost4 and rAE>0: #rCE rBE rAE rDE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AE', rAE)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rDE >=cost3 and rBE>0: #rCE rBE rDE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rAE >=cost4 and rDE>0: #rCE rBE rDE rAE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'AE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCE
        if 0 < cost2 and rDE >=cost2 and rCE>0: #rCE rDE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'DE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rDE
            if 0 < cost3 and rAE >=cost3 and rDE>0: #rCE rDE rAE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'AE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAE
                if 0 < cost4 and rBE >=cost4 and rAE>0: #rCE rDE rAE rBE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AE', rAE)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rDE
            if 0 < cost3 and rBE >=cost3 and rDE>0: #rCE rDE rBE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rAE >=cost4 and rBE>0: #rCE rDE rBE rAE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'AE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rDE >=cost1:
        tail=[dict()]
        for x in tail:
            myadd(x, 'DE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rDE
        if 0 < cost2 and rAE >=cost2 and rDE>0: #rDE rAE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'DE', rDE)
                myadd(x, 'AE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAE
            if 0 < cost3 and rBE >=cost3 and rAE>0: #rDE rAE rBE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'AE', rAE)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rCE >=cost4 and rBE>0: #rDE rAE rBE rCE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAE
            if 0 < cost3 and rCE >=cost3 and rAE>0: #rDE rAE rCE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'AE', rAE)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rBE >=cost4 and rCE>0: #rDE rAE rCE rBE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AE', rAE)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rDE
        if 0 < cost2 and rBE >=cost2 and rDE>0: #rDE rBE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'DE', rDE)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rAE >=cost3 and rBE>0: #rDE rBE rAE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'AE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAE
                if 0 < cost4 and rCE >=cost4 and rAE>0: #rDE rBE rAE rCE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'AE', rAE)
                        myadd(x, 'CE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rCE >=cost3 and rBE>0: #rDE rBE rCE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rAE >=cost4 and rCE>0: #rDE rBE rCE rAE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BE', rBE)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'AE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rDE
        if 0 < cost2 and rCE >=cost2 and rDE>0: #rDE rCE
            tail=[dict()]
            for x in tail:
                myinsert(x, 'DE', rDE)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rAE >=cost3 and rCE>0: #rDE rCE rAE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'AE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAE
                if 0 < cost4 and rBE >=cost4 and rAE>0: #rDE rCE rAE rBE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'AE', rAE)
                        myadd(x, 'BE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rBE >=cost3 and rCE>0: #rDE rCE rBE
                tail=[dict()]
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rAE >=cost4 and rBE>0: #rDE rCE rBE rAE
                    tail=[dict()]
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CE', rCE)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'AE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAE
                    if cost5<=rE:
                        tail=[dict()]
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AE', rAE)
                            myinsert(x, 'E', cost5)
                            if not(x in ret):
                                ret.append(x)
    if cost1 == 0:
        ret=[dict()]
    return(ret)
#####################################################################################################################################

def testD(cost1, ecost, rAB, rAC, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE):
    ret=[]

    if 0 < cost1 and rAD >=cost1:
        tail=testE(ecost, rAB, rAC, rAD-cost1, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'AD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rAD
        if 0 < cost2 and rBD >=cost2 and rAD>0: #rAD rBD
            tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost2, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AD', rAD)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rCD >=cost3 and rBD>0: #rAD rBD rCD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost3, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AD', rAD)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rDE >=cost4 and rCD>0: #rAD rBD rCD rDE
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE, rDE-cost4, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rDE >=cost3 and rBD>0: #rAD rBD rDE
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD, rCE, rDE-cost3, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AD', rAD)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rCD >=cost4 and rDE>0: #rAD rBD rDE rCD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost4, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAD
        if 0 < cost2 and rCD >=cost2 and rAD>0: #rAD rCD
            tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD, rBE, rCD-cost2, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AD', rAD)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rBD >=cost3 and rCD>0: #rAD rCD rBD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost3, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AD', rAD)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rDE >=cost4 and rBD>0: #rAD rCD rBD rDE
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE, rDE-cost4, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rDE >=cost3 and rCD>0: #rAD rCD rDE
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD, rBE,   0, rCE, rDE-cost3, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AD', rAD)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rBD >=cost4 and rDE>0: #rAD rCD rDE rBD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost4, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAD
        if 0 < cost2 and rDE >=cost2 and rAD>0: #rAD rDE
            tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD, rBE, rCD, rCE, rDE-cost2, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AD', rAD)
                myadd(x, 'DE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rDE
            if 0 < cost3 and rBD >=cost3 and rDE>0: #rAD rDE rBD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost3, rBE, rCD, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AD', rAD)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rCD >=cost4 and rBD>0: #rAD rDE rBD rCD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost4, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rDE
            if 0 < cost3 and rCD >=cost3 and rDE>0: #rAD rDE rCD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD, rBE, rCD-cost3, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AD', rAD)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rBD >=cost4 and rCD>0: #rAD rDE rCD rBD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost4, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBD >=cost1:
        tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost1, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBD
        if 0 < cost2 and rAD >=cost2 and rBD>0: #rBD rAD
            tail=testE(ecost, rAB, rAC, rAD-cost2, rAE, rBC,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'AD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAD
            if 0 < cost3 and rCD >=cost3 and rAD>0: #rBD rAD rCD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost3, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'AD', rAD)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rDE >=cost4 and rCD>0: #rBD rAD rCD rDE
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE, rDE-cost4, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAD
            if 0 < cost3 and rDE >=cost3 and rAD>0: #rBD rAD rDE
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD, rCE, rDE-cost3, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'AD', rAD)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rCD >=cost4 and rDE>0: #rBD rAD rDE rCD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost4, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBD
        if 0 < cost2 and rCD >=cost2 and rBD>0: #rBD rCD
            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE, rCD-cost2, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rAD >=cost3 and rCD>0: #rBD rCD rAD
                tail=testE(ecost, rAB, rAC, rAD-cost3, rAE, rBC,   0, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'AD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAD
                if 0 < cost4 and rDE >=cost4 and rAD>0: #rBD rCD rAD rDE
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE, rDE-cost4, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AD', rAD)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rDE >=cost3 and rCD>0: #rBD rCD rDE
                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE,   0, rCE, rDE-cost3, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rAD >=cost4 and rDE>0: #rBD rCD rDE rAD
                    tail=testE(ecost, rAB, rAC, rAD-cost4, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'AD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBD
        if 0 < cost2 and rDE >=cost2 and rBD>0: #rBD rDE
            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE, rCD, rCE, rDE-cost2, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'DE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rDE
            if 0 < cost3 and rAD >=cost3 and rDE>0: #rBD rDE rAD
                tail=testE(ecost, rAB, rAC, rAD-cost3, rAE, rBC,   0, rBE, rCD, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'AD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAD
                if 0 < cost4 and rCD >=cost4 and rAD>0: #rBD rDE rAD rCD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost4, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AD', rAD)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rDE
            if 0 < cost3 and rCD >=cost3 and rDE>0: #rBD rDE rCD
                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE, rCD-cost3, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rAD >=cost4 and rCD>0: #rBD rDE rCD rAD
                    tail=testE(ecost, rAB, rAC, rAD-cost4, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'AD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rCD >=cost1:
        tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD-cost1, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'CD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rCD
        if 0 < cost2 and rAD >=cost2 and rCD>0: #rCD rAD
            tail=testE(ecost, rAB, rAC, rAD-cost2, rAE, rBC, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'AD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAD
            if 0 < cost3 and rBD >=cost3 and rAD>0: #rCD rAD rBD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost3, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'AD', rAD)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rDE >=cost4 and rBD>0: #rCD rAD rBD rDE
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE, rDE-cost4, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAD
            if 0 < cost3 and rDE >=cost3 and rAD>0: #rCD rAD rDE
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD, rBE,   0, rCE, rDE-cost3, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'AD', rAD)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rBD >=cost4 and rDE>0: #rCD rAD rDE rBD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost4, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCD
        if 0 < cost2 and rBD >=cost2 and rCD>0: #rCD rBD
            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost2, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rAD >=cost3 and rBD>0: #rCD rBD rAD
                tail=testE(ecost, rAB, rAC, rAD-cost3, rAE, rBC,   0, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'AD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAD
                if 0 < cost4 and rDE >=cost4 and rAD>0: #rCD rBD rAD rDE
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE, rDE-cost4, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AD', rAD)
                        myadd(x, 'DE', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rDE
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rDE >=cost3 and rBD>0: #rCD rBD rDE
                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE,   0, rCE, rDE-cost3, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'DE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rDE
                if 0 < cost4 and rAD >=cost4 and rDE>0: #rCD rBD rDE rAD
                    tail=testE(ecost, rAB, rAC, rAD-cost4, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'DE', rDE)
                        myadd(x, 'AD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCD
        if 0 < cost2 and rDE >=cost2 and rCD>0: #rCD rDE
            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,   0, rCE, rDE-cost2, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'DE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rDE
            if 0 < cost3 and rAD >=cost3 and rDE>0: #rCD rDE rAD
                tail=testE(ecost, rAB, rAC, rAD-cost3, rAE, rBC, rBD, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'AD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAD
                if 0 < cost4 and rBD >=cost4 and rAD>0: #rCD rDE rAD rBD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost4, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AD', rAD)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rDE
            if 0 < cost3 and rBD >=cost3 and rDE>0: #rCD rDE rBD
                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost3, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'DE', rDE)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rAD >=cost4 and rBD>0: #rCD rDE rBD rAD
                    tail=testE(ecost, rAB, rAC, rAD-cost4, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'AD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rDE >=cost1:
        tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE-cost1, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'DE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rDE
        if 0 < cost2 and rAD >=cost2 and rDE>0: #rDE rAD
            tail=testE(ecost, rAB, rAC, rAD-cost2, rAE, rBC, rBD, rBE, rCD, rCE,   0, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'DE', rDE)
                myadd(x, 'AD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAD
            if 0 < cost3 and rBD >=cost3 and rAD>0: #rDE rAD rBD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost3, rBE, rCD, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'AD', rAD)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rCD >=cost4 and rBD>0: #rDE rAD rBD rCD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost4, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAD
            if 0 < cost3 and rCD >=cost3 and rAD>0: #rDE rAD rCD
                tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD, rBE, rCD-cost3, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'AD', rAD)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rBD >=cost4 and rCD>0: #rDE rAD rCD rBD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost4, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'AD', rAD)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rDE
        if 0 < cost2 and rBD >=cost2 and rDE>0: #rDE rBD
            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost2, rBE, rCD, rCE,   0, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'DE', rDE)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rAD >=cost3 and rBD>0: #rDE rBD rAD
                tail=testE(ecost, rAB, rAC, rAD-cost3, rAE, rBC,   0, rBE, rCD, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'AD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAD
                if 0 < cost4 and rCD >=cost4 and rAD>0: #rDE rBD rAD rCD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE, rCD-cost4, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'AD', rAD)
                        myadd(x, 'CD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rCD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rCD >=cost3 and rBD>0: #rDE rBD rCD
                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE, rCD-cost3, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rAD >=cost4 and rCD>0: #rDE rBD rCD rAD
                    tail=testE(ecost, rAB, rAC, rAD-cost4, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'CD', rCD)
                        myadd(x, 'AD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rDE
        if 0 < cost2 and rCD >=cost2 and rDE>0: #rDE rCD
            tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD-cost2, rCE,   0, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'DE', rDE)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rAD >=cost3 and rCD>0: #rDE rCD rAD
                tail=testE(ecost, rAB, rAC, rAD-cost3, rAE, rBC, rBD, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'AD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAD
                if 0 < cost4 and rBD >=cost4 and rAD>0: #rDE rCD rAD rBD
                    tail=testE(ecost, rAB, rAC,   0, rAE, rBC, rBD-cost4, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'AD', rAD)
                        myadd(x, 'BD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rBD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rBD >=cost3 and rCD>0: #rDE rCD rBD
                tail=testE(ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost3, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'DE', rDE)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rAD >=cost4 and rBD>0: #rDE rCD rBD rAD
                    tail=testE(ecost, rAB, rAC, rAD-cost4, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'DE', rDE)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'BD', rBD)
                        myadd(x, 'AD', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAD
                    if cost5<=rD:
                        tail=testE(ecost, rAB, rAC,   0, rAE, rBC,   0, rBE,   0, rCE,   0, rA, rB, rC, rD-cost5, rE,)
                        for x in tail:
                            myinsert(x, 'DE', rDE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AD', rAD)
                            myinsert(x, 'D', cost5)
                            if not(x in ret):
                                ret.append(x)
    if cost1 == 0:
        ret=testE(ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE)
    return(ret)
#####################################################################################################################################


def testC(cost1, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE):
    ret=[]

    if 0 < cost1 and rAC >=cost1:
        tail=testD(dcost, ecost, rAB, rAC-cost1, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'AC', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rAC
        if 0 < cost2 and rBC >=cost2 and rAC>0: #rAC rBC
            tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost2, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AC', rAC)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rCD >=cost3 and rBC>0: #rAC rBC rCD
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost3, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rCE >=cost4 and rCD>0: #rAC rBC rCD rCE
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rCE >=cost3 and rBC>0: #rAC rBC rCE
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD, rCE-cost3, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rCD >=cost4 and rCE>0: #rAC rBC rCE rCD
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAC
        if 0 < cost2 and rCD >=cost2 and rAC>0: #rAC rCD
            tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD-cost2, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AC', rAC)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rBC >=cost3 and rCD>0: #rAC rCD rBC
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rCE >=cost4 and rBC>0: #rAC rCD rBC rCE
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rCE >=cost3 and rCD>0: #rAC rCD rCE
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE,   0, rCE-cost3, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rBC >=cost4 and rCE>0: #rAC rCD rCE rBC
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAC
        if 0 < cost2 and rCE >=cost2 and rAC>0: #rAC rCE
            tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD, rCE-cost2, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AC', rAC)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rBC >=cost3 and rCE>0: #rAC rCE rBC
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE, rCD,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rCD >=cost4 and rBC>0: #rAC rCE rBC rCD
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rCD >=cost3 and rCE>0: #rAC rCE rCD
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD-cost3,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AC', rAC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rBC >=cost4 and rCD>0: #rAC rCE rCD rBC
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBC >=cost1:
        tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost1, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BC', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBC
        if 0 < cost2 and rAC >=cost2 and rBC>0: #rBC rAC
            tail=testD(dcost, ecost, rAB, rAC-cost2, rAD, rAE,   0, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'AC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAC
            if 0 < cost3 and rCD >=cost3 and rAC>0: #rBC rAC rCD
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost3, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rCE >=cost4 and rCD>0: #rBC rAC rCD rCE
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAC
            if 0 < cost3 and rCE >=cost3 and rAC>0: #rBC rAC rCE
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD, rCE-cost3, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rCD >=cost4 and rCE>0: #rBC rAC rCE rCD
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBC
        if 0 < cost2 and rCD >=cost2 and rBC>0: #rBC rCD
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD-cost2, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rAC >=cost3 and rCD>0: #rBC rCD rAC
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC
                if 0 < cost4 and rCE >=cost4 and rAC>0: #rBC rCD rAC rCE
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rCE >=cost3 and rCD>0: #rBC rCD rCE
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE,   0, rCE-cost3, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rAC >=cost4 and rCE>0: #rBC rCD rCE rAC
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'CD', rCD)
                        myinsert(x, 'CE', rCE)
                        myadd(x, 'AC', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAC
                    if cost5<=rC:
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBC
        if 0 < cost2 and rCE >=cost2 and rBC>0: #rBC rCE
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD, rCE-cost2, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rAC >=cost3 and rCE>0: #rBC rCE rAC
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE, rCD,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC
                if 0 < cost4 and rCD >=cost4 and rAC>0: #rBC rCE rAC rCD
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rCD >=cost3 and rCE>0: #rBC rCE rCD
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD-cost3,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rAC >=cost4 and rCD>0: #rBC rCE rCD rAC
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rCD >=cost1:
        tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD-cost1, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'CD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rCD
        if 0 < cost2 and rAC >=cost2 and rCD>0: #rCD rAC
            tail=testD(dcost, ecost, rAB, rAC-cost2, rAD, rAE, rBC, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'AC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAC
            if 0 < cost3 and rBC >=cost3 and rAC>0: #rCD rAC rBC
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rCE >=cost4 and rBC>0: #rCD rAC rBC rCE
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAC
            if 0 < cost3 and rCE >=cost3 and rAC>0: #rCD rAC rCE
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE,   0, rCE-cost3, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rBC >=cost4 and rCE>0: #rCD rAC rCE rBC
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCD
        if 0 < cost2 and rBC >=cost2 and rCD>0: #rCD rBC
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAC >=cost3 and rBC>0: #rCD rBC rAC
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE,   0, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC
                if 0 < cost4 and rCE >=cost4 and rAC>0: #rCD rBC rAC rCE
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0, rCE-cost4, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rCE >=cost3 and rBC>0: #rCD rBC rCE
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE,   0, rCE-cost3, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCE
                if 0 < cost4 and rAC >=cost4 and rCE>0: #rCD rBC rCE rAC
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCD
        if 0 < cost2 and rCE >=cost2 and rCD>0: #rCD rCE
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE,   0, rCE-cost2, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CD', rCD)
                myadd(x, 'CE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCE
            if 0 < cost3 and rAC >=cost3 and rCE>0: #rCD rCE rAC
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE, rBC, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC
                if 0 < cost4 and rBC >=cost4 and rAC>0: #rCD rCE rAC rBC
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCE
            if 0 < cost3 and rBC >=cost3 and rCE>0: #rCD rCE rBC
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CD', rCD)
                    myinsert(x, 'CE', rCE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rAC >=cost4 and rBC>0: #rCD rCE rBC rAC
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rCE >=cost1:
        tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE-cost1, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'CE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rCE
        if 0 < cost2 and rAC >=cost2 and rCE>0: #rCE rAC
            tail=testD(dcost, ecost, rAB, rAC-cost2, rAD, rAE, rBC, rBD, rBE, rCD,   0, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'AC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAC
            if 0 < cost3 and rBC >=cost3 and rAC>0: #rCE rAC rBC
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost3, rBD, rBE, rCD,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rCD >=cost4 and rBC>0: #rCE rAC rBC rCD
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAC
            if 0 < cost3 and rCD >=cost3 and rAC>0: #rCE rAC rCD
                tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC, rBD, rBE, rCD-cost3,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'AC', rAC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rBC >=cost4 and rCD>0: #rCE rAC rCD rBC
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCE
        if 0 < cost2 and rBC >=cost2 and rCE>0: #rCE rBC
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2, rBD, rBE, rCD,   0, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAC >=cost3 and rBC>0: #rCE rBC rAC
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE,   0, rBD, rBE, rCD,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC
                if 0 < cost4 and rCD >=cost4 and rAC>0: #rCE rBC rAC rCD
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE, rCD-cost4,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rCD >=cost3 and rBC>0: #rCE rBC rCD
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE, rCD-cost3,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'CD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rCD
                if 0 < cost4 and rAC >=cost4 and rCD>0: #rCE rBC rCD rAC
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rCE
        if 0 < cost2 and rCD >=cost2 and rCE>0: #rCE rCD
            tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD-cost2,   0, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'CE', rCE)
                myadd(x, 'CD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rCD
            if 0 < cost3 and rAC >=cost3 and rCD>0: #rCE rCD rAC
                tail=testD(dcost, ecost, rAB, rAC-cost3, rAD, rAE, rBC, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'AC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAC
                if 0 < cost4 and rBC >=cost4 and rAC>0: #rCE rCD rAC rBC
                    tail=testD(dcost, ecost, rAB,   0, rAD, rAE, rBC-cost4, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rCD
            if 0 < cost3 and rBC >=cost3 and rCD>0: #rCE rCD rBC
                tail=testD(dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'CE', rCE)
                    myinsert(x, 'CD', rCD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rAC >=cost4 and rBC>0: #rCE rCD rBC rAC
                    tail=testD(dcost, ecost, rAB, rAC-cost4, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC, rD, rE)
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
                        tail=testD(dcost, ecost, rAB,   0, rAD, rAE,   0, rBD, rBE,   0,   0, rDE, rA, rB, rC-cost5, rD, rE,)
                        for x in tail:
                            myinsert(x, 'CE', rCE)
                            myinsert(x, 'CD', rCD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AC', rAC)
                            myinsert(x, 'C', cost5)
                            if not(x in ret):
                                ret.append(x)
    if cost1 == 0:
        ret=testD(dcost, ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE)
    return(ret)
#####################################################################################################################################

###############################################################################################################################3
def testB(cost1, ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE):
    ret=[]

    if 0 < cost1 and rAB >=cost1:
        tail=testC(ccost, dcost, ecost, rAB-cost1, rAC, rAD, rAE, rBC, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'AB', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rAB
        if 0 < cost2 and rBC >=cost2 and rAB>0: #rAB rBC
            tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost2, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AB', rAB)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rBD >=cost3 and rBC>0: #rAB rBC rBD
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost3, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rBE >=cost4 and rBD>0: #rAB rBC rBD rBE
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rBE >=cost3 and rBC>0: #rAB rBC rBE
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD, rBE-cost3, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rBD >=cost4 and rBE>0: #rAB rBC rBE rBD
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAB
        if 0 < cost2 and rBD >=cost2 and rAB>0: #rAB rBD
            tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD-cost2, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AB', rAB)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rBC >=cost3 and rBD>0: #rAB rBD rBC
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rBE >=cost4 and rBC>0: #rAB rBD rBC rBE
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rBE >=cost3 and rBD>0: #rAB rBD rBE
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC,   0, rBE-cost3, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rBC >=cost4 and rBE>0: #rAB rBD rBE rBC
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rAB
        if 0 < cost2 and rBE >=cost2 and rAB>0: #rAB rBE
            tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD, rBE-cost2, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'AB', rAB)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rBC >=cost3 and rBE>0: #rAB rBE rBC
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3, rBD,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rBD >=cost4 and rBC>0: #rAB rBE rBC rBD
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rBD >=cost3 and rBE>0: #rAB rBE rBD
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD-cost3,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'AB', rAB)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rBC >=cost4 and rBD>0: #rAB rBE rBD rBC
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBC >=cost1:
        tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost1, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BC', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBC
        if 0 < cost2 and rAB >=cost2 and rBC>0: #rBC rAB
            tail=testC(ccost, dcost, ecost, rAB-cost2, rAC, rAD, rAE,   0, rBD, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'AB', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAB
            if 0 < cost3 and rBD >=cost3 and rAB>0: #rBC rAB rBD
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost3, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rBE >=cost4 and rBD>0: #rBC rAB rBD rBE
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAB
            if 0 < cost3 and rBE >=cost3 and rAB>0: #rBC rAB rBE
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD, rBE-cost3, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rBD >=cost4 and rBE>0: #rBC rAB rBE rBD
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBC
        if 0 < cost2 and rBD >=cost2 and rBC>0: #rBC rBD
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD-cost2, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rAB >=cost3 and rBD>0: #rBC rBD rAB
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB
                if 0 < cost4 and rBE >=cost4 and rAB>0: #rBC rBD rAB rBE
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rBE >=cost3 and rBD>0: #rBC rBD rBE
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0,   0, rBE-cost3, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rAB >=cost4 and rBE>0: #rBC rBD rBE rAB
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                    for x in tail:
                        myinsert(x, 'BC', rBC)
                        myinsert(x, 'BD', rBD)
                        myinsert(x, 'BE', rBE)
                        myadd(x, 'AB', cost4)
                        if not(x in ret):
                            ret.append(x)
                else:
                    cost5=80+cost4-rAB
                    if cost5<=rB:
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBC
        if 0 < cost2 and rBE >=cost2 and rBC>0: #rBC rBE
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD, rBE-cost2, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BC', rBC)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rAB >=cost3 and rBE>0: #rBC rBE rAB
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0, rBD,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB
                if 0 < cost4 and rBD >=cost4 and rAB>0: #rBC rBE rAB rBD
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rBD >=cost3 and rBE>0: #rBC rBE rBD
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD-cost3,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BC', rBC)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rAB >=cost4 and rBD>0: #rBC rBE rBD rAB
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBD >=cost1:
        tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost1, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BD', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBD
        if 0 < cost2 and rAB >=cost2 and rBD>0: #rBD rAB
            tail=testC(ccost, dcost, ecost, rAB-cost2, rAC, rAD, rAE, rBC,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'AB', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAB
            if 0 < cost3 and rBC >=cost3 and rAB>0: #rBD rAB rBC
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rBE >=cost4 and rBC>0: #rBD rAB rBC rBE
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAB
            if 0 < cost3 and rBE >=cost3 and rAB>0: #rBD rAB rBE
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC,   0, rBE-cost3, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rBC >=cost4 and rBE>0: #rBD rAB rBE rBC
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBD
        if 0 < cost2 and rBC >=cost2 and rBD>0: #rBD rBC
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAB >=cost3 and rBC>0: #rBD rBC rAB
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0,   0, rBE, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB
                if 0 < cost4 and rBE >=cost4 and rAB>0: #rBD rBC rAB rBE
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0, rBE-cost4, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rBE >=cost3 and rBC>0: #rBD rBC rBE
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0,   0, rBE-cost3, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BE', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBE
                if 0 < cost4 and rAB >=cost4 and rBE>0: #rBD rBC rBE rAB
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBD
        if 0 < cost2 and rBE >=cost2 and rBD>0: #rBD rBE
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC,   0, rBE-cost2, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BD', rBD)
                myadd(x, 'BE', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBE
            if 0 < cost3 and rAB >=cost3 and rBE>0: #rBD rBE rAB
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE, rBC,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB
                if 0 < cost4 and rBC >=cost4 and rAB>0: #rBD rBE rAB rBC
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBE
            if 0 < cost3 and rBC >=cost3 and rBE>0: #rBD rBE rBC
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BD', rBD)
                    myinsert(x, 'BE', rBE)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rAB >=cost4 and rBC>0: #rBD rBE rBC rAB
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
    if 0 < cost1 and rBE >=cost1:
        tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD, rBE-cost1, rCD, rCE, rDE, rA, rB, rC, rD, rE)
        for x in tail:
            myadd(x, 'BE', cost1)
            if not(x in ret):
                ret.append(x)
    else:
        cost2=cost1-rBE
        if 0 < cost2 and rAB >=cost2 and rBE>0: #rBE rAB
            tail=testC(ccost, dcost, ecost, rAB-cost2, rAC, rAD, rAE, rBC, rBD,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'AB', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rAB
            if 0 < cost3 and rBC >=cost3 and rAB>0: #rBE rAB rBC
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost3, rBD,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rBD >=cost4 and rBC>0: #rBE rAB rBC rBD
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rAB
            if 0 < cost3 and rBD >=cost3 and rAB>0: #rBE rAB rBD
                tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC, rBD-cost3,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'AB', rAB)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rBC >=cost4 and rBD>0: #rBE rAB rBD rBC
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBE
        if 0 < cost2 and rBC >=cost2 and rBE>0: #rBE rBC
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost2, rBD,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'BC', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBC
            if 0 < cost3 and rAB >=cost3 and rBC>0: #rBE rBC rAB
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE,   0, rBD,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB
                if 0 < cost4 and rBD >=cost4 and rAB>0: #rBE rBC rAB rBD
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0, rBD-cost4,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBC
            if 0 < cost3 and rBD >=cost3 and rBC>0: #rBE rBC rBD
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE,   0, rBD-cost3,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BC', rBC)
                    myadd(x, 'BD', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBD
                if 0 < cost4 and rAB >=cost4 and rBD>0: #rBE rBC rBD rAB
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
        cost2=cost1-rBE
        if 0 < cost2 and rBD >=cost2 and rBE>0: #rBE rBD
            tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC, rBD-cost2,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
            for x in tail:
                myinsert(x, 'BE', rBE)
                myadd(x, 'BD', cost2)
                if not(x in ret):
                    ret.append(x)
        else:
            cost3=cost2-rBD
            if 0 < cost3 and rAB >=cost3 and rBD>0: #rBE rBD rAB
                tail=testC(ccost, dcost, ecost, rAB-cost3, rAC, rAD, rAE, rBC,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'AB', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rAB
                if 0 < cost4 and rBC >=cost4 and rAB>0: #rBE rBD rAB rBC
                    tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE, rBC-cost4,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
            cost3=cost2-rBD
            if 0 < cost3 and rBC >=cost3 and rBD>0: #rBE rBD rBC
                tail=testC(ccost, dcost, ecost, rAB, rAC, rAD, rAE, rBC-cost3,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
                for x in tail:
                    myinsert(x, 'BE', rBE)
                    myinsert(x, 'BD', rBD)
                    myadd(x, 'BC', cost3)
                    if not(x in ret):
                        ret.append(x)
            else:
                cost4=cost3-rBC
                if 0 < cost4 and rAB >=cost4 and rBC>0: #rBE rBD rBC rAB
                    tail=testC(ccost, dcost, ecost, rAB-cost4, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB, rC, rD, rE)
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
                        tail=testC(ccost, dcost, ecost,   0, rAC, rAD, rAE,   0,   0,   0, rCD, rCE, rDE, rA, rB-cost5, rC, rD, rE,)
                        for x in tail:
                            myinsert(x, 'BE', rBE)
                            myinsert(x, 'BD', rBD)
                            myinsert(x, 'BC', rBC)
                            myinsert(x, 'AB', rAB)
                            myinsert(x, 'B', cost5)
                            if not(x in ret):
                                ret.append(x)
    if cost1 == 0:
        ret=testC(ccost, dcost, ecost, rAC, rAB, rAD, rAE, rBC, rCD, rCE,rBD, rBE, rDE, rA, rB, rC, rD, rE)
    print(ret)
    return(ret)
#####################################################################################################################################


#        ret=t bc cc dc ec, rAB, rAC, rAD, rAE, rBC, rBD, rBE,rCD, rCE,  rDE, rA, rB, rC, rD, rE)
x=testB(10, 1, 0, 0,  10,   0,   0,   0,   5,   6,   4,  0, 0, 0 ,0,0,4,0,0)
for y in x:
    print(x.count(y), "=", y)
