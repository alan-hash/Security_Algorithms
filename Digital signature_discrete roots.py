from Crypto.Util.number import getPrime
from random import randint
import random

# 1024
bits = 1024
bits2 =12

def getNumCondition(n):
    rand = random.getrandbits(bits)
    if (rand <= 0 | rand > n):
        return getNumCondition(n)
    return rand

def getNumConditionForP(n):
    return random.getrandbits(bits2)


q = getPrime(bits)
y = getNumCondition(q)
delta=getNumCondition(q)
p = getNumConditionForP(q)


data={}

# Llave publica
U = power_mod(y, p, q)
print()
print("U: " + str(U))

#El mensaje m considerando que 0 < m < q
m = getNumCondition(q)


#El número para enviar por el canal c de acuerdo con la tabla anterior.

data['Channel'] = power_mod((delta)* m + (y), 1, q)
print("Channel: " + str(data['Channel']))
