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
print()
print("m: " + str(m))

#El número para enviar por el canal c de acuerdo con la tabla anterior.

data['Channel'] = power_mod((delta)* m + (y), 1, q)
print()
print("Channel: " + str(data['Channel']))


#Realizar el cómputo del autenticador t definido a continuación:
result = 0

def getFac(p, i):
     return factorial(p) / (factorial(p - i) * factorial(i))


for contador in range(0, p-1):
    result = result + power_mod(getFac(p, contador) * power_mod(m, (p-contador)-1, p) * power_mod(delta, (p-contador), p)* power_mod(y,contador,p),1, q)

print()
print("Result: " + str(result))
print()

#Verificar la firma del mensaje por medio de la siguiente relación:
data['Cp'] = power_mod(data['Channel'], p, q)
print("Es igual? | " + str((data['Cp'] == ((m*result)+U)   ) ) )


