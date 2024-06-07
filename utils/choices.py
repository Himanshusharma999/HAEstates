import os
import pandas as pd

from HAEstates import app

DATASET_PATH = os.path.join(app.root_path, 'dataset', 'real_estate_data_chicago.csv')


def get_label_name(string):
    return string.replace("_", " ").capitalize()


class ModelChoices:
    def __init__(self, choices_list):
        for item in choices_list:
            setattr(self, item.lower(), get_label_name(item))

    def choices(self):
        return [(k, v) for k, v in self.__dict__.items()]

    def values(self):
        return [v for v in self.__dict__.keys()]

    def labels(self):
        return [l for l in self.__dict__.values()]


df = pd.read_csv(DATASET_PATH, sep=',')

PropertyTypeChoices = ModelChoices([str(choice) for choice in df.type.unique()])
ProperyBedsChoices = ModelChoices([str(choice) for choice in df.beds.unique()])
PropertyBathsChoices = ModelChoices([str(choice) for choice in df.baths.unique()])
PropertyStoriesChoices = ModelChoices([str(choice) for choice in df.stories.unique()])

UserTypeChoices = ModelChoices(['Farmer', 'Customer'])

if __name__ == '__main__':
    print(df.type.unique())
    print(PropertyTypeChoices.choices())
