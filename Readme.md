Project Logs Analysis

This project requires a virtual environment which will be made using combination of Virtual Box and Vagrant.

Steps for Installation

Step 1:
Clone the project repository and connect to the virtual machine
$ git clone https://github.com/mlupin/fullstack-nanodegree-logs-analysis.git

Step 2:
$ cd fullstack-nanodegree-logs-analysis
$ vagrant up

Step 3:
$ vagrant ssh

Step 4:
$ cd /vagrant

Step 5:
Now load the file containing all the data regarding the log here. Name of the file is newsdata.sql.

Step 6:
$ psql -d news -f newsdata.sql

Running the project:

Step 7:
$ python log.py

Step 8:
Open your browser and go to the localhost:8000

Step 9:
Click the button to get te=he desired output