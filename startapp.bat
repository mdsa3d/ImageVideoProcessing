@echo off
title [Extract Image From Video - WebApp]
set path=%CD%
call %path%\venv\Scripts\activate.bat
cd %path%\src
call streamlit run src\app.py --server.port 80
@REM @echo %path%