# understanding-datasets
Repository to publish notebooks and PDF files for understanding different aspects of datasets like distributions, feature correlations and imbalances. The notebooks and PDF files have been generated using the open source project [data.understand](https://github.com/ggupta2005/data.understand).

## Generating PDF reports and jupyter notebooks
The generate the PDF reports and the notebooks you need install [data-understand](https://pypi.org/project/data-understand/) and [rai-test-utils](https://pypi.org/project/rai-test-utils/).

```
pip install --upgrade data-understand
pip install rai-test-utils
```

Once the installation of the above two packages in complete, you can then run the python code in the files `generate_data_insights_classification_datasets.py` and `generate_data_insights_regression_datasets.py`

```
python generate_data_insights_classification_datasets.py
python generate_data_insights_regression_datasets.py
```

This should generate the PDF reports and jupyter notebooks in the corresponding directories.

## Generated PDF reports and jupyter notebooks for classification datasets
| Dataset | PDF report | jupyter notebook |
| -------- | -------- |-------------------|
| [adult](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/adult/adult.csv) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/adult/adult.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/adult/adult.csv.ipynb) 
| [cancer](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/cancer/cancer.csv) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/cancer/cancer.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/cancer/cancer.csv.ipynb)
| [iris](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/iris/iris.csv) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/iris/iris.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/iris/iris.csv.ipynb)
| [titanic](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/titanic/titanic.csv) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/titanic/titanic.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/titanic/titanic.csv.ipynb)
| [wine](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/wine/wine.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/wine/wine.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/classification/wine/wine.csv.ipynb)

Following are some links for PDF reports which were generated for some regression datasets:-
- [diabetes](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/diabetes/diabetes.csv.pdf)
- [energy](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/energy/energy.csv.pdf)
- [housing](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/housing/housing.csv.pdf)

## Generated PDF reports and jupyter notebooks for regression datasets
| Dataset | PDF report | jupyter notebook |
| -------- | -------- |-------------------|
| [diabetes](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/diabetes/diabetes.csv.ipynb) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/diabetes/diabetes.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/diabetes/diabetes.csv.ipynb)
| [energy](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/energy/energy.csv) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/energy/energy.csv.pdf) | [link](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/energy/energy.csv.ipynb)

Following are some links for jupyter notebooks which were generated for some regression datasets:-
- [diabetes](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/diabetes/diabetes.csv.ipynb)
- [energy](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/energy/energy.csv.ipynb)
- [housing](https://github.com/ggupta2005/understanding-datasets/blob/master/datasets/regression/housing/housing.csv.ipynb)

