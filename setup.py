import re
from setuptools import setup, find_packages


def readme():
    """Return the contents of the project README file."""
    with open('README.md') as f:
        return f.read()


version = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", open('motus/__init__.py').read(), re.M).group(1)

setup(
    name='motus',
    version=version,
    packages=find_packages(),
    url='https://github.com/crvernon/motus',
    license='MIT',
    author='Chris R. Vernon',
    author_email='chrisrvernon@gmail.com',
    description='Aut Visum Aut Non',
    long_description=readme(),
    long_description_content_type="text/markdown",
    python_requires='>=3.8.5',
    include_package_data=True,
    install_requires=[
        'numpy>=1.22.4',
        'pandas>=1.4.2',
        'sf-hamilton[visualization]>=1.10'
    ]
)
