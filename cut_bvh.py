def cut_bvh(input_file, output_file, start_time, end_time):
    # Read the BVH file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Find the frame time
    frame_time_index = None
    for i, line in enumerate(lines):
        if 'Frame Time' in line:
            frame_time_index = i
            break

    if frame_time_index is None:
        raise ValueError("Frame time not found in BVH file")

    frame_time = float(lines[frame_time_index].split()[-1])

    # Calculate frame indices for start and end times
    start_frame = int(start_time / frame_time)
    end_frame = int(end_time / frame_time)
    print(start_frame)
    print(end_frame)

    # Find the end of the header (ROOT, JOINTS, etc.)
    end_header_index = frame_time_index

    if end_header_index is None:
        raise ValueError("End of header not found in BVH file")

    # Write to the output file, skipping frames outside the specified range
    with open(output_file, 'w') as f:
        f.writelines(lines[:end_header_index+1])  # Write header
        f.writelines(lines[end_header_index+1+start_frame:end_header_index+1+end_frame])  # Write frames within the range


# Define input
input_file =  r"path/to/input/motion/data.bvh"
output_file = r"path/to/output/motion/data.bvh"
start_time_to_cut = 43  # seconds
end_time_to_cut =  50  # seconds

cut_bvh(input_file, output_file, start_time_to_cut, end_time_to_cut)

