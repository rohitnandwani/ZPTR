import platform
import os
import subprocess
import time
import checkPath
#import virtualenv

OSName = platform.system()
myPath =  os.path.dirname(os.path.abspath(__file__))

os.chdir(os.path.join(myPath, 'requiredPackages'))


if(OSName=='Windows'):
    #subprocess.call("msiexec /i python-2.7.9.msi TARGETDIR=\""+ os.getcwd() + "\\Python27\" /qb", shell=True)
    subprocess.call("msiexec.exe /i mongodb-win32-x86_64-2008plus-ssl-3.0.0-signed.msi INSTALLLOCATION=\""+ os.getcwd() +"\\mongodb-win\" ADDLOCAL=ALL /qb", shell=True)
    pythonExeMain = "\"" + os.getcwd() + "\\Python27\\python\""
if(OSName=='Linux'):
    pythonExeMain = os.path.join(os.sep + 'usr', 'bin', 'python')
    subprocess.call(pythonExeMain+" get-pip.py", shell=True)
    if(platform.linux_distribution()[0] == 'Ubuntu' or platform.linux_distribution()[0] == 'Debian'):
        subprocess.call("apt-get install libxml2-dev libxslt1-dev python-dev", shell=True)

import pip


pip.main(['install', 'virtualenv==1.10.1'])
subprocess.call(pythonExeMain+" -m virtualenv pythonVirtualEnvironment", shell=True)


if(OSName=='Windows'):
    pythonExeVenv = "\"" + os.getcwd() + "\\pythonVirtualEnvironment\\Scripts\\python\""
if(OSName=='Linux'):
    pythonExeVenv = os.path.join(os.getcwd(), 'pythonVirtualEnvironment', 'bin', 'python')


subprocess.check_call(pythonExeVenv+" -m pip install --upgrade pip", shell=True)
print "Installing python dependencies"
subprocess.check_call(pythonExeVenv+" -m pip install -r requirements.txt", shell=True)


print "Starting the mongodb service"

if not os.path.exists(os.sep + os.path.join('data', 'db')):
    os.makedirs(os.sep + os.path.join('data', 'db'))
if not (checkPath.is_in_path('mongod') or checkPath.is_in_path('mongod.exe')):
	os.chdir(os.path.join(myPath, 'requiredPackages', 'mongodb-'+OSName.lower()[0:3], 'bin'))
subprocess.Popen("mongod --smallfiles", shell=True)


print "Waiting for mongodb to get initialized"
time.sleep(10)


print "Starting the Django server"
os.chdir(os.path.join(myPath, 'mysite3'))
subprocess.Popen(pythonExeVenv+" manage.py runserver", shell=True)


print "Done"




