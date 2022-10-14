import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

tvshow_data = pandas.read_csv("tv_shows.csv")