# tests that uploading works correctly by using testpypi before pypi

venv deactivate
#python3 -m pip install --upgrade build
#python3 -m build
pip3 install --upgrade pip
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*

source venv/bin/activate