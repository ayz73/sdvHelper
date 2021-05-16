from setuptools import setup

requirements = [
    # TODO: put package requirements here
]

setup(
    name='sdvHelper',
    version='0.0.1',
    description="A PyQt5 application to help with Stardew Valley",
    author="ayz",
    author_email='aliensrocksladder@gmail.com',
    url='https://github.com/ayz73/sdvHelper',
    packages=['sdvhelper', 'sdvhelper.images',
              'sdvhelper.tests'],
    package_data={'sdvhelper.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'sdvHelper=sdvhelper.sdvHelper:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='sdvHelper',
    classifiers=[
        'Programming Language :: Python :: 3.9.0',
    ],
)
