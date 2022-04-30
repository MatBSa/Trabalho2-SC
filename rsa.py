import random, sys, os
from primes import generateLargePrime

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def generateRSAKey(keySize):
    print('Gerando p primo...')
    p = generateLargePrime(keySize)
    print('Gerando q primo...')
    q = generateLargePrime(keySize)
    n = p * q
	
    print('Gerando "e" que é relativamente primo de (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
   
    # Step 3: Calculate d, the mod inverse of e.
    print('Calculando "d" que é mod inverso de e...')
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('\n----------Chave pública----------\n', publicKey)
    print('\n----------Chave privada----------\n', privateKey)
    return (publicKey, privateKey)
    

def makeKeyFiles(name, keySize):
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('AVISO: O arquivo %s_pubkey.txt ou %s_privkey.txt já existe! Use um nome diferente ou exclua esses arquivos e execute novamente este programa.' % (name, name))
        
    publicKey, privateKey = generateRSAKey(keySize)
    # print()
    # print('Escrevendo chave pública para arquivo %s_pubkey.txt...' % (name))
    
    
    # fo = open('%s_pubkey.txt' % (name), 'w')
    # fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    # fo.close()
    # print()
    # print('Escrevendo chave privada para arquivo %s_privkey.txt...' % (name))
    
    # fo = open('%s_privkey.txt' % (name), 'w')
    # fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
    # fo.close()

# def main():
#    makeKeyFiles('RSA_demo', 1024)


# if __name__ == '__main__':
#    main()

