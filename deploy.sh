#!/bin/bash

rm -rf ./dist
rm -rf ./build

python setup.py install
python setup.py sdist
twine upload dist/*
