bl_info = {
    "name": "Recursive Bone Rename",
    "author": "kesera2",
    "version": (1, 2),
    "blender": (3, 0, 0),
    "location": "View3D > Tool Shelf",
    "description": "Rename bones recursively under root bones if name contains target string",
    "category": "Armature",
}

import bpy

class BoneRecursiveRenameProps(bpy.types.PropertyGroup):
    armature: bpy.props.PointerProperty(
        name="Armature",
        type=bpy.types.Object,
        poll=lambda self, obj: obj.type == 'ARMATURE'
    )
    target_string: bpy.props.StringProperty(name="Target String")
    replace_string: bpy.props.StringProperty(name="Replace With", default="")

class OBJECT_OT_recursive_bone_rename(bpy.types.Operator):
    bl_idname = "object.recursive_bone_rename"
    bl_label = "Recursive Bone Rename"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.bone_recursive_rename_props
        arm = props.armature
        if not arm or arm.type != 'ARMATURE':
            self.report({'ERROR'}, "Select a valid armature")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='EDIT')
        edit_bones = arm.data.edit_bones

        def recursive_rename(bone):
            # 名前にターゲット文字列があれば置換
            if props.target_string in bone.name:
                bone.name = bone.name.replace(props.target_string, props.replace_string)
            # 子ボーンも処理
            for child in bone.children:
                recursive_rename(child)

        # 親を持たないボーンが「ルートボーン」
        for bone in [b for b in edit_bones if b.parent is None]:
            recursive_rename(bone)

        bpy.ops.object.mode_set(mode='OBJECT')
        return {'FINISHED'}

class VIEW3D_PT_recursive_bone_rename(bpy.types.Panel):
    bl_label = "Recursive Bone Rename"
    bl_idname = "VIEW3D_PT_recursive_bone_rename"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "kesera2"

    def draw(self, context):
        layout = self.layout
        props = context.scene.bone_recursive_rename_props

        layout.prop(props, "armature")
        layout.prop(props, "target_string")
        layout.prop(props, "replace_string")
        layout.operator("object.recursive_bone_rename")

classes = (
    BoneRecursiveRenameProps,
    OBJECT_OT_recursive_bone_rename,
    VIEW3D_PT_recursive_bone_rename,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.bone_recursive_rename_props = bpy.props.PointerProperty(type=BoneRecursiveRenameProps)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.bone_recursive_rename_props

if __name__ == "__main__":
    register()
