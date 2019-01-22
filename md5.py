from hashlib  import md5,sha1,sha256,sha512

def hash(name):
    result=md5(name.encode())
    return result.hexdigest()

def hashsha(name):
    return sha1(name.encode()).hexdigest()



li={}
lm={}
got=0
def md(name):
    if li:
        return(comp(name))
    else:
        makelist()
        return(comp(name))

def makelist():
    f=open("rockyou.txt",encoding="latin-1")
    for i in f:

        li[hash(i.replace('\n',''))]=i.replace('\n','')
        #jack=name.replace('\n','')

def comp(name):
    jack=name.replace('\n','')
    if jack in li:
        return(li[name])
    else:
        return("Not Found")

def sha(name):
    if li:
        return(comp2(name))
    else:
        makelist2()
        return(comp2(name))

def makelist2():
    f=open("rockyou.txt",encoding="latin-1")
    for i in f:

        lm[hashsha(i.replace('\n',''))]=i.replace('\n','')

def comp2(name):
    jack=name.replace('\n','')
    if jack in lm:
        return(lm[name])
    else:
        return("Not Found")
