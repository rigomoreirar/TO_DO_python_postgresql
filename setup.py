from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as f:
        requirements = f.read().splitlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    return requirements

setup(
    name='TO_DO_python_postgresql',
    version='0.1',
    description='Simple TO-DO task project, using Python, Docker for PostgreSQL. This will work as a template for Hexagonal Architecture SOLID design.',
    author='Rigoberto Moreira',
    author_email='rigmoreirar@gmail.com',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)