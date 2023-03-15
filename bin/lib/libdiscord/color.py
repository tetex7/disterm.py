class hex_color:
    R:int
    G:int
    B:int
    FULL:int
    def __init__(self, R:int, G:int, B:int):
        if ((R + G + B) > 0xFFFFFF):
            self.R = 0xFF
            self.G = 0xFF
            self.B = 0xFF
            self.FULL = 0xFFFFFF
        else:
            self.FULL = R + G + B
            self.R = R
            self.G = G
            self.B = B

    def __str__(self) -> str:
        return str(self.FULL)

    def __int__(self) -> int:
        return self.FULL



