@echo off
python --version 2>NUL
if errorlevel 1 goto noPython

:startServer
python ket.py
pause

:noPython
echo Python required; see https://www.python.org/downloads/
pause