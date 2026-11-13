import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'visualization_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #Include all launch files 
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', ('*launch.[pxy][yma]*')) ))
    ],
    package_data={'': ['py.typed']},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Dinesh Kumar',
    maintainer_email='dineshdhieraj02@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publish_point = visualization_pkg.publish_point:main',
            'publish_pose = visualization_pkg.publish_pose:main',
            'marker = visualization_pkg.marker:main'
        ],
    },
)