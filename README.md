
# Logs Analysis

This is a reporting tool that will print out 3 reports based on the data in the database.

## Getting Started

Please follow these instructions in order to run this project locally.

### Prerequisites

#### Programming Language:

[Python](https://www.python.org/) - Tested on ver. 2.7.10

#### Virtual Machines

Download and Install:

[Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) | 
[Vagrant](https://www.vagrantup.com/downloads.html)

Download and unzip the configuration package [VM Config](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) prepared by Udacity. Change into the `vagrant` directory and clone this repository. On your terminal, at the same subdirectory, run `vagrant up`, then `vagrant ssh`.

Download and unzip the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here to the `vagrant` directory. Run `psql -d news -f newsdata.sql`. This will connect and setup the database server.

## Running the Script

Finally, in your terminal in Vagrant VM, run this command:  

````
python report.py
````
