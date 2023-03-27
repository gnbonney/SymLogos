# SymLogos

SymLogos is a Python library that extends the capabilities of [SymPy](https://www.sympy.org/) to support higher-order modal logic for formal reasoning and theorem proving.

The name "SymLogos" is derived from the combination of "Sym" from SymPy and "Logos," which is Greek for "reason" or "logic."

The goal of this project is to create a powerful and flexible library for working with higher-order modal logic expressions, allowing users to define axioms, prove theorems, and check consistency and validity within the context of a specified logical framework.

## Scope of SymLogos

SymLogos aims to provide a Python library for working with higher-order modal logic, specifically focused on implementing the logical framework necessary for encoding Gödel's ontological argument. The primary goal of this project is to provide a simple and easy-to-use interface for creating and manipulating propositions and modal operators, as well as verifying the consistency and validity of logical expressions within the context of Gödel's argument.

While there are many advanced logical systems and propositions that could be considered for implementation, such as temporal logic, first-order logic, epistemic logic, and deontic logic, these are considered to be beyond the scope of this project. This decision has been made to maintain simplicity and focus on the core objective of providing a library tailored for Gödel's ontological argument.

In the future, SymLogos could be extended or adapted to support additional logical systems, but these extensions would require a deeper understanding of their semantics and interaction with the existing modal logic system, as well as adjustments to the underlying logical system and the implementation of additional data structures and algorithms. We encourage interested contributors to explore these possibilities in separate projects or forks of SymLogos if they wish to expand the functionality beyond higher-order modal logic.

## Help Wanted

We are actively seeking contributors to help us finish the development of SymLogos. If you are interested in participating, please check out the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to the project.

To get an idea of the tasks and features that need to be implemented, please refer to the [TODO.md](TODO.md) file.

## Project Status

The current version of SymLogos provides basic support for propositional variables and modal operators (necessity and possibility). The project is still under active development, and we plan to add higher-order quantification, axioms, theorems, consistency, and validity checking, as well as seamless integration with SymPy's existing functionality.

## Installing Dependencies

To install the dependencies for SymLogos, you can use `pip`. First, navigate to the root directory of the project, and then run:

```bash
pip install -r requirements.txt

## Running Tests

To run the tests, you need to have Python and `pytest` installed on your system. First, install the testing dependencies by navigating to the `tests` directory and running:

```bash
pip install -r tests/requirements.txt
```

Then you can run pytest
```bash
pytest tests
```

## Getting Started

To start using SymLogos, simply import the library and create a propositional variable:

```python
from symlogos import Proposition

p = Proposition("p")
