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

- ✅ Implement a class for higher-order predicates.
- ✅ Implement a class for higher-order functions.
- ✅ Extend the existing quantifier classes in SymPy to support higher-order predicates and functions.

### Modal operators and semantics

- ✅ Improve the existing Necessity and Possibility classes to support more complex formulas and syntax.
- [ ] Implement a class for modal frames to represent possible worlds.
- [ ] Implement a class for modal models to evaluate formulas within the context of modal frames.

### Axioms and proof system

- ✅ Develop a mechanism for defining axioms with higher-order quantification and modal operators.
- [ ] Implement a formal proof system (e.g., natural deduction, sequent calculus) for higher-order modal logic.
    - ✅ Define basic data structures for expressions, terms, formulas, and rules.
    - ✅ Create a class for higher-order modal logic with methods for constructing formulas and rules, and for manipulating expressions.
    - [ ] Implement a tableau method for higher-order modal logic.
        - ✅ **Normalize the input formula:** Convert the input formula into an equivalent formula in negation normal form (NNF) as opposed to clausal normal form (CNF).
        - [ ] **Define tableau rules:** Define the set of tableau expansion rules specific to higher-order modal logic. These rules should cover higher-order quantifiers, modal operators, and other logical connectives. For the immediate project requirements, need to handle signed formulas (we might want to implement unsigned formulas later).
        - [ ] **Implement the tableau construction algorithm:** Implement an algorithm to construct a tableau for the input formula. The algorithm should apply the tableau rules in a systematic and exhaustive manner until no further rule can be applied or the tableau is closed (i.e., contains a contradiction).
        - [ ] **Determine the satisfiability of the formula:** Check whether the constructed tableau is closed or open. If the tableau is closed, the input formula is unsatisfiable. If the tableau is open, the formula is satisfiable.
        - [ ] **(Optional) Extract a model or countermodel:** If the tableau is open and satisfiable, you can extract a model from the open branches of the tableau. The model can be used to provide a countermodel for the negation of the input formula.
    - [ ] Develop a method to verify proofs in your proof system.
    - [ ] Create functions for parsing and formatting expressions and proofs.
    - [ ] Implement a main function for your library that allows users to input expressions and proofs, then verify and display the results.
- [ ] Implement functions for theorem proving and proof verification.

### Consistency and validity checking

- [ ] Implement a function to check the consistency of a set of axioms or logical expressions.
- [ ] Implement a function to check the validity of a given logical expression or argument.

### Integration with SymPy

- ✅ Ensure that the new classes and functions integrate smoothly with SymPy's existing functionality.
- ✅ Add support for simplification, substitution, and other standard SymPy operations on higher-order modal logic expressions.

### Documentation and examples

- [ ] Write comprehensive documentation for the library, including tutorials and API reference.
- [ ] Provide examples demonstrating the use of the library for various higher-order modal logic tasks, such as encoding Gödel's ontological argument.
