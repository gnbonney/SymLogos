from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="symlogos",
    version="0.1.0",
    author="Greg Bonney",
    author_email="gnbonney@gmail.com",
    description="A higher-order modal logic extension for SymPy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gnbonney/symlogos",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "sympy>=1.9",
    ],
)
