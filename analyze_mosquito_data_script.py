import pandas as pd
import analyze_mosquito_data_lib as mosquito_lib

filename = "A1_mosquito_data.csv"

data = pd.read_csv(filename)
# read the data

data["temperature"] = mosquito_lib.fahr_to_celsius(data["temperature"])

parameters = mosquito_lib.analyze(data)

# save parameters to file
parameters.to_csv("parameters.csv")

