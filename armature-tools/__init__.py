bl_info = {
    "name": "Armature Tools",
    "author": "kesera2",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D Sidebar > Tool Tab",
    "description": "Recursive rename & delete child bones tools",
    "category": "Armature",
}

from . import recursive_bone_renamer
from . import delete_child_bones

def register():
    recursive_bone_renamer.register()
    delete_child_bones.register()

def unregister():
    delete_child_bones.unregister()
    recursive_bone_renamer.unregister()

if __name__ == "__main__":
    register()
