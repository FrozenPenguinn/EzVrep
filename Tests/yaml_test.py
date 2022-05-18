"""
UNFINISHED!!! Featuring out a way to save DH matrix in yaml file so that humans can read directly
"""

import yaml
import numpy as np


dh = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
dh_yaml = yaml.safe_load(dh)
print(dh)


def write_yaml(filepath: str):
    with open(filepath, "w") as f:
        yaml.dump(dh_yaml, f)


if __name__ == "__main__":
    write_yaml("../Models/DH/UR5.yaml")
