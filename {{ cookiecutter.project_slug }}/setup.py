from setuptools import find_packages, setup

setup(
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.author_name }}',
)