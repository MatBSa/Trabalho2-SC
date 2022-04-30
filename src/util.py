def mat_mul(a, b):
    result = [[0],[0],[0],[0]]
    for i in range(4):
        for j in range(4):
            result[i][0] ^= mul(a[i][j], b[j][0])

    return result

def mul(a, b):
    res = 0
    for x in range(b.bit_length() + 1):
        if b & (1 << x):
            res ^= a << x

    while res.bit_length() > 8:
        res ^= 0x11b << (res.bit_length() - 9)

    return res

def rcon(n):
    res = 1
    for i in range(n):
        res = (res<<1) ^ (0x11b & -(res>>7))
    
    return res

def processMessage(msg):
    blocks = []
    for i in range(len(msg)):
        if i%16 == 0:
            blocks.append([])
        
        blocks[-1].append(msg[i])
    
    while len(blocks[-1]) != 16:
        blocks[-1].append(ord('{'))

    return blocks

def convert_matrix(block):
    res = [[] for _ in range(4)]
    for i in range(len(res)):
        for j in range(4):
            res[i].append(block[i+(4*j)])

    return res

def convert_list(block):
    res = []
    for i in range(4):
        for j in range(4):
            res.append(block[j][i])

    return res

import argparse

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'sim', 'true', 't', 'y', 's', '1'):
        return True
    elif v.lower() in ('no', 'não', 'nao', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')