import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

netflix_data = pandas.read_csv("netflixData.csv")