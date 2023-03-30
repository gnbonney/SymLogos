# Logical Rules

This document provides an overview of six types of logical rules that can be used in a proof system for higher-order modal logic. These rules are essential for encoding complex arguments, such as Gödel's ontological argument. The last 3 are related to modal logic and are necessary for working with arguments that involve modal operators such as necessity and possibility.

## 1. Modus Ponens

**Rule**: If `A` is true and `A → B` is true, then `B` is true.

**Input terms (premises)**:
- A
- A → B

**Result term (conclusion)**:
- B

## 2. Modus Tollens

**Rule**: If `¬B` is true and `A → B` is true, then `¬A` is true.

**Input terms (premises)**:
- ¬B
- A → B

**Result term (conclusion)**:
- ¬A

## 3. Universal Instantiation

**Rule**: If `∀x P(x)` is true, then `P(a)` is true for any `a`.

**Input term (premise)**:
- ∀x P(x)

**Result term (conclusion)**:
- P(a)

## 4. Existential Instantiation

**Rule**: If `∃x P(x)` is true, then there is some `a` such that `P(a)` is true.

**Input term (premise)**:
- ∃x P(x)

**Result term (conclusion)**:
- P(a) (for some `a`)

## 5. Modal Modus Ponens

**Rule**: If `□(A → B)` is true and `□A` is true, then `□B` is true.

**Input terms (premises)**:
- □(A → B)
- □A

**Result term (conclusion)**:
- □B

## 6. Barcan Formula

**Rule**: If `□∀x P(x)` is true, then `∀x □P(x)` is true.

**Input term (premise)**:
- □∀x P(x)

**Result term (conclusion)**:
- ∀x □P(x)

