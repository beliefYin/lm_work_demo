pyinstaller -w -F -i res/admin.ico admin.py

pyinstaller -w -F -i res/app.ico main.py

xcopy res dist\res\ /y /s

pause