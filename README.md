# SymLogos

SymLogos is a Python library that extends the capabilities of [SymPy](https://www.sympy.org/) to support higher-order modal logic for formal reasoning and theorem proving.

The name "SymLogos" is derived from the combination of "Sym" from SymPy and "Logos," which is Greek for "reason" or "logic."

The goal of this project is to create a powerful and flexible library for working with higher-order modal logic expressions, allowing users to define axioms, prove theorems, and check consistency and validity within the context of a specified logical framework.

## Help Wanted

We are actively seeking contributors to help us finish the development of SymLogos. If you are interested in participating, please check out the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

To get an idea of the tasks and features that need to be implemented, please refer to the [TODO.md](TODO.md) file.

## Project Status

The current version of SymLogos provides basic support for propositional variables and modal operators (necessity and possibility). The project is still under active development, and we plan to add higher-order quantification, axioms, theorems, consistency, and validity checking, as well as seamless integration with SymPy's existing functionality.

## Getting Started

To start using SymLogos, simply import the library and create a propositional variable:

```python
from symlogos import Proposition

p = Proposition("p")
