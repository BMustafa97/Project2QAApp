#!/bin/bash

# test service-1
cd ./service-1
pip3 install -r requirements.txt
pytest --cov=app --cov-report=term-missing
cd ..

# test service-2
cd ./service-2
pytest --cov=app --cov-report=term-missing
cd ..

# test service-3
cd ./service-3
pytest --cov=app --cov-report=term-missing
cd ..

# test service-4
cd ./service-4
pytest --cov=app --cov-report=term-missing
cd ..