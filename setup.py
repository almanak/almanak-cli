from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='almanak-cli',
    version='0.2.0',
    author='Claus Juhl Knudsen',
    author_email='clausjuhl@yahoo.com',
    packages=find_packages(),
    description='Command line interface to almanak-stuff.',
    long_description=long_description,
    url='https://github.com/clausjuhl/almanak-cli',
    include_package_data=True,
    license='MIT',
    python_requires='>=3.6.2',
    install_requires=[
        'click',
        # 'almanak',
    ],
    entry_points="""
        [console_scripts]
        almanak=almanakcli.__init__:cli
    """,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)