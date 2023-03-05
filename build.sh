# build the packages

python -m pip install build twine
python -m build

# automatically look for issues in the build

twine check dist/*

# manually verify that they were built correctly

cd dist/
unzip grade_calculator-0.0.0-py3-none-any.whl -d grade-calculator.whl # update version numbering as necessary
tree grade-calculator.whl/