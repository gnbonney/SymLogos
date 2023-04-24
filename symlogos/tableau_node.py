from __future__ import annotations
from typing import Optional, List
from symlogos.signed_formula import SignedFormula

class TableauNode:
    def __init__(self, signed_formula: SignedFormula, parent: Optional[TableauNode]=None) -> None:
        self.signed_formula = signed_formula
        self.parent = parent
        self.children = []

    def add_child(self, signed_formula):
        child_node = TableauNode(signed_formula, parent=self)
        self.children.append(child_node)
        return child_node

    def get_next_fresh_constant_index(self):
        if self.parent:
            return self.parent.get_next_fresh_constant_index() + 1
        else:
            return 0

    def get_next_fresh_variable_index(self) -> int:
        if self.parent:
            return self.parent.get_next_fresh_variable_index() + 1
        else:
            return 0

    def get_ancestors(self) -> List['TableauNode']:
        ancestors = []
        current_node = self.parent

        while current_node is not None:
            ancestors.append(current_node)
            current_node = current_node.parent

        return ancestors