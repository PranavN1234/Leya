from setuptools import setup, find_packages

setup(
    name='vela',
    version='0.1.0',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': [
            'vela=vela.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A coding assistant to help with repository management and code queries.',
)