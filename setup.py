#!/usr/bin/env python

from distutils.core import setup

setup(
  name='used-cars-price-predictor',
  version='1.0',
  description='Predicts prices of used cars',
  author='Ivan Stefanov',
  author_email='isteffanov@gmail.com',
  packages=['price_predictor', 
            'price_predictor/data_preparation',
            'price_predictor/trainers'],
  
)