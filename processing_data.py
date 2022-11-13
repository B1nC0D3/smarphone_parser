import pandas as pd
path_to_json = r'smartphone_parser/scraped_data.json'

pandas_data = pd.read_json(path_or_buf=path_to_json)
result = pandas_data.groupby('version').nunique().sort_values(by='link', ascending=False)

print(result.to_string())
