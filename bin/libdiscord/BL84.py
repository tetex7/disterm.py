from typing import Final
from ctypes import c_uint16
import datetime
from ctypes import c_byte
from ctypes import c_char
from typing import ByteString
import random

class enc_keys:
    SK1:Final[c_uint16]
    SK2:Final[c_uint16]
    SK3:Final[c_uint16]
    TY:Final[c_byte]
    def __init__(self, k1:c_uint16, k2:c_uint16, k3:c_uint16, k:c_byte) -> None:
        self.SK1 = k1
        self.SK2 = k2
        self.SK3 = k3
        self.TY = k
           
    def gen():
        SK1 = random.randint(41, 999) + datetime.datetime.now().day
        SK2 = random.randint(41, 999) +  (datetime.datetime.now().day + datetime.datetime.now().hour)
        SK3 = random.randint(41, 999)
        TY = random.randint(1, 0xFF)
        return enc_keys(SK1,SK2,SK3,TY)




class enc_str:
    dat:list[c_uint16]
    KEY:Final[enc_keys]
    def __init__(self, st:ByteString, key: enc_keys | None = None) -> None:
        dat = list()
        if (key is None):
            self.KEY = enc_keys.gen()
        self.KEY = key
        temp:list[c_char] = list()
        for v in st:
            temp.append(v)
        self.encode(temp)

    def encode(self, CH:list[c_byte]):
        for i in range(0, len(CH)):
            comp = (CH[i] + ((self.KEY.SK1 + self.KEY.SK2) - self.KEY.SK3) / self.KEY.TY)
            self.dat.append(comp)

    def decode(CH:list[c_byte], KEY:enc_keys):
        tem:list[c_byte] = list()
        o:ByteString = ByteString()
        for i in range(0, len(CH)):
            comp:c_char = (CH[i] - ((KEY.SK1 + KEY.SK2) - KEY.SK3) * KEY.TY)
            tem.append(comp)
        for v in tem:
            o = o + v
        return o
    def DIS_MSG(self) -> str:
        out:str = str()
        for v in self.dat:
            out = out + f"`{v}`"
        return out