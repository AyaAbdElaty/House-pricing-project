
import pandas as pd
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="House Pricing")
html_title = """<h1 style="color:white;text-align:center;"> House Pricing </h1>"""

st.markdown(html_title, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("https://img.freepik.com/free-vector/hand-drawn-rising-house-prices-illustration_23-2150801646.jpg?semt=ais_items_boosted&w=740")

df = pd.read_csv(r"D:\Epsilon\Pandas & numpy\Mid Project\Epsilon\House_Pricing_Cleaned_1.csv", index_col=0)


st.dataframe(df.head(10))

page = st.sidebar.radio('Pages', ['Univariate Analysis','Bivariate Analysis', 'MultiVariate Analysis'])
   

if page == 'Univariate Analysis':

    st.title('Univariate Analysis')

    for col in df.columns:

        st.plotly_chart(px.histogram(data_frame= df, x= col, title= col))
elif page == 'Bivariate Analysis':
    st.title("Bivariate analysis")
    st.header("The average price for each location")

    df1 = df.groupby("location")["Amount(in rupees)"].mean().sort_values(ascending= False)
    st.plotly_chart(px.bar(data_frame=df1, color_discrete_sequence=["blue"] ))

    st.header("The effect of Furnishing on Price")
    df2 = df.groupby("Furnishing")["Amount(in rupees)"].median().sort_values()
    st.plotly_chart(px.bar(df2, color_discrete_sequence=["blue"]))

    st.header("The relation between ownership and Price")
    
    st.markdown("###### Freehold: means complete ownership of a property and the land it's on, with no time limit")
    st.markdown("###### Leasehold  means temporary ownership for a fixed period under a lease")
    st.markdown("###### Cooperative society Housing co-ops where members collectively own and manage residential properties.")
    st.markdown("###### A Power of Attorney (POA) is a legal document that authorizes someone to act on your behalf in financial, property, or health matters.")
    df3 = df.groupby("Ownership")["Amount(in rupees)"].count().sort_values()
    st.plotly_chart(px.bar(df3, color_discrete_sequence= ["blue"]))

    st.header("The relation between Transaction and Price")
    df4 = df.groupby("Transaction")["Amount(in rupees)"].median().sort_values()
    st.plotly_chart(px.bar(df4,color_discrete_sequence=["blue"]))

    st.header("The relation between facing and price")
    df5 = df.groupby("facing")["Amount(in rupees)"].median().sort_values()
    st.plotly_chart(px.bar(df5, color_discrete_sequence=["blue"]))

    st.header("")
    
    st.header("The effect of area on Price")
    fig, ax = plt.subplots()
    sns.lineplot(x = "Carpet Area", y = "Amount(in rupees)", data = df, ax = ax)
    st.pyplot(fig)

    st.header("The effect of no. of balcony on price")
    fig1, ax1 = plt.subplots()
    sns.lineplot(x = "Balcony", y = "Amount(in rupees)", data = df, ax = ax1)
    st.pyplot(fig1)

    st.header("Does the floor number affect price?")
    fig2, ax2 = plt.subplots()
    sns.lineplot(x = "Floor No", y = "Amount(in rupees)", data = df)
    st.pyplot(fig2)

    


elif page == 'MultiVariate Analysis':

    Price_of_area_of_eachLocation = (df.groupby(["Carpet Area", 'location'])['Amount(in rupees)'].mean().round(4) * 100).reset_index()
    st.plotly_chart(px.bar(data_frame= Price_of_area_of_eachLocation, x= 'Carpet Area', y= 'Amount(in rupees)', text_auto= True, color= 'location',
        title= '',
        labels= {'actual_productivity' : 'Average Productivity'}, barmode= 'group',
        color_discrete_sequence= ['red']))
