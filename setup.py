from setuptools import find_packages, setup
from typing import List
import os

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    # Check if the file exists before reading
    if os.path.exists(file_path):
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='ML PROJECT',
    version='0.0.1',
    author='L AJAY',
    author_email='lingalaajay904@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Ensure the file path is correct
)
