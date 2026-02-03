# TOPSIS

## Overview
This project implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method using Python.
TOPSIS is a multi-criteria decision-making technique used to rank alternatives based on their closeness to the ideal solution.
The program is designed as a **command-line tool** and supports both **CSV and Excel (.xlsx) input files**.

- IF an excel file is provided,it is automatically converted into csv format before processing.
---
## Features
- Command line based execution
- Supports CSV and Excel input files
- Automatic Excel to CSV conversion
- Input validation and error handling
- Generates ranked output in CSV format
- Implements complete TOPSIS algorithm

---
## Methodology 
TOPSIS works by comparing each alternative with two reference solutions:
- Ideal best solution
- Ideal worst solution

### Steps to follow :
1. **Normalize the Dataset**  
   Convert raw data into comparable scale values.

2. **Apply Weights to Each Criterion**  
   Assign importance to each parameter using given weights.

3. **Determine Ideal Best and Worst Solutions**  
   - Identify best values for each criterion  
   - Identify worst values for each criterion  

4. **Calculate Distance from Ideal Solutions**  
   - Distance from Ideal Best Solution  
   - Distance from Ideal Worst Solution  

5. **Compute TOPSIS Score**  
   Calculate relative closeness of each alternative to the ideal solution.

6. **Rank Alternatives**  
   - Higher TOPSIS Score → Better Rank  
   - Lower TOPSIS Score → Lower Rank  

---
## Input Format
The program accepts input through the command line.

### Command Line Syntax
`python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>`
---
### Parameters Description

| Parameter | Description |
|-----------|------------|
| InputDataFile | CSV file containing alternatives and criteria values |
| Weights | Comma separated numeric weights |
| Impacts | Comma separated impacts (+ for benefit, - for cost) |
| OutputFile | Name of the output CSV file |
---
### Example 
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,-" output.csv

* Note: Please check that the number of weights and impacts entered matches the total number of criteria (features) in the input file.
---
## Output
The program generates an output CSV file containing the TOPSIS results.
-Example:
<img width="519" height="163" alt="image" src="https://github.com/user-attachments/assets/152e2004-02e8-410a-be3e-3b0f690b076f" />







