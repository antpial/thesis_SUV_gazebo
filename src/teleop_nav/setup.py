from setuptools import find_packages, setup

package_name = 'teleop_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/teleop_nav']),
        ('share/teleop_nav', ['package.xml']),
        ('share/teleop_nav/launch', [
    		'launch/teleop_wamv.launch.py',
    		# dodaj inne launch file jeśli będą
	]),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='antoni',
    maintainer_email='antoni.pialucha@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_nav = teleop_nav.teleop_nav:main',
        ],
    },
)
