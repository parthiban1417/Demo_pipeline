from setuptools import setup, find_packages
setup(name='census_income', 
      version='0.0.1',
      author='parthi',
      author_email='parthi@mail',
      packages=find_packages(),
      install_requirements=['pandas','numpy','flask']
      )