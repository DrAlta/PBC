import itertools
import copy
def myadd(xhash, xkey, x):
 #   print("adding ",xkey, "=",x," to ",xhash)
    if xkey in xhash:
        xhash.update({xkey: xhash[xkey]+x})
    else:
        if x >0:
            xhash.update({xkey: x})
        else:
            xhash.update({xkey: x})

def myinsert(xhash, xkey, x):
    assert not( xkey in xhash), "key %s already exists !" % xkey
    if x >0:
        xhash.update({xkey: x})
    else:
        xhash.update({xkey+'z': x})

#get the nManas long combinations of manaTypes
def getcombs(manaTypes, nManas, xMana):
    combs = [] 
    manaComb=[]
    #calculate the combinationg of manatypes
    for i in list(itertools.combinations(manaTypes, nManas)): 
        mytemp=[]
        for x in i:
            mytemp.append(x)
#        print("adding",x)
        combs.append(mytemp)
    for x in combs:
        if set(xMana).issubset( x):
            manaComb.append(frozenset([*x]))
    return(manaComb)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#price={"A":2,'B':0,'C':0,"D":0,"E":0}
manaTypes2=["A","B","C","D"]
nManas2=2
prices={frozenset("A"):3}
avalMana={frozenset(['A','B']):5,frozenset(['A','C']):2,frozenset('A'):1}
xMana=frozenset('A')
#comb=["AB","AC", "AD"]
#ret=[]
#print(getcombs(manaTypes2,2,('A')))
print("new")
loopover=[]
def loopfunc(comb,cost, mytail,ret,xMana,manaTypes,nManas,prices,avalMana):
    cnt=0

    for x in comb:
        buildup=copy.deepcopy(mytail)
        loopover.append(x)

        comb2=copy.deepcopy(comb)
        comb2.remove(x)
        #myinsert(buildup, x,0)
        #print({x},"avalMana",set(avalMana.keys()))
        if {x}.issubset(set(list(avalMana.keys()))):
            print(x,"is in",set(avalMana.keys()))
            if cost>0:
                print("cost",cost,"from",avalMana[x])
                if cost <= avalMana[x]:
                    myinsert(buildup, x, cost)
                    if buildup and not(buildup in ret):
                        ret.append(buildup)    #else:
                else:
                    myinsert(buildup, x, avalMana[x])
                    tail=loopfunc(comb2,cost-avalMana[x], buildup,ret,xMana,manaTypes,nManas,prices,avalMana)
                        
                    '''for x in tail[0]:
                        myadd(buildup, x,tail[0][x])'''
                         
                
            #myinsert(buildup, x, price[xMana])
        loopover.pop()
        cnt+=1
    return(ret)
print(loopfunc(getcombs(manaTypes2,nManas2,xMana),4,dict(),[],xMana,manaTypes2,nManas2,prices,avalMana))
#print(loopfunc(getcombs(manaTypes2,nManas2),3,dict(),[],xMana,manaTypes2,nManas2,prices,avalMana))
def myfunc(cost,xMana,manaTypes,nManas,prices,avalMana):
    ret=[]
    comb=getcombs(manaTypes, nManas, xMana)
    ret=loopfunc(comb,cost,dict(),[],xMana,manaTypes,nManas,prices,avalMana)
    #print("fisrt pass",ret)
    if ret:
        #print("returning from this pass")
        return(ret)
    else:
        #print("failed this pass")
        if nManas>1:
            #print("continuing")
            ncost=cost
            for x in comb:
                if x in avalMana:
                    ncost-=avalMana[x]
            ret2=myfunc(ncost,xMana,manaTypes,nManas-1,prices,avalMana)
            if ret2:
                ret=[]
                for tail in ret2:
                    for x in comb:
                        if x in avalMana:
                            myadd(tail,x,avalMana[x])
                    ret.append(tail)              
                return(ret)
            else:
                return([])
        else:
            return([])#true
#++++
#print(myfunc(3,xMana,manaTypes2,nManas2,prices,avalMana))
######################
######################
######################
def recurseTest(xMana,manaTypes,nManas,prices,avalMana):
    if xMana in prices and prices[xMana]>0:
        #print("prices=",prices[xMana],", Xmana=",xMana,", manaTypes=",manaTypes,", nManas=",nManas,", prices=",prices,", avalMana=",avalMana)
        ret=myfunc(prices[xMana],xMana,manaTypes,nManas,prices,avalMana)
        if ret:
            #print("continueing to next manatype with:",ret)
            costTypes=list(prices.keys())
            if costTypes.index(xMana)<len(costTypes)-1:
                nextMana=manaTypes[manaTypes.index(xMana)+1]
                #print("doing",nextMana)
                ret2=[]
                for x10 in ret:
                    #print("trying on",x10)
                    navalMana=copy.deepcopy(avalMana)
                    for cmod in x10:
                        myadd(navalMana,cmod,-x10[cmod])
                    #print("prices=",prices[xMana],", Xmana=",xMana,", manaTypes=",manaTypes,", nManas=",nManas,", prices=",prices,", avalMana=",navalMana)
                    tail=recurseTest(nextMana,manaTypes,nManas,prices,navalMana)
                    if tail:
                        
                        #print("tail=",tail)
                        for xtail in tail:
                            #print(xMana,">", xtail)
                            for tmod in x10:
                                myadd(xtail,tmod,x10[tmod])
                        ret2.append(xtail)
                        #print("return point Y",xtail)
                    else:
                        #print("return point X")
                        return([])
                return(ret2)
            else:
                return(ret)
                #print("nomore Manas!")
        else:
            #print("failing on",xMana)
            return([])
    else:
        #print("continueing to next manatype")
        costTypes=list(prices.keys())
        if costTypes.index(xMana)<len(costTypes)-1:
            nextMana=manaTypes[manaTypes.index(xMana)+1]
            #print("doing",nextMana)
            return(recurseTest(nextMana,manaTypes,nManas,prices,avalMana))
        #else:
        #    print("nomore Manas!")
        return([dict()])
def testManaCosts(manaTypes,nManas,prices,avalMana):
    costTypes=list(prices.keys())
    if 0<len(costTypes):
        return(recurseTest(costTypes.pop(0),manaTypes,nManas,prices,avalMana))

#print(testManaCosts(manaTypes2,nManas2,prices,avalMana))
