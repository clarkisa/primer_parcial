from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_exam_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='clarisa',
    maintainer_email='clarisa.vasquez@ucb.edu.bo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sensor1_pub = my_exam_package.sensor1_pub:main',
            'sensor2_pub = my_exam_package.sensor2_pub:main',
            'sensor3_pub = my_exam_package.sensor3_pub:main',
            'promedio = my_exam_package.promedio:main',
            'display = my_exam_package.display:main',
        ],
    },
)
