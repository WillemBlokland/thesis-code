import os
import wave
import contextlib

# Function to get the duration of a wav file
def get_wav_duration(file_path):
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

# Function to iterate over directories and print the duration of wav files
def print_wav_durations(main_folder):
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                duration = get_wav_duration(file_path)
                print(f"File: {file_path} - Duration: {duration:.2f} seconds")

# Main folder containing the subfolders with wav files
main_folder = r'C:\Users\wbblo\Bureaublad\AI_THESIS\sound_thesis_0-19'

# Print durations of all wav files in the directory
print_wav_durations(main_folder)
