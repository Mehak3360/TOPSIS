# TOPSIS – Multi-Criteria Decision Making Tool

This package implements the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method, a popular **Multi-Criteria Decision Making (MCDM)** technique used to rank alternatives based on their distance from an ideal best and an ideal worst solution.

TOPSIS is widely used in various domains such as:

- Product selection and comparison  
- Supplier evaluation  
- Project prioritization  
- Performance assessment  
- Resource allocation  

## Installation

Install the package using `pip`:

```bash
pip install topsis-mehak-102303699==0.2

### Command Line Syntax
- `python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>`

### Parameters Description

| Parameter | Description |
|-----------|------------|
| InputDataFile | CSV file containing alternatives and criteria values |
| Weights | Comma separated numeric weights |
| Impacts | Comma separated impacts (+ for benefit, - for cost) |
| OutputFile | Name of the output CSV file |

### Example 
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,-" output.csv

* Note: Please check that the number of weights and impacts entered matches the total number of criteria (features) in the input file.

## Output
The program generates an output CSV file containing the TOPSIS results.
-Example:
<img width="519" height="163" alt="image" src="https://github.com/user-attachments/assets/152e2004-02e8-410a-be3e-3b0f690b076f" />
