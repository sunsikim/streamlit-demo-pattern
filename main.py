"""
Note that docstring is ignored indeed.
"""

import streamlit as st
import pandas as pd
import numpy as np

"""
# My First Streamlit Application

This is hello world example of Streamlit application. 
This example attempts to try various options of Streamlit as many as possible for future use.
Not only it enables English alphabets to be displayed, but it also allows other languages such as 한국어.
Cool thing about this framework is its native support on *markdown* and $latex$ syntax.
Also, as mentioned [here](https://docs.streamlit.io/library/api-reference/write-magic/magic#how-magic-works), 
this engine is smart enough to ignore docstring that appears as first text block of a python module.

## 1. How to Display Contents

Explicit way would be using `st.write` or many other case-specific methods listed in the API reference.
For example, to display dataframe defined as below;
```python
num_columns = 10
df_example = pd.DataFrame(
    data=np.random.random((5, num_columns)),
    columns=[f"col_{index}" for index in range(num_columns)]
)
```
user can use `st.write` or `st.dataframe` method. 
Main difference between two is that latter case-specific method has more options to configure than former swiss army knife method.
"""

num_columns = 10
df_example = pd.DataFrame(
    data=np.random.random((5, num_columns)),
    columns=[f"col_{index}" for index in range(num_columns)]
)
st.dataframe(df_example)

"""
However, it can be somewhat hassle to wrap every content with such explicit methods, and moreover, it can be redundant.
Streamlit collects defined but unassigned values from the Python module it executes, and it parses them rinto appropriate format.
This is called *Streamlit magic command*, according to the documentation.

### magic command for text, explicit method for other sources

As introduced in the title paragraph, Streamlit is good at parsing markdown syntax from raw text.
Moreover, markdown syntax is rich enough when purpose of the application is to demonstrate data and corresponding AI/ML data product.
Since I feel comfortable in using many different components of markdown, I decided to make use of magic command in markdown syntax every time I need to display long text contents.
Then overall text format comes to resemble friendly R markdown format(in my personal view as Statistics major :-)) which separates text component format from code component format.
For more information on other components which can be rendered and displayed on the application, check out various [element pages](https://docs.streamlit.io/library/api-reference) in API reference.

## 2. How to Interact with Audiences

There are some avaiable options when attempting to make interactive application that reacts to user input. 
How it reacts to real-time input was simple: **it just reruns whole script with arrived user input**.
You can see the dataframe displayed above which was generated from random numbers is regenerated everytime you change the status of checkbox below.
"""

if st.checkbox("Show `df_example` defined above"):
    st.dataframe(df_example)

"""
This is true for any type of interactive widgets. User can utilize linear slider as an input UI, and page refreshes everytime value which linear slide represents changes.
"""

frequency = st.slider(
    label="frequency",
    min_value=0.1,
    max_value=3.0,
    value=1.0,
    step=0.1,
    # on_change=render_sin_graph
)
x = np.linspace(0, 2, 1000) * np.pi
y = np.sin(frequency * x)
st.caption(f"$y=\sin(ax), 0\leq x\leq 2\pi$ where $a=${frequency}")
st.line_chart(data=pd.DataFrame({"x": x, f"y": y}), x="x", y="y" )

"""
For more available types of widgets, check out [input widgets section](https://docs.streamlit.io/library/api-reference/widgets) of API reference page.

## 3. How to Customize Layout

Streamlit provides options to customize page layout such as utilizing sidebar space and separating single screen into multiple columns. 
Name of API for each functionality is `st.sidebar`, `st.columns` respectively, and their usage is not so different from the usage of single page explained so far.
"""

user_name = st.sidebar.text_input(
    label="name",
    max_chars=20,
    type="default",
    help="Place where you enter your name",
    placeholder="Enter your name"
)
user_password = st.sidebar.text_input(
    label="password",
    type="password",
    help="Place where you enter your password",
    placeholder="Enter your password"
)
"""
For example, code for making text input component on sidebar space is identical to API used for making it on main page.
It just requires component to be defined in different `st.sidebar` namespace as below.

```python
user_name = st.sidebar.text_input(
    label="name",
    max_chars=20,
    type="default",
    help="Place where you enter your name",
    placeholder="Enter your name"
)
```

Also, it provides to option to customize content layout such as selectively hiding the content and displaying different contents as a multiple different tabs in a single container.
Name of each functionality is `st.expander`, `st.tabs` respectively. 
For more detailed options of each API, check documentation in [layouts and containers](https://docs.streamlit.io/library/api-reference/layout) section.
"""

with st.expander(label="Show `df_example` defined above", expanded=False):
    """
    Unlike displaying dataframe with checkbox as above, this expander does not rerun whole script as its expanded status is changed by user.
    """
    st.dataframe(df_example)
