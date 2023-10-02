from setuptools import setup, find_packages
from glob import glob
import os

package_name = 'py_echo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(include=['py_echo', 'py_echo.*']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ignazio D\'Amicis',
    maintainer_email='damicisignazio@gmail.com',
    description='Conversion of cpp_echo',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
            'console_scripts': [
                    'client = py_echo.publisher_member_function:main',
                    'server = py_echo.subscriber_member_function:main',
            ],
    },
    
)
