from chunk import index_chunk_data, generate_test_chunk_data
from numpy import zeros, prod, array

data = generate_test_chunk_data()

data[index_chunk_data(data, 1, 1, 1)] = 2
data[index_chunk_data(data, 1, 1, 1)]
