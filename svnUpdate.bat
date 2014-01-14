@echo off

set SRCDIR=E:\Downloads\ITSy\JavaProjects-2012-10-23\JavaProjects
set DESDIR=C:\dev\workspace\ITSy-integration

for %%a in (Proximity Systec LifeTecEliteStatsExtractor Isolator IntegratorClient Integrator DovacEliteProcessFlow DovacEliteIdhq DovacEliteCommon DovacEliteAdmin) do (
	robocopy %SRCDIR%\%%a\src %DESDIR%\%%a\src /MIR
)

for %%a in (DovacEliteDHQ DovacEliteKiosk LifeTecBioLab LifeTecDE LifeTecElite LifeTecElitePM LifeTecIDB LifeTecManufacturing LifeTecTeleTec) do (
	robocopy %SRCDIR%\%%a\src %DESDIR%\%%a\src /MIR
	robocopy %SRCDIR%\%%a\web %DESDIR%\%%a\WebContent /MIR
)

:End
pause