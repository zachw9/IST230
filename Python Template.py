def negation(p: bool) -> bool:
    """
    Returns the logical negation of p (¬p).
    """
    # TODO: Delete 'pass' and implement negation
    print(negation(True)) #False
    print(negation(False)) #True

def conjunction(p: bool, q: bool) -> bool:
    """
    Returns the logical conjunction of p and q (p ∧ q).
    """
    # TODO: Delete 'pass' and implement conjunction
    print(conjunction(True, True)) #True
    print(conjunction(True, False)) #False
    print(conjunction(False, True)) #False
    print(conjunction(False, False)) #False

def disjunction(p: bool, q: bool) -> bool:
    """
    Returns the logical disjunction of p and q (p ∨ q).
    """
    # TODO: Delete 'pass' and implement disjunction
    print(disjunction(True, True)) #True
    print(disjunction(True, False)) #True
    print(disjunction(False, True)) #True
    print(disjunction(False, False)) #False

def exclusive_or(p: bool, q: bool) -> bool:
    """
    Returns the exclusive OR of p and q (p ⊕ q).
    Evaluates to True if exactly one of the inputs is True.
    """
    # TODO: Delete 'pass' and implement exclusive OR
    print(exclusive_or(True, True)) #False
    print(exclusive_or(True, False)) #True
    print(exclusive_or(False, True)) #True
    print(exclusive_or(False, False)) #False

def conditional(p: bool, q: bool) -> bool:
    """
    Returns the implication p → q.
    Remember the rule from Section 1.3: This is False ONLY when 
    the hypothesis (p) is True and the conclusion (q) is False.
    """
    # TODO: Delete 'pass' and implement conditional logic
    print(conditional(True, True)) #True
    print(conditional(True, False)) #False
    print(conditional(False, True)) #True
    print(conditional(False, False)) #True

def biconditional(p: bool, q: bool) -> bool:
    """
    Returns the biconditional evaluation of p and q (p ↔ q).
    """
    # TODO: Delete 'pass' and implement biconditional logic
    print(biconditional(True, True)) #True
    print(biconditional(True, False)) #False
    print(biconditional(False, True)) #False
    print(biconditional(False, False)) #True

    # ==========================================
# SAMPLE INPUT EXECUTION ENGINE
# ==========================================

def execute_with_sample_inputs():
    """Runs explicit test cases with custom parameters."""
    print("\n========================================================")
    print("       RUNNING INDIVIDUAL SAMPLE INPUT TESTS")
    print("========================================================")
   
    # Test Case 1: Evaluating standard values
    p1, q1 = True, False
    print(f"Sample Input Set 1: p = {p1}, q = {q1}")
    print(f" -> Negation(p):         {negation(p1)}")

    print("-" * 50)



if __name__ == "__main__":
    print("IST 230 Lab - Chapter 1 Master Script Execution")
    execute_with_sample_inputs()