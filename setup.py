from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="dumbgrep-cli",
    description="The best grep I ever did see.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="1.0.0",
    url="https://github.com/Kevinpgalligan/dumbgrep",
    author="Kevin Galligan",
    author_email="galligankevinp@gmail.com",
    scripts=["scripts/dumbgrep"],
    packages=find_packages("src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[]
)
