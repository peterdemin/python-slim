from setuptools import setup, find_packages


setup(
    name='waferslim',
    version='1.0',
    packages=find_packages(exclude=["*tests*"]),
    description=open('waferslim/README.md', 'rt').read(),
    author='Peter Demin',
    author_email='poslano@gmail.com',
    install_requires=(
         'setuptools>=0.6b1',
         'six',
    ),
)
