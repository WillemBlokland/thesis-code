import numpy as np

def inspect_npy_file(file_path):
    # Load the .npy file
    data = np.load(file_path)
    
    # Print the shape and type of the data
    print(f"Shape of the data: {data.shape}")
    print(f"Data type: {data.dtype}")
    
    # Print a brief overview of the data
    print("Data sample (first 5 entries):")
    print(data[:5])

#Define input
file_path = 'path/to/numpy.npy'
inspect_npy_file(file_path)
