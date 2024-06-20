import bpy
import numpy as np
import time

# Load the vertex data from the .npy file
data_path = 'path/to/numpy.npy'
vertex_data = np.load(data_path)

# Path to your audio file
# audio_path = 'path/to/audio.wav'

# Get the object
obj = bpy.data.objects['F1']
if obj.type != 'MESH':
    raise ValueError("Selected object is not a mesh")

bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = obj
obj.select_set(True)
bpy.ops.object.mode_set(mode='OBJECT')
mesh = obj.data

if len(mesh.vertices) != len(vertex_data[0]) // 3:
    raise ValueError("The number of vertices in the mesh does not match the data")
    
# Start timing
start_time = time.time()

for frame_number, frame_data in enumerate(vertex_data):
    for i, vertex in enumerate(mesh.vertices):
        vertex.co.x = frame_data[i * 3]
        vertex.co.y = frame_data[i * 3 + 1]
        vertex.co.z = frame_data[i * 3 + 2]

    mesh.update()
    for vertex in mesh.vertices:
        vertex.keyframe_insert(data_path="co", frame=frame_number)

bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = len(vertex_data) - 1

# Add the audio to the scene
scene = bpy.context.scene
if not scene.sequence_editor:
    scene.sequence_editor_create()

# Add audio strip to sequencer
# audio_strip = scene.sequence_editor.sequences.new_sound("AudioStrip", audio_path, channel=1, frame_start=0)

# Adjust the end frame of the scene to match the length of the audio
# audio_length = audio_strip.frame_final_duration
scene.frame_end = scene.frame_end - 1


# End timing
end_time = time.time()
duration = end_time - start_time

print(f"Start time: {start_time}")
print(f"End time: {end_time}")
print(f"Duration: {duration} seconds")
