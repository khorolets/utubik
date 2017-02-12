from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='utubik',
    version='0.1.0',
    description='Simple YouTube reading helper',
    long_description=readme,
    author='Bohdan Khorolets',
    author_email='b@khorolets.com',
    url='https://github.com/khorolets/utubik',
    packages=find_packages(exclude=('tests', 'docs'))
)
