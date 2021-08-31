import pandas as pd
import numpy as np

from numpy.random import randn

df = pd.DataFrame(randn(5, 3), ['A', 'B', 'C', 'D', 'E'], ['X', 'Y', 'Z'])

print(df)
