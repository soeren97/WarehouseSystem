# Warehouse management system
This is a toy example of a CLI-based warehouse system interacting with a MySQL server. In the program, it is possible to search for items and transactions as well as add them. Three logs will be created when adding transactions or items, which can also be displayed from the CLI. The system is designed in a way that new features can easily be added without creating issues for existing functionality.


## Installation Guide

### Prerequisites:
- Anaconda installed
- pip installed (usually comes with Anaconda)
- MySQL server installed
- Graphviz installed (for UML)

### Steps:

1. **Clone the Repository:**
`git clone https://github.com/soeren97/WarehouseSystem`

2. **Navigate to the Repository Directory:**
`cd */WarehouseSystem`

3. **Create a Virtual Environment (Optional but Recommended):**
`conda create -n your-env-name python=3.9`

4. **Activate the Virtual Environment:**
`conda activate your-env-name`

5. **Install Required Packages:**
`pip install .`

6. **Verify Installation:**
Ensure all dependencies are installed successfully without any errors.

7. **Deactivate Virtual Environment (If Created):**
`conda deactivate`

8. **Create config.json.**
Create a file containing the fields username and password in the repocetory directory.


### Additional Notes:

- **Virtual Environment:** Creating a virtual environment is a good practice to isolate project dependencies from other projects and the system Python environment.
- **pip Install:** The `pip install .` command installs the necessary packages specified in the `setup.py` file from the current directory.
- **requirements** The required packages can be found in the `setup.py` file as the variable `INSTALL_REQQUIRES`.
- **Diagrams** UML and ER diagrams can be generated using the `diagrams.py` file and will be located in a new folder called `Diagrams`.
