# Packaging PyTorch with [PyInstaller](https://github.com/pyinstaller/pyinstaller-hooks-contrib)

PyInstaller hooks are required to allow PyTorch to be bundled. The hooks package should automatically be installed when installing PyInstaller.

The documentation provides more details into Hooks, and how to bundle(Page 69, [Understanding PyInstaller Hooks](https://readthedocs.org/projects/pyinstaller/downloads/pdf/latest/)).

`cx_Freeze` [may also be required](https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python) to bundle a Python script with PyTorch.
