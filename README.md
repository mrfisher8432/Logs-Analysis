
# Logs Analysis

This is a reporting tool that will print out 3 reports based on the data in the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

#### Programming Language:

[Python](https://www.python.org/) - Tested on ver. 2.7.10

#### Virtual Machines

Download and Install:

[Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
[Vagrant](https://www.vagrantup.com/downloads.html)

Download and unzip the configuration package [VM Config](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) prepared by Udacity. Inside the `vagrant` subdirectory, along with other starter project, clone this repository. On terminal, at the same subdirectory, run `vagrant up`, then `vagrant ssh`.

Download and unzip the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here to the `vagrant` subdirectory. Run `psql -d news -f newsdata.sql`. This will connect and setup the database server.

## Running the Script

On your terminal in vagrant, run this command:  

````
python report.py
````
