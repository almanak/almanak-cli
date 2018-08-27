from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='almanak-cli',
    version='0.1.2',
    author='Claus Juhl Knudsen',
    author_email='clausjuhl@yahoo.com',
    packages=find_packages(),
    description='Command line interface to almanak.',
    long_description=long_description,
    url='https://github.com/clausjuhl/almanak-cli',
    include_package_data=True,
    license='MIT',
    python_requires='>=3.6.2',
    install_requires=[
        'click==6.7'
    ],
    entry_points="""
        [console_scripts]
        almanak=almanak-cli.app:cli
    """,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.6.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)