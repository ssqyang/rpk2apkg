### RpkConverter

This tool is used to convert rpk file to Anki apkg.

To pack the .py files into executable file, please execute the following command in the command line:

```shell
# if pyinstaller is not installed
pip install pyinstaller
# -w will hide the console window
# Windows
pyinstaller -w -F main.py --add-data "static/*;./static" --workpath temp --distpath . -n RpkConverter.exe
# Mac
pyinstaller -w -F main.py --add-data "static/*:./static" --workpath temp --distpath . -n RpkConverter
```

The pyinstaller will generate /temp directory to store temp files, which can be deleted manually.

