from setuptools import find_packages, setup
from glob import glob
import os
package_name = 'robot_bio'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/robot_bio']),
        ('share/robot_bio', ['package.xml']),

        # launch
        (os.path.join('share', 'robot_bio', 'launch'),
            glob('launch/*.py')),

        (os.path.join('share', 'robot_bio', 'urdf'),
            glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='raul',
    maintainer_email='raul@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'gui_control = robot_bio.gui_control:main',
        ],
    },
)
