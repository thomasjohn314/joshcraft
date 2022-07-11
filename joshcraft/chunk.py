from numpy import zeros, prod

from block import Block

class Chunk:
    def __init__(self, dimensions=(2, 2, 2)) -> None:
        self.dim_x, self.dim_y, self.dim_z = dimensions
        self.data = zeros(prod(dimensions), dtype=int)
    
    def __getitem__(self, key):
        if len(key) == 1:
            return self.data[key]
        
        x, y, z = key
        a = self.data.size / self.dim_x
        b = a / self.dim_y
        c = b / self.dim_z
        return self.data[int((a * x) + (b * y) + (c * z))]

    def __setitem__(self, key, block: Block):
        if len(key) == 1:
            self.data[key] = block.id
            return

        x, y, z = key
        a = self.data.size / self.dim_x
        b = a / self.dim_y
        c = b / self.dim_z
        self.data[int((a * x) + (b * y) + (c * z))] = block.id