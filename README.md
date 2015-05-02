

The working project is hosted on:
http://python-task-round.herokuapp.com/input/
http://python-task-round.herokuapp.com/student/

Also, the AngularJS code is in the pythonTask/static folder.

##Running the script:

  runProject.py is a python script that sets up the project on Windows and Linux systems, tested on Windows 7,8 and Ubuntu 14.10.
  
  The script uses a virtual environment, so the python installation(if already exists) is not modified.


####  Prerequisites:
If python *is not* already installed on windows, run the installPythonWin.bat. 

If you are using a distribution of Linux other than Debian or Ubuntu, install the packages libxml2-dev, libxslt1-dev, and python-dev.

If you are using a Linux virtual machine, allocate enough ram(1.5 GB recommended), or building one of the python dependancies(lxml) will fail.

If mongodb is already installed, make sure the Path variable has its location. If it is not installed, it gets installed and works via the script. 

Supplied and recommended version of Python is 2.7.9 and mongodb is 3.0.0.
	  

####  To execute:
  
######On Windows:
    
    cd <path to downloaded folder>
    <path to Python executable> runProject.py
      
  If Python is installed from the installPythonWin.bat, it is located in the requiredPackages\Python27 folder.

######On Linux:
    
    cd <path to downloaded folder>
    sudo /usr/bin/python runProject.py



##Accessing the app:

######To enter student and behavior records, go to the url:
  
    127.0.0.1:8000/input
    
  You can check the browser console for messages.

######To view the student records, sorted by date:
  
    127.0.0.1:8000/student

######To access the database api:
  
    127.0.0.1:8000/api/v1



##Cleanup:

######On Windows:
  
  Uninstall mongodb and python if required.
    
  Delete the downloaded folder

######On Linux:
  
  Just delete the downloaded folder.
