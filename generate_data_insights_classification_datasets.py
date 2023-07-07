from rai_test_utils.datasets.tabular import (
    create_adult_census_data,
    create_cancer_data,
    create_iris_data,
    create_simple_titanic_data,
    create_wine_data,
)
import subprocess
import pandas as pd
import os


def generate_insights_classification_datasets():
    dataset_to_function_dict = {
        "iris": create_iris_data,
        "cancer": create_cancer_data,
        "wine": create_wine_data,
        "titanic": create_simple_titanic_data,
        "adult": create_adult_census_data,
    }

    for dataset_name in dataset_to_function_dict:
        dataset = dataset_to_function_dict[dataset_name]
        if dataset_name == "adult":
            X_train, _, y_train, _, _ = dataset()
            feature_names = list(X_train.columns)
        else:
            X_train, _, y_train, _, feature_names, _ = dataset()
        if not isinstance(X_train, pd.DataFrame):
            X_train = pd.DataFrame(data=X_train, columns=feature_names)

        X_train["target"] = y_train

        parent_directory = "datasets/" + "classification/" + dataset_name + "/"
        if not os.path.exists(parent_directory):
            os.makedirs(parent_directory)
        csv_file_name = parent_directory + dataset_name + ".csv"
        X_train.to_csv(csv_file_name, index=False)

        command = "data_understand -f {0} -t target -p -j".format(csv_file_name)

        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        print(result)
        assert result.returncode == 0


if __name__ == "__main__":
    generate_insights_classification_datasets()
