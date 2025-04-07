# Mastermind
A simplified version of Mastermind

- The secret code with 2 pegs
- Colors: Red (R), Green (G), Blue (B), Yellow (Y)

Repetition is allowed, so there is 4x4=16 possible combinations.

## Step 0: Intitial Belief base
```python
K = {
    (R, R), (R, G), (R, B), (R, Y),
    (G, R), (G, G), (G, B), (G, Y),
    (B, R), (B, G), (B, B), (B, Y),
    (Y, R), (Y, G), (Y, B), (Y, Y)
}
```

In this example the secret code is (G, Y). The agent dont know this.

## Step 1: First guess = (R, G)
### Feedback
By guessing (R, G) the agent gets back the feedback: 1 white peg.

This means:
- One correct color, wrong position
- No correct colors in correct positions

### Analysis

From this we can infer the following:
- The guess (R, G) contains: R and G
- So the code must have either R or G
- But not in those positions

Therefor we can filter:
- Remove all codes the dont have R or G at all
- Remove codes that have R in position 1
- Remove codes that have G in position 2
- Rome all codes that have both R and G at the same time

### Revised belief base
```python
K = {
    (G, B), (G, Y),
    (B, R),
    (Y, R)
}
```
## Step 2: Second guess = (G, B)
### Feedback
By guessing (G, B) the agent gets back the feedback: 1 black peg.

This means:
- One correct color in correct position
- One wrong color

### Analysis

From this we can infer the following:
- The guess (G, B) contains: G and B
- So the code must have either G or B
- In that position

Therefor we can filter:
- Remove all codes the dont have G or B at all

### Revised belief base
```python
K = {
    (G, B), (G, Y),
    (B, R),
}
```

## Step 3: Third guess = (B, R)
### Feedback
By guessing (B, R) the agent gets back the feedback: no pins.

This means:
- Nothing is correct

### Analysis

From this we can infer the following:
- The guess (B, R) contains: B and R
- So the code must have neither B or R

Therefor we can filter:
- Remove all codes the have B or R

### Revised belief base
```python
K = {
    (G, Y)
}
```

## Step 4: Final guess
There is only one possibility left so the agent knows that is the correct answer.

And the agent is correct.




# Simple example with boolean
|$C1_R$|$C1_G$|$C2_R$|$C2_G$|
|---|---|---|---|
|0|1|0|1|
|0|1|1|0|
|1|0|0|1|
|1|0|1|0|


Each code combinations can be written as:
- $(R, G) \rightarrow C1_R \land C2_G$
- $(G, R) \rightarrow C1_G \land C2_R$

The secret code is $(G, R)$

## Step 1: Guess = $(R, R) \rightarrow C1_R \land C2_R$
### Feedback
1 black peg.

- One color is correct, wrong location

### Analysis
- There is exactly one red color

### Revised belief base
```python
K = {
    C1_R ∧ C2_R,
    C1_R ∧ C2_G,
    C1_G ∧ C2_R,
    C1_G ∧ C2_G
}
```
|Guess|Symbol|# of R|Valid?|
|---|---|---|---|
|(R, R)|C1_R ∧ C2_R|2|No|
|(R, G)|C1_R ∧ C2_G|1|Yes|
|(G, R)|C1_G ∧ C2_R|1|Yes|
|(G, G)|C1_G ∧ C2_G|0|No|
```python
K = {
    C1_G ∧ C2_R
}
```

Only one possibility left
