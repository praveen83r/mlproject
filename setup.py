from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        # Read all lines from requirements.txt
        requirements = file_obj.readlines()
        
        # Remove newline characters from each line
        requirements = [req.replace('\n', '') for req in requirements]
        
        # Remove '-e .' if it's in the list
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Praveen',
    author_email='rokkalap049@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
