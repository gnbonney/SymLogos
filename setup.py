from setuptools import setup, find_packages

setup(
    name='symlogos',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "sympy>=1.7.1"
    ],
    extras_require={
        "tests": ["pytest"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    author='Greg Bonney',
    author_email='gnbonney@gmail.com',
    description='SymLogos is a Python library that extends the capabilities of SymPy to support higher-order modal logic for formal reasoning and theorem proving.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gnbonney/symlogos',
    license='MIT',
)
