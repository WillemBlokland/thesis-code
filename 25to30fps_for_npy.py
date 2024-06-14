import numpy as np
import os

def resample_face_animation(input_file, output_file, original_fps=25, target_fps=30):
    # Load the face animation data from the .npy file
    face_data = np.load(input_file)

    # Determine the number of frames and vertices
    num_frames = face_data.shape[0]
    num_vertices = face_data.shape[1]

    # Calculate the new number of frames for the target fps
    new_num_frames = int(num_frames * (target_fps / original_fps))

    # Create a new array to hold the resampled data
    resampled_face_data = np.zeros((new_num_frames, num_vertices, 3))

    # Resample the data using linear interpolation
    for i in range(num_vertices):
        for j in range(3):
            resampled_face_data[:, i, j] = np.interp(
                np.linspace(0, num_frames - 1, new_num_frames),
                np.arange(num_frames),
                face_data[:, i, j]
            )

    # Save the resampled data to a new .npy file
    np.save(output_file, resampled_face_data)
    print(f'Resampled data saved to {output_file}')

# Example usage
input_file = 'C:/Users/wbblo/Bureaublad/AI_THESIS/ground_truth/ground_truth/npy/trn_2022_v1_208_10sec_emotional_F1_Condition_F1.npy'
output_file = 'C:/Users/wbblo/Bureaublad/AI_THESIS/trn_2022_v1_208_10sec_emotional_F1_Condition_F1_25_to_30fps.npy'
resample_face_animation(input_file, output_file)
