#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 18:45:44 2018

@author: ryantmcnally
"""

## meRM 1.0
## 2018-10-09
## Lightweight logger tool build to be people readable

import pandas as pd

## Intro text
print('meRM 1.0')

## ---
## Load a bunch of things

## Load in the list of things
things = pd.read_csv('things.csv')

## Load in the list of companies
##companies = pd.read_csv('companies.csv')

## Load in the list of projects
##projects = pd.read_csv('projects.csv')

## Load in the list of people
##people = pd.read_csv('people.csv')

## Load in the thing descriptor options
direction = pd.read_csv('direction.csv')
how = pd.read_csv('how.csv')
what = pd.read_csv('what.csv')

## ---
## Format the data

## Shifts the index to align with the card number
## Replaces NaN with a whitespace
things.index += 1
things = things.fillna('')

## ---
## Input for how the thing took place
how_input = input('How did the thing take place: ')
direction_input = input('To, from, or with:            ')
who_input = input('Who with (person id)?:        ')
what_input = input('What type of thing:           ')
description_input = input('Thing description:            ')

    
    
