from typing import Union, Final

class hex_color:
    FULL:bytearray
    def __init__(self, R:bytes, G:bytes, B:bytes):
            self.FULL = bytearray([R, G, B])
            
    def __str__(self) -> str:
        return str(self.FULL)

    def __int__(self) -> int:
        return int(self.FULL.hex(), base=16)



