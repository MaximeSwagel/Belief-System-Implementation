# 02180_intro_to_ai_group_28_assignment_2

This project is the implementation of a belief base revision system in Python, submitted for the DTU course in a group of 4 *02180 Introduction to Artificial Intelligence*. It follows the AGM postulates and includes support for contraction, expansion, and revision. The system is tested with a suite of unit tests, and an optional Mastermind solver is also implemented using the belief revision engine.

# Collaboration
The coding work was divided evenly, and we collaborated closely on all tasks.  
For reference, the original group repository can be found [here](https://github.com/MagnusStarkadOttosen/02180_intro_to_ai_group_28_assignment_2).

## How to Run
Just need python 3.7+

### Tests
You can run the test with the following commands:
python parser_test.py
python cnf_test.py
python resolution_test.py
python contraction_test.py
python expansion_test.py
python belief_base_test.py
python mastermind_test.py

### Mastermind
You can run the mastermind with the following command:
python mastermind.py

You can also change the parameters in mastermind.py  main()
You can change the goal and the amount of colors.
We recommend not going that high with the amount of colors, as it gets exponentially slower.
