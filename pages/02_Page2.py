import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import altair as alt

imdb = pd.read_csv('imdb_top250_movies.csv')
imdb1 = imdb.loc[:,['Title','Year','Runtime','Genre','Director','imdbRating']].copy()

chType = st.selectbox(
  'Choose Chart Type',
  ('Bar plot','Box plot','Donut Chart','Line chart'))


if chType == 'Bar plot':  
  barChart = alt.Chart(imdb1).mark_bar(color='grey').encode(alt.X('Year'),alt.Y('imdbRating', scale=alt.Scale(domain=[8,9.5])),tooltip = ['Title','Year','Runtime','Genre','imdbRating'])
  meanLine = alt.Chart(imdb1).mark_rule(color='red').encode(y='mean(imdbRating)')
  st.altair_chart((barChart + meanLine).properties(width=700).interactive())

elif chType == 'Box plot':
  st.altair_chart(alt.Chart(imdb1).mark_boxplot(median={"color": "red"}).encode(
    alt.Y('imdbRating', scale=alt.Scale(domain=[7.5,9.5]))).properties(width=80,height=200).interactive())

elif chType == 'Donut Chart':
  st.altair_chart(alt.Chart(imdb1).mark_arc(innerRadius=50).encode(
     theta = alt.Theta(field='imdbRating'),
     color = alt.Color('imdbRating', scale=alt.Scale(scheme='greenblue')),
     tooltip = ['Title','Year','Runtime','Genre','imdbRating']))

elif chType == 'Line chart':
  st.altair_chart(alt.Chart(imdb1).mark_line(point=alt.OverlayMarkDef(color="green")).encode(
    alt.X('Year'),
    alt.Y('imdbRating',scale=alt.Scale(domain=[8,9.5])),
    tooltip = ['Title','Year','Runtime','Genre','imdbRating']).properties(width=1000,height=250).interactive())


if st.button('show Scatter plot with filled circles'):
  st.altair_chart(alt.Chart(imdb1).mark_circle().encode(
     alt.X('Title'),
     alt.Y('Year', scale=alt.Scale(domain=[1921,2017])),
     size='imdbRating:N',
     color = alt.Color('imdbRating', scale=alt.Scale(scheme='goldred')),
     tooltip = ['Title','Year','Runtime','Genre','imdbRating']).properties(
    width=5000,height=300).interactive())