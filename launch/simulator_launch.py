
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import TextSubstitution
from launch_ros.actions import SetParameter
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  robot_namespace = LaunchConfiguration('robot_namespace')
  operator_namespace = LaunchConfiguration('operator_namespace')
  background_chart = LaunchConfiguration('background_chart')
  use_sim_time = LaunchConfiguration('use_sim_time')

  robot_namespace_arg = DeclareLaunchArgument(
    "robot_namespace", default_value=TextSubstitution(text="ben")
  )
  operator_namespace_arg = DeclareLaunchArgument(
    "operator_namespace", default_value=TextSubstitution(text="operator")
  )
  background_chart_arg = DeclareLaunchArgument(
    "background_chart", default_value=PathJoinSubstitution(
      [FindPackageShare('camp'), 'workspace', '13283', '13283_2.KAP']
    )
  )
  use_sim_time_arg = DeclareLaunchArgument(
    "use_sim_time", default_value=TextSubstitution(text="false")
  )

  set_use_sim_time = SetParameter(name='use_sim_time', value=use_sim_time)
  # 'use_sim_time' will be set on all nodes following the line above

  launch_sim_robot_include = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      PathJoinSubstitution([
        FindPackageShare('project11_simulation'),
        'launch',
        'sim_robot_launch.py'
      ])
    ),
    launch_arguments={
      'namespace': robot_namespace,
      'enable_bridge': 'false',
      'operator_host': 'localhost',
      'use_sim_time': use_sim_time
    }.items()
  )

  launch_sim_operator_include = IncludeLaunchDescription(
    PythonLaunchDescriptionSource(
      PathJoinSubstitution([
        FindPackageShare('project11_simulation'),
        'launch',
        'sim_operator_launch.py'
      ])
    ),
    launch_arguments={
      'robot_namespace': robot_namespace,
      'operator_namespace': operator_namespace,
      'enable_bridge': 'false',
      'background_chart': background_chart,
      'use_sim_time': use_sim_time,
      'rviz': 'true',
      'rviz_configuration': PathJoinSubstitution([
        FindPackageShare('ben_project11'),
        'config',
        'ben.rviz'
      ])
    }.items()
  )

  return LaunchDescription([
    robot_namespace_arg,
    operator_namespace_arg,
    background_chart_arg,
    use_sim_time_arg,
    set_use_sim_time,
    launch_sim_robot_include,
    launch_sim_operator_include
  ])


