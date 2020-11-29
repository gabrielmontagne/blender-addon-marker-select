import bpy

bl_info = {
    'name': 'Marker selection operators',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Bulk manipulate the selection state of timeline markers',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-marker-select/issues',
    'category': 'Render'
}

class MarkerSelectLeft(bpy.types.Operator):
    """Select all markers to the left of the keyframe"""
    bl_idname = "anim.maker_select_left"
    bl_label = "Marker select left"

    def execute(self, context):
        scene = context.scene
        markers = scene.timeline_markers
        frame_current = scene.frame_current

        for m in markers:
            m.select = m.frame < frame_current

        return {'FINISHED'}

class MarkerSelectRight(bpy.types.Operator):
    """Select all markers to the right of the keyframe"""
    bl_idname = "anim.maker_select_right"
    bl_label = "Marker select right"

    def execute(self, context):
        scene = context.scene
        markers = scene.timeline_markers
        frame_current = scene.frame_current

        for m in markers:
            m.select = m.frame >= frame_current

        return {'FINISHED'}

class MarkerSelectNone(bpy.types.Operator):
    """Clear marker selection"""
    bl_idname = "anim.maker_select_none"
    bl_label = "Marker select none"

    def execute(self, context):
        scene = context.scene
        markers = scene.timeline_markers
        frame_current = scene.frame_current

        for m in markers:
            m.select = False

        return {'FINISHED'}

class MarkerSelectAll(bpy.types.Operator):
    """Select all markers"""
    bl_idname = "anim.maker_select_all"
    bl_label = "Marker select all"

    def execute(self, context):
        scene = context.scene
        markers = scene.timeline_markers
        frame_current = scene.frame_current

        for m in markers:
            m.select = True

        return {'FINISHED'}

def register():
    bpy.utils.register_class(MarkerSelectLeft)
    bpy.utils.register_class(MarkerSelectRight)
    bpy.utils.register_class(MarkerSelectAll)
    bpy.utils.register_class(MarkerSelectNone)

def unregister():
    bpy.utils.unregister_class(MarkerSelectLeft)
    bpy.utils.unregister_class(MarkerSelectRight)
    bpy.utils.unregister_class(MarkerSelectAll)
    bpy.utils.unregister_class(MarkerSelectNone)

if __name__ == "__main__":
    register()
