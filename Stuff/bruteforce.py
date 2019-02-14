import hashlib
convertString = "aabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789 0@!"
size =  len(convertString)
palabra = ''
i = 0
maxLen = 6
stringToHack = "26fe616a85cc8c5867ef510145a69a25"
#xew


def md5 (string):
    user = string
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()
    return h2


def bruteForce(n,base, convertString):
   # convertString = "abcdefghijklmnopqrstuvwxyz"
    size =  len(convertString)
  #  print (size)
    if n < base:
       return convertString[n]
    else:
       return bruteForce(n//base,base,convertString) + convertString[n%base]
#print(toStr(100,int(size), convertString))


while len(palabra) <= maxLen:
#for i in range(1,1000000):
    palabra = (bruteForce(i,int(size), convertString))

  #  print(i)

    if stringToHack == str(md5(palabra)):
        print ("En Buenahora la palabra es: ")
        print (i)
        print (palabra)
        break
    else:
        if (i % 1000000==0):
            print (i)
            print(palabra)
    #    print (palabra)
   # break
    i +=1


#print (md5('aa'))
 



 

