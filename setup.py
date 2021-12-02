from os import environ

from setuptools import find_packages, setup

setup(
    name="samplepackage",
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description="Sample package to expiremt with GitHub actions",
    long_description=open("README.md", "r").read(),
    maintainer="",
    maintainer_email="",
    python_requires=">=3.7,<3.10",
    install_requires=open("requirements.txt", "r").read().split("\n")
)
