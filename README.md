# Lab Overview

Basic overview of OOP design pattern, and how it differ between OOP and precedual programming

# Project Structure
```
oop_lab_1/
│
├── README.md             # This file
├── Cities.csv            # The dataset
├── data_processing.py	  # The analysis code
```

# Design Overview

## DataLoader

A class dedicated to loading CSV class

## Table

A table class that allows you to filter and aggegrate table, the filter function return an instance of Table, and the aggegrate return the output of aggerate function

The `table` attribute returns the CSV table
The `name` attributes returns the table name

# Running

```py
python data_processing.py
```