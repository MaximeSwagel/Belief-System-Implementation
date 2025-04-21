# Belief Revision Engine - Checklist

## Belief base
- [ ] Create `BeliefBase` class to store propositional formulas
- [ ] Add support for adding and removing formulas
- [ ] Add support for formula prioritization (for contraction)


## Formula Parsing
- [x] Define AST node classes (`Var`, `Not`, `And`, `Or`, `Implies`, `Iff`)
- [x] Implement tokenizer for propositional logic formulas
- [x] Implement recursive descent parser
- [ ] Add error handling for malformed input
- [x] Write unit tests for parsing

## CNF Conversion
- [x] Implement transformation from arbitrary formula to CNF:
  - [x] Eliminate `→` and `↔`
  - [x] Push negations inward (De Morgan's Laws)
  - [x] Distribute ∨ over ∧
- [x] Test CNF output correctness

## Logical Entailment (Resolution)
- [ ] Implement clause-level resolution algorithm
- [ ] Implement entailment test: `entails(belief_base, formula)`
- [ ] Handle tautologies and contradictions correctly
- [ ] Test entailment with known valid/invalid cases

## Belief Contraction
- [ ] Implement **partial meet contraction** algorithm
- [ ] Implement prioritization heuristic (e.g., recency, strength)
- [ ] Ensure output belief base no longer entails ¬φ
- [ ] Test contraction on edge cases

## Belief Expansion
- [ ] Implement safe addition of formula to belief base
- [ ] Check for and resolve inconsistencies
- [ ] Optionally reject expansion if it creates contradictions

## Belief Revision
- [ ] Implement revision as `Rev(B, φ) = Expand(Contract(B, ¬φ), φ)`
- [ ] Combine contraction and expansion correctly
- [ ] Test revision across multiple scenarios

## AGM Postulates Validation
- [ ] Implement automated tests for AGM postulates:
  - [ ] Success: `φ ∈ Rev(B, φ)`
  - [ ] Inclusion: `Rev(B, φ) ⊆ B + φ`
  - [ ] Vacuity: if `¬φ ∉ Cn(B)`, then `B + φ = Rev(B, φ)`
  - [ ] Consistency: if `φ` is consistent, so is `Rev(B, φ)`
  - [ ] Extensionality: logically equivalent `φ, ψ ⇒ same revision`

  ## (Optional) Mastermind Integration
- [ ] Encode game rules as beliefs
- [ ] Revise beliefs based on guess feedback
- [ ] Generate next guess from belief base
- [ ] Loop until code is found

## Horn Clause Optimization (Optional)
- [ ] Detect whether a clause is a **Horn clause**
- [ ] Identify **definite clauses** (exactly one positive literal)
- [ ] Identify **goal clauses** (no positive literals)
- [ ] Implement **forward chaining** inference for Horn clauses
- [ ] Implement **backward chaining** inference for Horn clauses
- [ ] Use Horn clause detection to optimize resolution/inference
- [ ] Add unit tests with Horn-only belief bases