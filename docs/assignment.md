# Technical Assignment

## Context

(not relevant to complete the exercise)A bank wants to build an AI model to estimate a loan applicant’s salary. Estimating the salary will help the bank in the decision towards accepting/rejecting the application. The data scientists want to use the [US Census dataset](https://www.kaggle.com/datasets/uciml/adult-census-income) available online as a training dataset for the AI model.

## Task overview

- Input dataset: Download from [Google Drive](https://drive.google.com/file/d/1hDIpnh_yxLqlbWUaEnxp8piTN82_wwhT/view?usp=sharing).
- Filesize: 5MB. 50,000 rows.
- Type: CSV, tabular, categorical & continuous columns.
- All column names: 'age', 'workclass', 'fnlwgt', 'education', 'marital-status', ‘occupation', 'relationship', 'race', 'sex', 'hours-per-week', 'native-country', 'capital', 'income'.
- Target column name: income.
- Code filename: Python
- Input parameters: The dataset path.
- Time: 30 min.
- Output: Through the terminal, just printing, no visualization needed.

> Use OOP and clean code principles to complete this exercise.

## Part 1: Continuous or Categorical ? (15 min)

Print which columns from the dataset are categorical or continuous.For categorical columns, print the amount of unique values in this column and its list of unique values.For continuous columns, print the amount of unique values in this column and its min/max range.


### Example output:

``` sh
age - continuous - 97 values - 0 to 120
sex - categorical - 2 values - Male, Female
...
```

### Condition:

A string column is categorical. A numeric column is categorical if it has equal/less than 10 unique values OR if all its values are unique, otherwise it is continuous.

## Part 2: Imbalanced ? (15 min)

Print if a categorical column is imbalanced, its minimum occurrence and the occurence of its classes.
All continuous columns are assumed to be balanced.

### Example output:

``` sh
sex - categorical - balanced -  5% min occurrence - Male 60%, Female 40%
race - categorical -  imbalanced - 3.33% min occurrence - White 60%, Black 30%, Asian 10%
age - continuous - balanced
...
```

Hint: a column is imbalanced if one of its categories occurs strictly less than 10% of its occurrence (known as the minimum occurrence). The occurrence is 100% divided by the number of categories. Eg: you have categories A, B, C, D  and E. The occurrence is 20% and the minimum occurrence is 2%. If one of the 5 categories occurs less than 2%, then the column is deemed imbalanced.

## Part 3: Generation! (Advanced - 2 hours)

It is now time to fix the imbalanced columns. 
Generate data points (new rows) to add to the input dataset so that all the columns become balanced.Bonus: generate the minimum amount possible.
Print the amount of rows added.Add the two datasets together and then call the part 2 function/object again.

Make sure to:

- Keep the previously balanced columns still balanced.
- Sample continuous columns randomly but within their min/max range.
- Due to its long tail distribution, it is ok if the ‘native-country’ variable is still unbalanced.

### Example output:

``` sh
100235 rows added 
sex - balanced
race - balanced
...
```
