import pandas as pd
from rai_test_utils.datasets.tabular import (
    create_diabetes_data,
    create_energy_data,
    create_housing_data,
)
import subprocess
import os


def generate_insights_regression_datasets():
    dataset_to_function_dict = {
        "diabetes": create_diabetes_data,
        "housing": create_housing_data,
        "energy": create_energy_data,
    }

    for dataset_name in dataset_to_function_dict:
        dataset = dataset_to_function_dict[dataset_name]
        X_train, X_test, y_train, y_test, feature_names = dataset()
        if not isinstance(X_train, pd.DataFrame):
            X_train = pd.DataFrame(data=X_train, columns=feature_names)

        X_train["target"] = y_train

        parent_directory = "datasets/" + "regression/" + dataset_name + "/"
        if not os.path.exists(parent_directory):
            os.makedirs(parent_directory)
        csv_file_name = parent_directory + dataset_name + ".csv"
        X_train.to_csv(csv_file_name, index=False)

        command = "data_understand -f {0} -t target -p -j".format(csv_file_name)

        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        print(result)
        assert result.returncode == 0


if __name__ == "__main__":
    generate_insights_regression_datasets()
