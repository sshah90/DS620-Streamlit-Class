import streamlit as st

# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

from datetime import time,datetime,date

st.set_page_config(
    page_title="DS-Streamlit-Class", page_icon=":sunglasses:",
)

def data_display():
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

    "Display an interactive Plotly chart using `st.plotly_chart`"

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

def app():
    st.title("Uber pickups in NYC")

    DATE_COLUMN = "date/time"
    DATA_URL = (
        "https://s3-us-west-2.amazonaws.com/"
        "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
    )

    @st.cache
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis="columns", inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    data_load_state = st.text("Loading data...")
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache)")

    if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)

    st.subheader("Number of pickups by hour")
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)

    # Some number in the range 0-23
    hour_to_filter = st.slider("hour", 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader("Map of all pickups at %s:00" % hour_to_filter)
    st.map(filtered_data)


def user_input():
    "# In this section we will try to explore ways to interarate with users"

    # Add interactivity with widgets
    "Checkbox with `st.checkbox` command"
    s = st.checkbox("Show dataframe")

    if s:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        chart_data

    # Use a selectbox with options
    "Display a select widget with `st.selectbox`"

    # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        
    option = st.selectbox("Which number do you like best?", ["DS-610","DS-620","DS-640"])

    "You selected: ", option

    # second_option = st.selectbox("Which number do you like best?", chart_data["a"])

    # "You selected: ", second_option

    "Display a multiselect widget with `st.multiselect`"

    options = st.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
    st.write('You selected:', options)

    "Display a radio button widget with `st.radio`"

    genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    else:
        st.write("You didn't select comedy.")


    "Display a slider widget with `st.slider`. This supports int, float, date, time, and datetime types."
    age = st.slider('How old are you?', 0, 130, 10,10,format="%d days")
    st.write("I'm ", age, 'years old')

    "Time slider example"
    appointment = st.slider("Schedule your appointment:",value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    "Date slider example"
    start_time = st.slider("When do you start?",datetime(2010, 1, 1, 0, 0),datetime(2020, 1, 1, 9, 30),value=datetime(2020, 1, 1, 9, 30),format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)

    "Display a slider widget to select items from a list using `st.select_slider`"
    color = st.select_slider('Select a color of the rainbow',options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('My favorite color is', color)

    "Display a single-line text input widget using `st.text_input`"
    title = st.text_input('Movie title', 'Godzilla vs Kong')
    st.write('The current movie title is', title)

    "Display a multi-line text input widget using `st.text_area`"
    txt = st.text_area('Text to analyze',"")
    st.write('Sentiment:', txt)

    "Display a button widget with `st.button`, returns bool"
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')

    "Display a date input widget with `st.date_input`"
    d = st.date_input("When's your birthday", date(2019, 7, 6))
    st.write("Your birthday is:", d)

    """
    ## **Explore following user input functionality our own**
    - number_input
    - time_input
    - file_uploader
    - color_picker
    """

# let's add sidebar so that we can layout our app
option = st.sidebar.selectbox(
    "Which Level would you like to choose?",
    ["Display your data", "User Inputs", "App"],
)

st.sidebar.markdown(f"You selected: {option}")

if option == "Display your data":
    data_display()
elif option == "App":
    app()
elif option == "User Inputs":
    user_input()
