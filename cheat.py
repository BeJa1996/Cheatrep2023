def cheat(assignment):
    """This function returns the correct solution to any of the assignments from week one.
        Please insert the assignment number as a string."""

    if assignment == "Q1.2P.1":
        return print("\n",
                     "import numpy as np  # imports the `numpy` module with the alias `np`\n",
                     "import pandas as pd # generally you would put all import statements at the top\n",
                     "                    # of the script - enables, e.g., easy installation of all\n",
                     "                    # relevant packages")
    elif assignment == "Q1.2P.2":
        return print("\n",
                     "another_array = np.zeros((2, 4, 6))\n",
                     "# valid solution #1 - indexes the single element\n",
                     "print(another_array[-1, 0, 2])\n",
                     "# valid solution #2 - subsets the full dimension\n",
                     "print(another_array[:, 0, :])\n",
                     "print(another_array[:, :, 2])\n",
                     "print(another_array[-1, :, :])\n",
                     "# Generally, remember that Python (in contrast to R)\n",
                     "#     - is zero-indexed (indices go from 0 to (n-1))\n",
                     "#     - negative indices \"invert\" the access instead of deselection\n",
                     "#     - you need to indicate fully indexed dimensions with a colon\n")
    elif assignment == "Q1.2P.3":
        return print("\n",
                     "another_array = np.zeros((2, 4, 6))\n",
                     "new_array = another_array.copy()\n",
                     "# alternatively: new_array = np.copy(another_array)\n",
                     "new_array[1, 2, 2] = 1\n",
                     "print(f\"another: '{another_array[1, 2, 2]}' vs. new: '{new_array[1, 2, 2]}'\")\n",
                     "# In Python, when using =, we only assign a reference to an object in memory,\n",
                     "# so both new_array and another_array are pointing to the same memory\n",
                     "# allocation, namely, the one created by np.zeros(). To make a true copy, you\n",
                     "# can use the .copy() method or np.copy().")
    elif assignment == "Q1.2P.4":
        return print("\n",
                     "%paste  # does not work in a python script\n",
                     "        # it is only defined for iPython terminal execution\n",
                     "        # in native Python, `%` is the modulo operator")
    elif assignment == "Q1.2P.5":
        return print("\n",
                     "# to change the working directory:\n",
                     "%cd \"your directory\"\n",
                     "# print the current working directory:\n",
                     "%pwd\n",
                     "# list the contents of the working directory:\n",
                     "%ls\n",
                     "# list current workspace variables:\n",
                     "%who   # variable names\n",
                     "%whos  # objects with additional information\n")
    elif assignment == "Q1.2P.6":
        return print("\n",
                     "pip install pip-install-test   # using your terminal\n",
                     "%pip install pip-install-test  # using the iPython console")
    else:
        return print("Not yet created.")


cheat("Q1.2P.1")

