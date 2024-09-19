# Co2emissions


The dataset 'visualizing_global_co2_data.csv' contains high percentage of missing values.

| Column                        | Percentage Missing |
|-------------------------------|--------------------|
| country                       | 0.000000           |
| year                          | 0.000000           |
| iso_code                      | 16.712123          |
| population                    | 20.929681          |
| gdp                           | 71.216254          |
| ...                           | ...                |
| temperature_change_from_n2o   | 25.649235          |
| total_ghg                     | 87.847346          |
| total_ghg_excluding_lucf      | 87.847346          |
| trade_co2                     | 91.582671          |
| trade_co2_share               | 91.584648          |


 Our purpose is then tackle the problem following the approach:

- Columns with Low Missing Values (e.g., less than 20%):
For columns with relatively few missing values, we might consider imputation methods such as mean, median, mode imputation, or using more sophisticated methods like KNN imputation or interpolation.

- Columns with Moderate Missing Values (e.g., between 20% and 50%):
For columns with a moderate percentage of missing values, we could use more advanced imputation methods like KNN imputation, iterative imputation (e.g., MICE), or consider building predictive models to estimate missing values based on other features.

- Columns with High Missing Values (e.g., over 50%):
Columns with a high percentage of missing values may require careful consideration. Depending on the importance of these columns to your analysis, we might decide to drop them if they are not critical.
