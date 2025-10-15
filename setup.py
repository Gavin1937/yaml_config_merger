from setuptools import setup


# get descriptions
description = 'A simple python3 library to merge yaml configs.'
long_description = ''
with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

# load __version__.py
version = {}
with open('./yaml_config_merger/__version__.py', 'r', encoding='utf-8') as file:
    exec(file.read(), version)

# load requirements.txt
requirements = []
with open('requirements.txt', 'r', encoding='utf-8') as file:
    requirements = [line.strip() for line in file.readlines() if len(line.strip()) > 0]


# package settings
setup(
    name='yaml_config_merger',
    author='Gavin1937',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Gavin1937/yaml_config_merger',
    version=version['__version__'],
    license='MIT',
    license_files=['LICENSE'],
    packages=[
        'yaml_config_merger',
    ],
    python_requires='>=3.8.0',
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
