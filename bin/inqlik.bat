@echo off
SET BINDIR=%~dp0
"%BINDIR%dart.exe" "%BINDIR%inqlik.snapshot" %*
