# Packaging ~PyTorch~ *opencv* with [PyInstaller](https://github.com/pyinstaller/pyinstaller-hooks-contrib)

**Update: It seems the culprit when bundling with `easyocr` is not PyTorch, but `opencv`**

## Changelog

- [*See here*](https://stackoverflow.com/questions/67494128/pyinstaller-modulenotfounderror-no-module-named-cv2)
    - `pyinstaller` downgraded to 4.5.1
    - `pyinstaller-hooks-contrib` downgraded to 2021.3, from 2022

PyInstaller hooks are required to allow PyTorch to be bundled. The hooks package should automatically be installed when installing PyInstaller.

The documentation provides more details into Hooks, and how to bundle(Page 69, [Understanding PyInstaller Hooks](https://readthedocs.org/projects/pyinstaller/downloads/pdf/latest/)).

`cx_Freeze` [may also be required](https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python) to bundle a Python script with PyTorch.

## Bundling the Package

Run the following, before navigating and executing `./dist/main/main.exe`

```
pyinstaller --collect-all easyocr main.py
```
