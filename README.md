## Contributors 

Shawn Xiao Hu, Eugene You, Gilbert Akuja, Tien Nguyen

## very_fast_eda

[![Documentation Status](https://readthedocs.org/projects/fast-eda/badge/?version=latest)](https://fast-eda.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/UBC-MDS/fast_eda/graph/badge.svg?token=qRRzvujw3T)](https://codecov.io/gh/UBC-MDS/fast_eda)
[![ci-cd](https://github.com/UBC-MDS/fast_eda/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/fast_eda/actions/workflows/ci-cd.yml)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![PyPI - Version](https://img.shields.io/pypi/v/very_fast_eda)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/very_fast_eda)

The `very_fast_eda` package simplifies data exploration by providing key functions for quick insights. The `describe_function()` summarizes numeric columns with statistics like mean and median. The `distribution_plots()` visualizes both categorical and numeric columns using bar charts or histograms. The `counts_nulls()` identifies missing values in each column. The `correlation_matrix()` generates a correlation matrix between the features in the data frame. FastEDA helps users efficiently explore datasets and identify key patterns with minimal effort. 

- `describe_function()`:
Summarizes numeric columns in a DataFrame by calculating basic statistics such as mean, median, standard deviation, and range. It provides a quick overview of central tendencies and data spread.

- `distribution_plots()`:
Visualizes the distribution of both categorical and numeric columns by generating bar charts for categorical data and histograms for numeric data. This function helps in understanding the frequency distribution and patterns in the dataset.

- `counts_nulls()`:
Counts the number of missing values in each column of the DataFrame, providing a clear overview of data completeness. This function is useful for identifying columns that may require cleaning or imputation.

- `correlation_matrix_viz()`:
Generate a correlation matrix visualization for numeric columns in a DataFrame.

## Python Ecosystem Fit 

The `very_fast_eda` package fits into the broader Python ecosystem as a lightweight tool designed to simplify the initial stages of exploratory data analysis (EDA). While there are other Python packages that offer similar functionality, such as [ydata-profiling](https://github.com/ydataai/ydata-profiling), `very_fast_eda` differentiates itself by focusing on providing quick and efficient summary statistics, visualizations, and missing data counts in a minimalistic and easy-to-use format. `very_fast_eda` aims for speed and simplicity, making it ideal for users who need a quick, lightweight solution without overwhelming complexity.

Unlike  [ydata-profiling](https://github.com/ydataai/ydata-profiling) and `sweetviz`, which generate detailed, interactive HTML reports, `very_fast_eda` is designed for rapid, inline insights within a Jupyter Notebook or Python script, making it more suitable for quick exploratory work rather than full-fledged automated reporting. Additionally, `very_fast_eda` emphasizes computational efficiency, avoiding the performance overhead associated with generating large, complex reports.

## Installation

```bash
$ pip install very_fast_eda
```
## Documentation 

Our online documentation can be found [here](https://fast-eda.readthedocs.io/en/latest/?badge=latest)

## Usage

The `very_fast_eda` package simplifies data exploration by providing key functions used to get quick insights such as
distribution plots,null value counts, correlation matrix, descriptive statistics such as mean,median and standard deviations. 

Once you install `very_fast_eda` using pip, you can access the following functions as shown below in the examples.

``` bash
import seaborn as sns 
import pandas as pd 
import fast_eda.fast_eda as eda 

dist_plots = eda.distribution_plots(iris, 2, 3) # This will show distribution plots of the given dataset 

nulls_values = eda.count_nulls(iris) # This will show a summary of the number of null values in each rows 

correlation_matrix_plot = eda.correlation_matrix_viz(iris) # This will generate the correlation matrix for numeric columns

descriptions = eda.describe_function(iris) # This will generate summary statistics such as mean, medain and standard deviations 

```

## Running Tests

To make sure the `very_fast_eda` package is working properly on your system, you can run the testing scripts with `poetry` and `pytest`. 

If you don't have `poetry`, please install it first

```bash
pip install poetry
```

Run the following commands under the project root 

```bash
poetry run pytest --cov=fast_eda
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`very_fast_eda` was created by Tien Nguyen, Eugene You, Gilbert Akuja, Shawn Xiao Hu. It is licensed under the terms of the MIT license.

## Credits

`fast_eda` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
