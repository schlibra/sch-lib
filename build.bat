@echo off
rd /s /q dist
python -m build
twine upload --repository-url http://pypi dist\*