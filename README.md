## Contributors 

Shawn Xiao Hu, Eugene You, Gilbert Akuja, Tien Nguyen

## fast_eda

[![Documentation Status](https://readthedocs.org/projects/fast-eda/badge/?version=latest)](https://fast-eda.readthedocs.io/en/latest/?badge=latest)
[![ci-cd](https://github.com/UBC-MDS/fast_eda/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/fast_eda/actions/workflows/ci-cd.yml)

The `fast_eda` package simplifies data exploration by providing key functions for quick insights. The `describe_function()` summarizes numeric columns with statistics like mean and median. The `distribution_plots()` visualizes both categorical and numeric columns using bar charts or histograms. The `counts_function()` identifies missing values in each column. The `correlation_matrix()` generates a correlation matrix between the features in the data frame. FastEDA helps users efficiently explore datasets and identify key patterns with minimal effort. 

- `describe_function()`:
Summarizes numeric columns in a DataFrame by calculating basic statistics such as mean, median, standard deviation, and range. It provides a quick overview of central tendencies and data spread.

- `distribution_plots()`:
Visualizes the distribution of both categorical and numeric columns by generating bar charts for categorical data and histograms for numeric data. This function helps in understanding the frequency distribution and patterns in the dataset.

- `counts_nulls()`:
Counts the number of missing values in each column of the DataFrame, providing a clear overview of data completeness. This function is useful for identifying columns that may require cleaning or imputation.

- `correlation_matrix_viz()`:
Generate a correlation matrix visualization for numeric columns in a DataFrame.

The `fast_eda` package fits into the broader Python ecosystem as a lightweight tool designed to simplify the initial stages of exploratory data analysis (EDA). While there are other Python packages that offer similar functionality, such as [ydata-profiling](https://github.com/ydataai/ydata-profiling), `fast_eda` differentiates itself by focusing on providing quick and efficient summary statistics, visualizations, and missing data counts in a minimalistic and easy-to-use format. FastEDA aims for speed and simplicity, making it ideal for users who need a quick, lightweight solution without overwhelming complexity.

## Installation

```bash
$ pip install fast_eda
```
## Documentation 

Our online documentation can be found [here](https://fast-eda.readthedocs.io/en/latest/?badge=latest)
## Usage

The fast_eda package simplifies data exploration by providing key functions used to get quick insights such as
distribution plots,null value counts, correlation matrix, descriptive statistics such as mean,median and standard deviations. 

Once you install fast_eda using pip, you can access the following functions as shown below in the examples.

``` bash
import fast_eda.fast_eda as eda 
import seaborn as sns 
import pandas as pd 


dist_plots = eda.distribution_plots(iris, 2, 3) # This will show distribution plots of the given dataset 

nulls_values = eda.count_nulls(iris) # This will show a summary of the number of null values in each rows 

correlation_matrix_plot = eda.correlation_matrix_viz(iris) # This will generate the correlation matrix for numeric columns

descriptions = eda.describe_function(iris) # This will generate summary statistics such as mean, medain and standard deviations 

```

## Running Tests
To make sure the fast_eda package is working properly on your system, you can run the testing scripts with pytest. This will require you to have pytest installed on your system.

```bash
$ pip install pytest
```

You will then need to clone the repository on to your machine and navigate to the root directory. Once that is done you can execute the following command to run our testing scripts:

```bash
$ pytest
```

To get a view of the test coverage, you can run the following command:

```bash
$ pytest --cov=src/fast_eda
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`fast_eda` was created by Tien Nguyen, Eugene You, Gilbert Akuja, Shawn Xiao Hu. It is licensed under the terms of the MIT license.

## Credits

`fast_eda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
