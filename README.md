# Project Name

A Shopping Web site project with a database. 
This is a ITU BLG317E – DATABASE SYSTEMS course project 
Aim is to design an efficient database with a frontend website

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Brief instructions on how to install/setup your project. Include necessary dependencies, prerequisites, and installation steps.


Its highly recommended to use a virtual environment for the project , if you dont want to use it you can skip the 3-4-5 steps

For example:
1. Clone the repository: `git clone https://github.com/yourusername/yourproject.git`
2. Navigate to the project directory: `cd yourproject`
3. Install a virtual envrionment with name venv: `python -m venv venv --or python3 -m venv venv`
4. Activate the virtual environment: 
        `source venv/bin/activate`, on linux machines
        `venv/bin/activate`, on windows machines
5. Set your python interpreter as in the venv file :
        `Ctrl+Shift+P` -> select python interpreter -> `./venv/bin/python`
6. Install dependencies: `pip install -r requirements.txt`

## Usage

In order to work with databases you need an active postgres database and set paramters: user name, database name ,and a password accordingly please see `set_initials` method in the `database_manager` file

1. Run the project: `python server.py`
2. Open your web browser and go to `http://localhost:5000` to view the application.

## Contributing

--

## License

This project is licensed under the [MIT License](LICENSE).



