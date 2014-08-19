@echo off
rem : Maven 3 script
rem Written - Use Maven 2 and Maven 3 on the same machine

rem set OLDM2_HOME=%M2_HOME%
set M2_HOME=C:\Dev\apps\maven-3.0.3

rem set OLDPATH=%PATH%
rem set PATH=%M2_HOME%\bin;%PATH%;

rem echo %PATH%
C:\Dev\apps\maven-3.0.3\bin\mvn %1 %2 %3 %4 %5 %6 %7

rem set M2HOME=%OLDM2_HOME%
rem set PATH=%OLDPATH%
rem mvn clean compile gwt:eclipse eclipse:eclipse
