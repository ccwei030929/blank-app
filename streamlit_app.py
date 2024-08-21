# import streamlit as st

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import pandas as pd

# Function to read and process the CSV file
def process_csv_data():
    df = pd.read_csv('table1.csv')
    table2 = {
        'Alpha': int(df.loc[4, 'A']) + int(df.loc[19, 'A']),
        'Beta': float(df.loc[14, 'A']) / float(df.loc[6, 'A']),
        'Charlie': float(df.loc[12, 'A']) * float(df.loc[11, 'A'])
    }
    return df, table2

# Display Table 1
df, table2 = process_csv_data()
st.title('Table 1')
st.table(df)

# Display Table 2
st.title('Table 2')
st.table(table2)
