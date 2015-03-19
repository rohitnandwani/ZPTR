SET mypath=%~dp0
echo %mypath:~0,-1%

cd %mypath:~0,-1%\requiredPackages

REM Install Python
msiexec /i python-2.7.9.msi TARGETDIR="%mypath%\requiredPackages\Python27" /qb