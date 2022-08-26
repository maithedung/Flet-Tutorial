# Packaging desktop app
## On Windows
- pip install pyinstaller
- pyinstaller your_program.py
- dist\your_program\your_program.exe

### Hide that console window
- pyinstaller your_program.py --noconsole --noconfirm

### Bundling to one file
- pyinstaller your_program.py --noconsole --noconfirm --onefile

