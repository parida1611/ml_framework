from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='ml_framework',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt')
)