# Belief Revision Engine - Checklist

## Belief base
- [x] Create `BeliefBase` class to store propositional formulas
- [x] Add support for adding and removing formulas
- [x] Add support for formula prioritization (for contraction)


## Formula Parsing
- [x] Define AST node classes (`Var`, `Not`, `And`, `Or`, `Implies`, `Iff`)
- [x] Implement tokenizer for propositional logic formulas
- [x] Implement recursive descent parser
- [x] Add error handling for malformed input
- [x] Write unit tests for parsing

## CNF Conversion
- [x] Implement transformation from arbitrary formula to CNF:
  - [x] Eliminate `→` and `↔`
  - [x] Push negations inward (De Morgan's Laws)
  - [x] Distribute ∨ over ∧
- [x] Test CNF output correctness

## Logical Entailment (Resolution)
- [x] Implement clause-level resolution algorithm
- [x] Implement entailment test: `entails(belief_base, formula)`
- [x] Handle tautologies and contradictions correctly
- [x] Test entailment with known valid/invalid cases

## Belief Contraction
- [x] Implement **partial meet contraction** algorithm
- [x] Implement prioritization heuristic (e.g., recency, strength)
- [x] Ensure output belief base no longer entails ¬φ
- [x] Test contraction on edge cases

## Belief Expansion
- [x] Implement safe addition of formula to belief base
- [x] Check for and resolve inconsistencies
- [x] Optionally reject expansion if it creates contradictions

## Belief Revision
- [x] Implement revision as `Rev(B, φ) = Expand(Contract(B, ¬φ), φ)`
- [x] Combine contraction and expansion correctly
- [x] Test revision across multiple scenarios

## AGM Postulates Validation
- [x] Implement automated tests for AGM postulates:
  - [x] Success: `φ ∈ Rev(B, φ)`
  - [x] Inclusion: `Rev(B, φ) ⊆ B + φ`
  - [x] Vacuity: if `¬φ ∉ Cn(B)`, then `B + φ = Rev(B, φ)`
  - [x] Consistency: if `φ` is consistent, so is `Rev(B, φ)`
  - [x] Extensionality: logically equivalent `φ, ψ ⇒ same revision`

  ## (Optional) Mastermind Integration
- [x] Encode game rules as beliefs
- [x] Revise beliefs based on guess feedback
- [x] Generate next guess from belief base
- [x] Loop until code is found

## Horn Clause Optimization (Optional)
- [ ] Detect whether a clause is a **Horn clause**
- [ ] Identify **definite clauses** (exactly one positive literal)
- [ ] Identify **goal clauses** (no positive literals)
- [ ] Implement **forward chaining** inference for Horn clauses
- [ ] Implement **backward chaining** inference for Horn clauses
- [ ] Use Horn clause detection to optimize resolution/inference
- [ ] Add unit tests with Horn-only belief bases