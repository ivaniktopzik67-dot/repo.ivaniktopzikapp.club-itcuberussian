@echo off
echo Запуск «Побег из школы 4–5»...

:: Проверяем наличие Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python не установлен! Установите Python 3.8+
    pause
    exit /b 1
)

:: Запускаем игру
cd /d "%~dp0"
python game.py

pause
