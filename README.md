# understanding-datasets
Repository to publish notebooks and PDF files for understanding different aspects of datasets like distributions, feature correlations and imbalances. The notebooks and PDF files have been generated using the open source project [data.understand](https://github.com/ggupta2005/data.understand).

The generate the PDF reports and the notebooks you need install [data-understand](https://pypi.org/project/data-understand/) and [rai-test-utils](https://pypi.org/project/rai-test-utils/).

```
pip install data-understand
pip install rai-test-utils
```

Once the installation of the above two packages in complete, you can then run the python code in the files `generate_data_insights_classification_datasets.py` and `generate_data_insights_regression_datasets.py`

```
python generate_data_insights_classification_datasets.py
python generate_data_insights_regression_datasets.py
```

This should generate the PDF reports and jupyter notebooks in the corresponding directories.
