from setuptools import find_packages, setup

setup(
    name="photoblend",
    version="0.0.15",
    url="https://github.com/aausek/PhotoBlend",
    license='',
    install_requires=["PySide2", "Pillow", "numpy"],
    packages=find_packages(),
    python_requires=">=3.7",
)