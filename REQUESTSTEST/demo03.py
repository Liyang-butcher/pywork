import pandas as pd #给pandas取别名pd
data = pd.read_excel('data.xlsx')
print(data.values[0])