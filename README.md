# Lab Overview

Basic overview of OOP design pattern, and how it differ between OOP and precedual programming.

# Project Structure
```
oop_lab_3/
│
├── README.md             # This file
├── Cities.csv            # The Cities dataset
├── Countries.csv         # The Countries dataset
├── data_processing.py	  # The analysis code
```

# Design Overview

## DataLoader

A class dedicated to loading CSV class

The `load_csv` class returns a dictionary of the file_name provided

## Table

A table class that allows you to filter and aggegrate table, the filter function return an instance of Table, and the aggegrate return the output of aggerate function

The `table` attribute returns the CSV table
The `name` attributes returns the table name

the

## DB

A class for holding data

The `insert` function insert `key` into the database with `value`
The `search` function search for `key` and return it's value

# Running

```py
python data_processing.py
```