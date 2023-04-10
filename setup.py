from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requ = []
    with open(file_path, 'r') as file_obj:
         requ = file_obj.readlines()
         requ = [req.replace("\n","")for req in requ]##replace the '\n' by blank

         if HYPHEN_E_DOT in requ:
              requ.remove(HYPHEN_E_DOT)
setup(
    name='mlproject',
    version="'0.0.1",
    author='Rohit',
    author_email='parikshit_rohit@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)