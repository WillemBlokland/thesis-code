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

# Example usage
file_path = 'C:/Users/wbblo/Bureaublad/AI_THESIS/ground_truth/ground_truth/npy/trn_2022_v1_208_10sec_emotional_F1_Condition_F1.npy'
inspect_npy_file(file_path)
