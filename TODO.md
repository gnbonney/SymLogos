# TODO

This document lists the additional features and tasks needed to achieve the goals of the SymLogos project. The project aims to extend SymPy's capabilities to support higher-order modal logic and reproduce the work of Christoph Benzmüller and Bruno Woltzenlogel Paleo.

## Goals

1. Implement higher-order quantification for predicates and functions.
2. Introduce modal operators (necessity and possibility) and their semantics.
3. Provide support for defining axioms with modal operators and higher-order quantification.
4. Develop a formal proof system for deriving theorems within the context of higher-order modal logic.
5. Implement consistency and validity checking for logical expressions.
6. Ensure seamless integration with SymPy's existing functionality.

## Tasks

### Higher-order quantification

- [x] Implement a class for higher-order predicates.
- [x] Implement a class for higher-order functions.
- [x] Extend the existing quantifier classes in SymPy to support higher-order predicates and functions.

### Modal operators and semantics

- [x] Improve the existing Necessity and Possibility classes to support more complex formulas and syntax.
- [ ] Implement a class for modal frames to represent possible worlds.
- [ ] Implement a class for modal models to evaluate formulas within the context of modal frames.

### Axioms and proof system

- [x] Develop a mechanism for defining axioms with higher-order quantification and modal operators.
- [ ] Implement a formal proof system (e.g., natural deduction, sequent calculus) for higher-order modal logic.
    - [x] Define basic data structures for expressions, terms, formulas, and rules.
    - [x] Create a class for higher-order modal logic with methods for constructing formulas and rules, and for manipulating expressions.
    - [ ] Implement a tableau method for higher-order modal logic.
    - [ ] Develop a method to verify proofs in your proof system.
    - [ ] Create functions for parsing and formatting expressions and proofs.
    - [ ] Implement a main function for your library that allows users to input expressions and proofs, then verify and display the results.
- [ ] Implement functions for theorem proving and proof verification.

### Consistency and validity checking

- [ ] Implement a function to check the consistency of a set of axioms or logical expressions.
- [ ] Implement a function to check the validity of a given logical expression or argument.

### Integration with SymPy

- [x] Ensure that the new classes and functions integrate smoothly with SymPy's existing functionality.
- [x] Add support for simplification, substitution, and other standard SymPy operations on higher-order modal logic expressions.

### Documentation and examples

- [ ] Write comprehensive documentation for the library, including tutorials and API reference.
- [ ] Provide examples demonstrating the use of the library for various higher-order modal logic tasks, such as encoding Gödel's ontological argument.
