@echo off

if "%1"==""       GOTO USAGE
if "%1"=="tools"  GOTO TOOLS
if "%1"=="tools5" GOTO TOOLS5
if "%1"=="admin5" GOTO ADMIN5

:TOOLS	
set LINK="C:\Dev\workspace\EU-PRODUCTION-SUPPORT-1\ls-tools\defaultroot" 
set SERVER_DIR="c:\Dev\apps\jboss\jboss-5\server\tools\deploy"
GOTO DO

:TOOLS5
set LINK="C:\Dev\workspace\EU-PRODUCTION-SUPPORT-1\ls-tools5\src\main\webapp"
set SERVER_DIR="c:\Dev\apps\jboss\jboss-5\server\tools5\deploy"
GOTO DO

:ADMIN5
set LINK="C:\Dev\workspace\EU-PRODUCTION-SUPPORT-1\ls-admin5\src\main\webapp"
set SERVER_DIR="c:\Dev\apps\jboss\jboss-5\server\tools5\deploy"
GOTO DO

:DO
c:
echo %LINK%
cd "%SERVER_DIR%"
junction -d ls-%1.war > nul
rem if not exist "ls-%1.war" mkdir "ls-%1.war"
junction "ls-%1.war" %LINK%
goto END

:USAGE
echo.
echo Application name not specified.
echo eg:  link tools
echo.

:END
