import numpy as np
import os

def resample_face_animation(input_file, output_file, original_fps=25, target_fps=30):
    # Load the face animation data from the .npy file
    face_data = np.load(input_file)

    # Determine the number of frames and the length of the flattened vertex data
    num_frames, data_length = face_data.shape

    # Calculate the new number of frames for the target fps
    new_num_frames = int(num_frames * (target_fps / original_fps))

    # Ensure the data length matches the expected number of vertices * 3 coordinates
    num_vertices = data_length // 3
    if data_length != num_vertices * 3:
        raise ValueError("Data length does not match the expected number of vertices times 3 coordinates")

    # Resample the data using linear interpolation
    resampled_face_data = np.zeros((new_num_frames, data_length), dtype=face_data.dtype)
    for i in range(data_length):
        resampled_face_data[:, i] = np.interp(
            np.linspace(0, num_frames - 1, new_num_frames),
            np.arange(num_frames),
            face_data[:, i]
        )

    # Save the resampled data to a new .npy file
    np.save(output_file, resampled_face_data)
    print(f'Resampled data saved to {output_file}')

# Directory containing the .npy files
input_directory = 'C:/Users/wbblo/Bureaublad/AI_THESIS/result'

# Iterate over all .npy files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.npy'):
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(input_directory, filename.replace('.npy', '_30fps.npy'))
        resample_face_animation(input_file, output_file)
