import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

"# In this section we will try to explore ways to display our data"

# Let’s add a title to test things out
st.title("My Cool Streamlit App!!!")

# Let's write something
# write any text
st.write("Here's our first attempt at using data to create a table:")
# write dataframes
st.write(
    pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
)
# write JSON
st.write({"Name": "John", "Country": "USA"})

# Emojis are love!
st.write("Display some cool emojis :sunglasses:")

# st.write accepts chart objects too!
df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
# st.write(c)

# you can also use
st.text("you can also use st.text or st.markdown as well")

# let me showcase some Magic!
"""
# My Cool Streamlit App!!!
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
# df

# you can also use st.dataframe and st.table
"Display a df with `st.dataframe(df)` and `st.table(df)`"
st.dataframe(df)
st.table(df)

# let's display some charts
"let's display charts"
chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
# line_chart
"Display a line chart figure with `st.line_chart`"
st.line_chart(chart_data)
# area_chart
"Display a area chart figure with `st.area_chart`"
st.area_chart(chart_data)

# bar_chart
"Display a bar chart figure with `st.bar_chart`"
st.bar_chart(chart_data)

# let's draw Map chart
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
"Display a map figure with `st.map`"
st.map(map_data)

"Display a matplotlib.pyplot figure with `st.pyplot`"
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)

"Display a chart using the Altair library with `st.altair_chart`"
st.altair_chart(c, use_container_width=True)

"Display an interactive Plotly chart."

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ["Group 1", "Group 2", "Group 3"]

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.25, 0.5])

st.plotly_chart(fig, use_container_width=True)

"""
## **Explore following user data disply functionality our own**
- header
- subheader
- markdown
- latex
- image
- audio
- video
"""
