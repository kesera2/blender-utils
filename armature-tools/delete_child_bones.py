bl_info = {
    "name": "Delete Child Bones",
    "author": "kesera2",
    "version": (1, 2),
    "blender": (3, 0, 0),
    "location": "View3D Sidebar > Armature Tools",
    "description": "選択したボーンとその子ボーンを再帰的に削除するアドオン",
    "warning": "",
    "doc_url": "https://github.com/kesera2/blender-utils",
    "category": "Armature",
}

import bpy # type: ignore

# 子ボーンを再帰的に削除する関数
def delete_child_bones(bone, armature):
    children = bone.children[:]
    for child in children:
        delete_child_bones(child, armature)
        armature.data.edit_bones.remove(child)

class DeleteChildAndSelfBonesOperator(bpy.types.Operator):
    bl_idname = "armature.delete_child_and_self_bones"
    bl_label = "Delete Selected Bones and Their Children"
    bl_description = "Delete the selected bones and all their child bones"

    def execute(self, context):
        armature = context.active_object

        if not armature or armature.type != 'ARMATURE':
            self.report({'WARNING'}, "Active object is not an armature.")
            return {'CANCELLED'}

        if bpy.context.mode != 'EDIT_ARMATURE':
            self.report({'WARNING'}, "Switch to Edit Mode to delete bones.")
            return {'CANCELLED'}

        selected_bones = [b for b in armature.data.edit_bones if b.select]
        if not selected_bones:
            self.report({'INFO'}, "No bones selected.")
            return {'CANCELLED'}

        deleted_count = 0

        def delete_child_bones_count(bone):
            nonlocal deleted_count
            children = bone.children[:]
            for child in children:
                delete_child_bones_count(child)
                armature.data.edit_bones.remove(child)
                deleted_count += 1

        for bone in selected_bones:
            delete_child_bones_count(bone)
            armature.data.edit_bones.remove(bone)
            deleted_count += 1

        bpy.context.view_layer.update()
        self.report({'INFO'}, f"Deleted {deleted_count} bone(s).")
        return {'FINISHED'}

class ArmatureToolsPanel(bpy.types.Panel):
    bl_label = "Delete Child Bones"
    bl_idname = "ARMATURE_PT_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'kesera2'

    def draw(self, context):
        layout = self.layout
        layout.operator(DeleteChildAndSelfBonesOperator.bl_idname)

def register():
    bpy.utils.register_class(DeleteChildAndSelfBonesOperator)
    bpy.utils.register_class(ArmatureToolsPanel)

def unregister():
    bpy.utils.unregister_class(DeleteChildAndSelfBonesOperator)
    bpy.utils.unregister_class(ArmatureToolsPanel)

if __name__ == "__main__":
    register()