### RpkConverter

This tool is used to convert rpk file to Anki apkg.

如果遇到任何问题，请发起issue，并描述情况。如果转换rpk出现问题，请将文件发到邮箱 `ssqyang [AT] outlook.com`，我会debug并修复问题。

# Build

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

