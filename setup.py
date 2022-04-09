
from setuptools import setup
#This is to include the readme from the github repo
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='Proactive-JSONconfig',
    url='https://github.com/Proactive-Development/JSONconfig/',
    author='Proactive Development',
    packages=['JSONconfig'],
    install_requires=[''],
    version='0.1.1',
    license='NONE',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Easily manage your projects with JSON files',
)