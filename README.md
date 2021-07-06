# ENPM-809E

Here is a summary of the tasks to do for this assignment.
1. Test PDDL files:
(a) Download the PDDL domain and problem files from Canvas.
(b) Uncomment the dynamic predicates and functions that are in the init and goal states.
(c) Run the planner on these two files to make sure the PDDL files are correct and that the planner can generate a
plan. You can place these 2 files in the same folder as your planner and run:
./popf3-clp rwa2-domain.pddl rwa2-problem.pddl
2. User inputs:
(a) Write a Python program which accepts user inputs, as described in Section 4.
(b) Store these inputs in a Python data structure because you will need them in the next step.
3. Update PDDL problem file:
 (a) Using the user inputs you stored in the previous step, update dynamic predicates in the init and goal states of the PDDL problem file. In the next two figures, I provided the full init and goal states. I highlighted the only things that you need to update from user inputs. Do not modify anything else!!!. To help you out, I have provided a small program (fileio.py) which:
• Opens the PDDL problem file.
• Stores its content in a Python list.
• Updates some items in the list from user inputs.
• Generates a new PDDL problem file (leaving the original one alone).
4. Run planner on PDDL files:
(a) Now that you have a new PDDL problem file which you updated from user inputs, you need to run the planner on the domain file and the (new) problem file.
(b) You have to run the PDDL planner from a Python program. The code to do this was provided in class in pythonshell.py. You just need to modify the value of some variables based on the location of the domain file, the problem file, and the planner on your system.
(c) The planner will generate a plan. You will need to store this plan in a data structure for the next step. You can, for instance, store each line of the plan as an item in a Python tuple or list.
5. Execute the plan:
(a) Now that you have a sequence of PDDL actions (plan) stored in a Python data structure, you need to iterate over this data structure and call a method (see Section 5) for each action.
(b) When this program executes we should see strings being printed out on the screen.
