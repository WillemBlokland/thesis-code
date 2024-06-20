import wave

# Function to trim the audio
def trim_wav(input_file, output_file, start_time, duration):
    with wave.open(input_file, 'rb') as wav_file:
        # Get the frame rate and number of frames
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Calculate start and end frame indices
        start_frame = int(start_time * frame_rate)
        end_frame = start_frame + int(duration * frame_rate)

        # Ensure the end frame doesn't exceed the total number of frames
        end_frame = min(end_frame, num_frames)

        # Set the file parameters for the output file
        with wave.open(output_file, 'wb') as output_wav:
            output_wav.setparams(wav_file.getparams())

            # Move to the start frame
            wav_file.setpos(start_frame)

            # Read and write audio frames until reaching the end frame
            while wav_file.tell() < end_frame:
                frames_to_read = min(1024, end_frame - wav_file.tell())
                frames = wav_file.readframes(frames_to_read)
                output_wav.writeframes(frames)

# Define input
input_file = r'path/to/input/audio.wav'
output_file = r'path/to/output/audio.wav'
start_time = 43  # Start time in seconds
duration = 7  # Duration to extract in seconds

trim_wav(input_file, output_file, start_time, duration)
