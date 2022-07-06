import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as plx
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import altair as alt
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import graphviz as graphviz

st.set_page_config(page_title="Tobibui1904",layout="wide")
st.markdown("<h1 style='text-align: center; color: lightblue;'>Inflation's effect on Vietnamese economy from 1996 to 2020 annually</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; color: red;'>Inflation</h1>", unsafe_allow_html=True)
st.subheader("Definition:")
st.write("Inflation is the decline of purchasing power of a given currency over time. A quantitative estimate of the rate at which the decline in purchasing power occurs can be reflected in the increase of an average price level of a basket of selected goods and services in an economy over some period of time. The rise in prices, which is often expressed as a percentage, means that a unit of currency effectively buys less than it did in prior periods. Inflation can be contrasted with deflation, which occurs when the purchasing power of money increases and prices decline.")

#Inflation table
df1=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Inflation.csv")
df1.rename(columns = {"FPCPITOTLZGVNM":'Inflation'}, inplace = True)

#Real interest rate (%)
df6=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Real interest rate (%).csv")
df6.style.format({
    'CPI change rate': '{:,.2%}'.format,
})


#Inflation graph
lines = (
    alt.Chart(df1)
    .mark_line()
    .encode(x="DATE", y="Inflation")
)

line_Inflation = pd.DataFrame({
    'DATE': [1996, 2020],
    'Inflation': [0, 0],
})

Inflation_plot = alt.Chart(line_Inflation).mark_line(color= 'red').encode(
    x= 'DATE',
    y= 'Inflation'
)

Inflation=lines+Inflation_plot
st.altair_chart(Inflation)

#Inflation comment
st.write("From the chart, we can see there's no stable trend in inflation as it's very chaotic and changing every year. As we noticed, there are 2 main peaks that we should notice: the Asian Financial Crisis impact from 1998 to 2001 and the Great Recession from 2008-2009. The Asian Financial Crisis was so intense that the inflation saw a deep decrease along with the negative inflation rate, which was very terrible for economy. In other word, we saw a deflation making price fell, leading to more debt as people bought too much items due to low prices. Therefore, the money and credit supply would be decreased leading to a bad economic situation of low creditability. ")

#Real interest rate analysis
st.markdown("<h1 style='text-align: left; color: red;'>Real Interest rate</h1>", unsafe_allow_html=True)
st.subheader("Definition:")
st.write("A real interest rate is an interest rate that has been adjusted to remove the effects of inflation. Once adjusted, it reflects the real cost of funds to a borrower and the real yield to a lender or to an investor.")
st.write("A real interest rate reflects the rate of time preference for current goods over future goods. For an investment, a real interest rate is calculated as the difference between the nominal interest rate and the inflation rate:")
st.latex(r'''
    r -  i
    ''')

#Real Interest rate graph
Real_interest_rate=alt.Chart(df6).mark_line().encode(
    x='DATE',
    y='Real interest rate (%)'
)

line_Real_interest_rate = pd.DataFrame({
    'DATE': [1996, 2020],
    'Real interest rate (%)': [0, 0],
})
Real_interest_rate_plot = alt.Chart(line_Real_interest_rate).mark_line(color= 'red').encode(
    x= 'DATE',
    y= 'Real interest rate (%)'
)

Interest_rate=Real_interest_rate+Real_interest_rate_plot
st.altair_chart(Interest_rate)

#Real interest rate comment
st.write("From the graph, we can see that the real interest rate fluctuated during the 1996-2020 period. There's no durable trend because real interest rate is heavily dependant on the consumers as well as the inflation. Real interest rate reflects the consumers'behavior of holding or spending money during a particular period. In this case, there were 3 years that witnessed a negative real interest rate: 2005,2008 and 2011. In those 3 years, the consumers were likely to save up their money in bank accounts or even their home because of some downside financial deflation, including the great recession. In order to make economic activity become more active, Vietnamese government set the real interest rate to be negative so that the banks or whoever lends the money to consumers to pay fees for the loaner. This may be weird but it's considered a desperate method of expansionary monetary policy during a deflation to raise the economy up. Consumers may expect their money to be worth more tomorrow than today during these periods. When this happens, the economy can experience a sharp decline in demand, causing prices to plummet even lower. This had to be stopped for the sacred of Vietnamese GDP development.")
