import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="package-api-demorgan104",
    version="0.0.1",
    author="demorgan104",
    author_email="timotei@tutanota.de",
    description="Package API with Conan IO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/demorgan104/package-based-system",
    packages=['package_api'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)