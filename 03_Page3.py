import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt


imdb = pd.read_csv('imdb_top250_movies.csv')
imdb1 = imdb.loc[:,['Title','Year','Released','Runtime','Genre','Director','imdbRating']].copy()

# slider
rat_slider = st.slider('Choose a Rating',8.0,9.3)

# radio button
ptype = st.radio("Select your plot chart", ['Scatter plot with filled squares','Pie chart'])

# Scatter plot with filled squares
if ptype == 'Scatter plot with filled squares':
  st.altair_chart(alt.Chart(imdb1[imdb1['imdbRating']==rat_slider]).mark_square().encode(
      alt.X('Year', scale=alt.Scale(domain=[1920,2017])),
      alt.Y('imdbRating', bin=True),
      tooltip = ['Title','Year','Runtime','Genre','imdbRating']).interactive())

# Pie chart
elif ptype == 'Pie chart':
  st.altair_chart(alt.Chart(imdb1[imdb1['imdbRating']==rat_slider]).mark_arc().encode(
    theta = alt.Theta(field='Year'),
    color = alt.Color('Title', scale=alt.Scale(scheme='greenblue')),
    tooltip = ['Title','Year','Runtime','Genre','imdbRating']))


# checkbox
ch_table = st.checkbox('Show Table with imdb details')

# if checkbox is cliked then display the dataframe releated to imdbRating selected by slider
if ch_table:
  st.dataframe(imdb1[imdb1['imdbRating']==rat_slider])
