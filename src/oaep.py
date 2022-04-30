import hashlib
from typing import Callable
from math import ceil
import random
import string

def xor(data: bytes, mask: bytes):
    return bytes([_a ^ _b for _a,_b in zip(data, mask)])

def integerToOctate(x: int, xlen: int):
    return x.to_bytes(xlen, byteorder="big")

def sha3_256(m: bytes):
    hasher = hashlib.sha3_256()
    hasher.update(m)
    return hasher.digest()

def mgf1(seed: bytes, mlen: int, f_hash: Callable = sha3_256):
    t = b""
    hlen = len(f_hash(b""))
    for c in range(0, ceil(mlen/ hlen)):
        _c = integerToOctate(c, 4)
        t +=  f_hash(seed + _c)
    return t[:mlen]
    

def oaep_encode(m: string, n: int, k0: int, k1: int, f_hash: Callable = sha3_256, f_mfg1: Callable = mgf1 ):
    #m = m.ljust(n - k0 - k1) # messagem tem que ser de tamanho n -k0 -k1  
    # 1) Adicionar k1 zeros para a mensagem
    for i in range(k1):
        m += str(0)
    # 2) Gera um r aleatório de tamanho k0
    r = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(k0))
    # 3) Usa o oráculo G = mgf1 para expandir r de k0 para n - k0 de tamanho
    rExpanded = mgf1(bytes(r, "UTF-8"), n - k0)
    # 4) Faz o xor para gerar os duas partes dos bytes
    X = xor(bytes(m, "UTF-8"), rExpanded)
    Y = xor(bytes(r, "UTF-8"), sha3_256(X))    
    # 5) Concatena os bytes 
    result = b"".join([X, Y])
    return X, Y, result

def oaep_decode(X: bytes, Y: bytes, n = 1024, k0 = 32):
    r = xor(Y, sha3_256(X))
    m = xor(X, mgf1(r, n - k0))
    m = str(m).replace("0", "")
    return r, m