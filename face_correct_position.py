import bpy

# Transform data to be applied
location_data = (-0.0019144369289278984, -0.08021366596221924, 1.5782066583633423)
rotation_data = (4.6791534423828125, 0.03137320652604103, 6.20258092880249)
scale_data = (0.1513398289680481, 0.1658138930797577, 0.10031352937221527)

# Function to apply transform data to an object
def apply_transform_data(obj_name, location, rotation, scale):
    obj = bpy.data.objects.get(obj_name)
    if obj is None:
        print(f"Object '{obj_name}' not found.")
        return

    obj.location = location
    obj.rotation_euler = rotation
    obj.scale = scale

    print(f"Transform data applied to '{obj_name}'.")

# Call the function with the object name 'F1' and the transform data
apply_transform_data('F1', location_data, rotation_data, scale_data)