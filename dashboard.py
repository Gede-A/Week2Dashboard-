import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
}

df = pd.DataFrame(data)

# Streamlit app
st.title('Sample Data Visualization')

# Display the dataframe
st.write("### Data Table")
st.dataframe(df)

# Plot a bar chart
st.write("### Bar Chart")
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'])
ax.set_xlabel('Category')
ax.set_ylabel('Values')
st.pyplot(fig)

# Plot a line chart
st.write("### Line Chart")
st.line_chart(df.set_index('Category'))
