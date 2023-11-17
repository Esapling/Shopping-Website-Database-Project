To run the project , please first activate the virtual environment otherwise you need to download 
packages one by one. 
->To activate the virtual environment open the terminal in the project folder and run the command 
    source venv/bin/activate

if you are having problem on windows machines , try this instead
    venv/bin/activate

-> make sure your your python interpreter is selected as the one in venv/bin
    press (Ctrl+Shift+P) select python interpreter , select it as ./venv/bin/python

In order to work with databases you need to set paramters user name, database name ,and a password 
please see set_initials method in the database_manager file

after setups run the server file as python server.py 


if you are having issues with packages , you can try completely remove the venv file and install it again for this , in your terminal, run the command 
    run rm -rf venv/  --removes the virtual environment
    python -m venv venv --or python3 -m venv venv , installs the virtual envrionment with name venv
    pip install -r requirements.txt -- installs all necessary packages


