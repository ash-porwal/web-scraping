# Going to webscrape table from this https://www.worldometers.info/world-population/
import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.worldometers.info/world-population/"
res = requests.get(url=url)
soup = BeautifulSoup(res.text, "lxml")

# On analysing I found this tag contains table info - <table class="table table-striped table-bordered table-hover table-condensed table-list">
table_info = soup.find("table", class_ = "table table-striped table-bordered table-hover table-condensed table-list")
# print(table_info)

# As we want to fetch table, so it must contains headers as well
# so, first thing we want from table data is to get headers
cols_tags = table_info.find_all("th")
all_headers = []
for each_tag in cols_tags:
    temp_string = each_tag.text
    all_headers.append(temp_string.strip())

# creating dataframe from above headers, 
# and setting those headers as column names
df = pd.DataFrame(columns = all_headers)
print(df)

# Getting Rows from website
final_each_row = []
rows_info = table_info.find_all("tr")
for each_tag in rows_info:
    # as data exists under td tag, so we need to find all td one more time
    row_data = each_tag.find_all("td")
    print(row_data)
    print()
    data_each_row = []
    for each_val in row_data:
        data_each_row.append(each_val.text)
    final_each_row.append(data_each_row)
        
# print(final_each_row)

# Appending each list as a row and setting columns
df = pd.DataFrame(final_each_row, columns = all_headers)
print(df.dropna()) # Dropping None row


# If you dont want above way, then below is using .loc method to append
# for each_list in final_each_row:
#     if len(each_list) != 0:
#         df.loc[len(df)] = each_list
# print()
# print(df)
