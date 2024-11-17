import os
import pandas as pd
import matplotlib.pyplot as plt
import io
import numpy as np

class Services:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        if os.path.exists(self.file_path):
            return pd.read_json(self.file_path)
        return pd.DataFrame()

    def save_data(self):
        self.data.to_json(self.file_path, index=False)

    def merge_data(self, new_data):
        if not self.data.empty:
            self.data = pd.concat([self.data, new_data], ignore_index=True)
        else:
            self.data = new_data
        self.save_data()
