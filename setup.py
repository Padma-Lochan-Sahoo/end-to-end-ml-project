
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name='END-TO-END-ML-PROJECT',
    version='1.0',
    author='Padma',
    author_email='padmalochansahoo8503@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='This is a machine learning project',
    
)