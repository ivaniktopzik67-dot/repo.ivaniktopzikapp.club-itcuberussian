@echo off
echo Удаление «Побег из школы 4–5»...

set "INSTALL_DIR=%PROGRAMFILES%\EscapeFromSchool4-5"

:: Удаляем папку игры
rmdir /S /Q "%INSTALL_DIR%"


:: Удаляем ярлык
del "%USERPROFILE%\Desktop\Побег из школы 4-5.lnk" 2>nul

echo Игра удалена!
pause
