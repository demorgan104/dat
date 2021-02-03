from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dat",
    version="0.0.1",
    author="demorgan104",
    author_email="timotei@tutanota.de",
    description="The best friend of C/C++ developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/demorgan104/dat",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'dat=dat.scripts.cli:cli'
        ],
    },
    python_requires='>=3.6',
)