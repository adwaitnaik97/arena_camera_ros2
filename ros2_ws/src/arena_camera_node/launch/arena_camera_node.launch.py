from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='arena_camera_node',
            executable='start',
            name='arena_camera_node',
            output='screen',
            parameters=[{
                'serial': '904240001',
                'topic': '/special_images',
                'width': 100,
                'height': 200,
                'pixelformat': 'rgb8',
                'gain': 10.0,
                'exposure_time': 150.0,
                'trigger_mode': True
            }]
        )
    ])
