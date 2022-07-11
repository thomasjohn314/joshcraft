from numpy import zeros, prod, array

def index_chunk_data(data: array, x: int, y: int, z: int):
    a = data.size / 16 # x
    b = a / 256 # y
    c = b / 16 # z
    return int((a * x) + (b * y) + (c * z))

def generate_test_chunk_data():
    return zeros(prod((16, 256, 16)), dtype=int)