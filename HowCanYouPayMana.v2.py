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
def getcombs(manaTypes, nManas):
    combs = [] 
    manaComb=[]
    #calculate the combinationg of manatypes
    for i in list(itertools.combinations(manaTypes, nManas)): 
        mytemp=""
        for x in i:
            mytemp=mytemp+x
        combs.append(mytemp)
    for x in combs:
        if xMana in x:
            manaComb.append(x)
    return(manaComb)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#price={"A":2,'B':0,'C':0,"D":0,"E":0}
avalMana={"AB":2,"AC":2,"A":1}
xMana='A'
#comb=["AB","AC", "AD"]
#ret=[]
loopover=[]
def loopfunc(comb,cost, mytail,ret,xMana,manaTypes,nManas,prices,avalMana):
    cnt=0

    for x in comb:
        buildup=copy.deepcopy(mytail)
        loopover.append(x)

        comb2=copy.deepcopy(comb)
        comb2.remove(x)
        #myinsert(buildup, x,0)
        if x in avalMana:
            if cost>0:
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
manaTypes2=["A","B","C","D"]
nManas2=2
prices={"A":3}
#print(loopfunc(getcombs(manaTypes2,nManas2),4,dict(),[],xMana,manaTypes2,nManas2,prices,avalMana))
#print(loopfunc(getcombs(manaTypes2,nManas2),3,dict(),[],xMana,manaTypes2,nManas2,prices,avalMana))
def myfunc(cost,xMana,manaTypes,nManas,prices,avalMana):
    ret=[]
    ret=[]
    comb=getcombs(["A","B","C","D"], nManas)
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
def testfunc(xMana,manaTypes,nManas,prices,avalMana):
    if xMana in prices and prices[xMana]>0:
        #print("prices=",prices[xMana],", Xmana=",xMana,", manaTypes=",manaTypes,", nManas=",nManas,", prices=",prices,", avalMana=",avalMana)
        ret=myfunc(prices[xMana],xMana,manaTypes,nManas,prices,avalMana)
        if ret:
            #print("continueing to next manatype with:",ret)
            if manaTypes.index(xMana)<len(manaTypes)-1:
                nextMana=manaTypes[manaTypes.index(xMana)+1]
                #print("doing",nextMana)
                ret2=[]
                for x10 in ret:
                    #print("trying on",x10)
                    navalMana=copy.deepcopy(avalMana)
                    for cmod in x10:
                        myadd(navalMana,cmod,-x10[cmod])
                    #print("prices=",prices[xMana],", Xmana=",xMana,", manaTypes=",manaTypes,", nManas=",nManas,", prices=",prices,", avalMana=",navalMana)
                    tail=testfunc(nextMana,manaTypes,nManas,prices,navalMana)
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
        if manaTypes.index(xMana)<len(manaTypes)-1:
            nextMana=manaTypes[manaTypes.index(xMana)+1]
            #print("doing",nextMana)
            return(testfunc(nextMana,manaTypes,nManas,prices,avalMana))
        #else:
        #    print("nomore Manas!")
        return([dict()])
        
print(testfunc(xMana,manaTypes2,nManas2,prices,avalMana))
