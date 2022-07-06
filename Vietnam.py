import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as plx
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import altair as alt
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from vega_datasets import data

st.set_page_config(page_title="Tobibui1904",layout="wide")
header=st.container()
tables=st.container()
gdp=st.container()
GDP_element=st.container()
contact_form=st.container()

with header:
    st.markdown("<h1 style='text-align: center; color: lightblue;'>Vietnam's economy from 1996 to 2020 annually</h1>", unsafe_allow_html=True)
    st.caption("<h1 style='text-align: center;'>By Tobi Bui</h1>",unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: left; color: red;'>Introduction about Vietnam</h1>", unsafe_allow_html=True)
    st.markdown("""
    Vietnam, officially the Socialist Republic of Vietnam, is a country in Southeast Asia. Located at the eastern edge of mainland Southeast Asia, it covers 311,699 square kilometres (120,348 sq mi). With a population of over 96 million, it is the world's fifteenth-most populous country. Vietnam borders China to the north, Laos and Cambodia to the west, and shares maritime borders with Thailand through the Gulf of Thailand, and the Philippines, Indonesia, and Malaysia through the South China Sea. Its capital is Hanoi and its largest city is Ho Chi Minh City.

A developing country with a lower-middle-income economy, Vietnam is nevertheless one of the fastest growing economies of the 21st century, and its total GDP is predicted to possibly rival those of several developed nations by 2050. Contemporary issues in Vietnam include corruption, censorship and a poor human rights record; the country ranks among the lowest in international measurements of civil liberties, press freedoms, and freedom of religion and ethnic minorities. It is part of international and intergovernmental institutions including the United Nations, the ASEAN, the APEC, the CPTPP, the Non-Aligned Movement, the OIF, and the WTO. It has assumed a seat on the United Nations Security Council twice.
    """
    )
    st.write("---")

#GDP table
df=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\GDP.csv")
df.rename(columns = {"MKTGDPVNA646NWDB":'GDP'}, inplace = True)

#Inflation table
df1=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Inflation.csv")
df1.rename(columns = {"FPCPITOTLZGVNM":'Inflation'}, inplace = True)

#CPI table
df2=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\CPI.csv")
df2.rename(columns = {"VNMPCPIPCPPPT":'CPI change rate'}, inplace = True)
df2.style.format({
    'CPI change rate': '{:,.2%}'.format,
})

# Government spending table
df3=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Government spending.csv")

#Imports of goods and services
df4=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Imports of goods and services.csv")

#Exports of goods, services and primary income (BoP, current US$)
df5=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Exports of goods, services and primary income (BoP, current US$).csv")

#Real interest rate (%)
df6=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Real interest rate (%).csv")
df6.style.format({
    'CPI change rate': '{:,.2%}'.format,
})

#Research and development expenditure (% of GDP)
df7=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Research and development expenditure (% of GDP).csv")

#Consumption table
df8=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Consumption.csv")

#Summary of GDP, Consumption, Government Spending, and Net Exports
df9=pd.read_csv(r"C:\Users\Admin\Vietnamese economy\Summary.csv")

with tables:
    #Summary table of GDP; Government spending; Imports of goods and services; Exports of goods, services
    cols_to_use = df1.columns.difference(df.columns)
    dfNew = pd.merge(df, df1[cols_to_use], left_index=True, right_index=True, how='outer')

    cols_to_use1 = df2.columns.difference(dfNew.columns)
    dfNew1 = pd.merge(dfNew, df2[cols_to_use1], left_index=True, right_index=True, how='outer')

    cols_to_use2 = df3.columns.difference(dfNew1.columns)
    dfNew2 = pd.merge(dfNew1, df3[cols_to_use2], left_index=True, right_index=True, how='outer')

    cols_to_use3 = df4.columns.difference(dfNew2.columns)
    dfNew3 = pd.merge(dfNew2, df4[cols_to_use3], left_index=True, right_index=True, how='outer')

    cols_to_use4 = df5.columns.difference(dfNew3.columns)
    dfNew4 = pd.merge(dfNew3, df5[cols_to_use4], left_index=True, right_index=True, how='outer')

    cols_to_use5 = df6.columns.difference(dfNew4.columns)
    dfNew5 = pd.merge(dfNew4, df6[cols_to_use5], left_index=True, right_index=True, how='outer')

    cols_to_use6 = df7.columns.difference(dfNew5.columns)
    dfNew6 = pd.merge(dfNew5, df7[cols_to_use6], left_index=True, right_index=True, how='outer')
    
    cols_to_use7 = df8.columns.difference(dfNew6.columns)
    dfNew7 = pd.merge(dfNew6, df8[cols_to_use7], left_index=True, right_index=True, how='outer')

    st.markdown("<h1 style='text-align: left; color: red;'>Summary table</h1>", unsafe_allow_html=True)
    st.write('This is a table summarizing all data of GDP, Inflation, CPI Change Rate, Gross National Expenditure, Imports Of Goods, Exports Of Goods, Real Interest Rate, Research And Development Expenditure')
    st.write(dfNew7)
    st.subheader('What this table can do:')
    st.write('1: Pin columns: left or right')
    st.write('2: Sort columns in any order: ascending or descending')
    st.write('3: Filters: select the columns you want to be displayed on the table')
    st.write('4: Pivot Modes: determine the value you want for the overview of the data')
    st.write("---")

with gdp:
    st.markdown("<h1 style='text-align: left; color: red;'>GDP's overview:</h1>", unsafe_allow_html=True)
    st.subheader('Definition')
    st.markdown("""
    Gross domestic product (GDP) is the total monetary or market value of all the finished goods and services produced within a country’s borders in a specific time period. As a broad measure of overall domestic production, it functions as a comprehensive scorecard of a given country’s economic health.
    """
    )
    st.subheader("GDP's development from 1996-2020:")
    #GDP graph
    GDP=alt.Chart(df).mark_area(
        color="lightblue",
        interpolate='step-after',
        line=True
    ).encode(
        x='DATE',
        y='GDP'
    )
    st.altair_chart(GDP, use_container_width=True)
    st.write("In general, Vietnam's GDP saw an increasing trend over the 1996-2020 period")
    st.write("According to the World Bank, Vietnam has been a development success story. Economic reforms since the launch of Đổi Mới in 1986, coupled with beneficial global trends, have helped propel Vietnam from being one of the world’s poorest nations to a middle-income economy in one generation.  ")
    st.write("Thanks to its solid foundations, the economy has proven resilient through different crises, the latest being COVID-19. Vietnam was one of only a few countries to post GDP growth in 2020 when the pandemic hit.")

    #GDP difference table
    v = np.diff(df['GDP'])
    v=v.tolist()
    list=[]
    for i in range(24):
        x=df['GDP'][i].tolist()
        y=(v[i]/x)*100
        list.append(y)

    GDP_difference = pd.DataFrame(list, columns=['Difference'],index=['1996-1997','1997-1998','1998-1999','1999-2000','2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020'])
    st.write("Let's take a look at GDP's development by years")
    st.dataframe(GDP_difference)
    st.write("From the table, we can see the Vietnamese GDP's greatest development was in the period between 2007-2008 with 28.0515% growth. Vice versa, its slowest period was in the period of 1997-1998 with only 1.3631% growth")
    
    #GDP review in 2007-2008
    st.write("Vietnam did a good job in sustaining the economy towards development in the Great Recession from 2007-2009, which affected the world economy, especiaaly the US. Additionally, in that period, Vietnam encounter continuous natural disaster, plauge. 2007-2008 was a tough period for Vietnam but we still managed to overcome it and found a way to increase our GDP in an unexpected way. We did it with the policy adjustment to control inflation as a top priority, stabalize macroeconomic, and ensure social security. That policy was called '8-group system solution': ")
    st.markdown("<p style='text-align: center;'>1: Control the money market</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>2: Using fiscal policy</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>3: Increase export, control import</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>4: Focus on manucfacturing</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>5: Guarantee people's life</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>6: Spread out about savings and consumption</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>7: Remove uncertainty from people's expectation</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>8: Applying tight monetary policy to sustain inflation</p>", unsafe_allow_html=True)
    st.write("")
    #GDP review in 1997-1998
    st.write("In contrast, 1997-1998 was a difficult time for the Vietnamese economy as we faced Asian economic crisis due to the following reasons: Weak macroeconomics and Investors drawing out money from the market. The crisis caused the money value to significantly decrease, stock market collapse. Some countries were heavily affected such as Indonesia, South Korea and Thailand but not Vietnam. We did a great job in developing the economy by decreasing excess of imports over exports, stabalizing prices, increasing agricultural and industrial products, consolidating National Defense, and expanding foreign economic relations. ")
    st.write("---")

with GDP_element:
    st.header("Elements of GDP:")
    st.subheader("GDP's formula is:")
    st.latex(r'''
    C + I + G + NX
    ''')
    st.subheader('Explanation:')
    st.write('C: Consumption')
    st.write('I: Investment')
    st.write('G: Government spending')
    st.write('NX: Net Export')

    #Consumption analysis
    st.markdown("<h1 style='text-align: left; color: red;'>Consumption</h1>", unsafe_allow_html=True)
    st.subheader("CPI")
    st.write("A consumer price index (CPI) is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. Changes in measured CPI track changes in prices over time.")

    #CPI graph
    CPI=alt.Chart(df2).mark_line(interpolate='step-after').encode(
        x='DATE',
        y='CPI change rate'
    )

    line_CPI = pd.DataFrame({
        'DATE': [1996, 2020],
        'CPI change rate': [0, 0],
    })
    CPI_plot = alt.Chart(line_CPI).mark_line(color= 'red').encode(
        x= 'DATE',
        y= 'CPI change rate'
    )

    CPI_change_rate=CPI+CPI_plot
    st.altair_chart(CPI_change_rate)

    #CPI comment
    st.write("From the graph, we can see people's spending changing significantly from year to year. They spent oftenly during the 2007-2008 period with a change of 19.89127206% while they spent least during the 1997-2000 period with all negative. This is the effect of the policies made in those 2 crisis periods in GDP's overview section. One is to stimulate the money market spending, while the others is to limit the spending. Through CPI, people tended to save money in banks during the 1997-2000 period due to the high cost of living, which often caused by high inflation, while they tended to spend a lot in the Great recession in 2007-2008 to stimulate the economic activities avoiding getting the zero lower bound interest rate.")
    st.write("In conclusion, CPI helps identify the consumer spending trend, which would help economists to adjust policies to sustain the economy, and increase GDP like the way Vietnam did. As a communist country, the government has the ultimate power to lead the economy in the way they want for the purpose of Government Spending. That's why they can guide consumer's spending towards the Government Spending, and control the economy so smooth like that.")

    #Consumption analysis
    st.subheader("Consumption in $")
    st.write("Consumption is an activity in which institutional units use up goods or services; consumption can be either intermediate or final. It is the use of goods and services for the satisfaction of individual or collective human needs or wants. Alternatively, a consumption of a good or service is one that is used (without further transformation in production) by households, non-profit institutions serving households (NPISHs) or government units for the direct satisfaction of individual needs or wants or the collective needs of members of the community.")

    left1,right1=st.columns(2)
    with left1:
        #Consumption chart
        Consumption=alt.Chart(df8).mark_line(
            point=alt.OverlayMarkDef(color="red")
        ).encode(
            x='DATE',
            y='Consumption'
        )
        st.altair_chart(Consumption)
    
    with right1:
        #GDP-Consumption percentage table
        list2=[]
        for i in range(25):
            c=df['GDP'][i].tolist()
            d=df8["Consumption"][i].tolist()
            e=(d/c)*100
            list2.append(e)

        GDP_Consumption_table = pd.DataFrame(list2, columns=['Percent'],index=['1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])
        GDP_Consumption_table.index.name="DATE"
        st.dataframe(GDP_Consumption_table)
        
    #Consumption comment
    st.write("From the chart, we can see that there's an increasing trend from 1996-2020, which is the same trend as the GDP. This makes Consumption as the largest components affecting the development of GDP, which can be seen through the table. Of the 4 components of GDP, we witness an increase trend without steeping down in Government Spending and Consumption, but there's still a little bit fluctuation in Net Exports. However, the GDP still increased due to the huge effect of Consumption development on GDP, which make a decrease in Net Exports nothing. The reason leading to this increasing consumption is that Vietnam's economy is well developed that we now have our own e-commerce website including Shoppe, Lazada as well as credit card convenient payment, more international brand entering Vietnamese market such as H&M, Zara, etc. From this, we can see Vietnam is a very high potential country to invest. ")
    
    #Government spending analysis
    st.markdown("<h1 style='text-align: left; color: red;'>Government spending</h1>", unsafe_allow_html=True)
    st.write("Government spending refers to money spent by the public sector on the acquisition of goods and provision of services such as education, healthcare, social protection, and defense. When the government acquires goods and services for current use to directly satisfy the individual or collective needs and requirements of the community, it is classified as government final consumption spending. When the government acquires goods and services for future use, it is classified as government investment. This includes public consumption and public investment, and transfer payments consisting of income transfers.")

    #Government spending graph
    base = alt.Chart(df3).encode(x='DATE:O')
    bar = base.mark_bar().encode(y='Government final spending')

    x = base.mark_line(color= 'red').encode(
        y= 'Government final spending'
    )

    Gross_National_Expenditure_plot=x+bar
    Gross_National_Expenditure_plot.properties(width=600)
    st.altair_chart(Gross_National_Expenditure_plot)

    #Government spending comment
    st.write("Overall, there is an increasing trend in Government spending, which intepret Vietnam's policy to improve public infrastructure. That money was used to supply goods and services that are not supplied by the private sector, such as defense, roads, and bridges; merit goods such as hospitals and schools, and welfare payments and benefits including unemployment and disability benefits; to achieve improvements in the supply-side of the macro-economy, such as spending on education and training to improve labor productivity, and provide subsidies to industries that may need financial support for either their operation or expansion. The private sector is not able to meet such financial requirements and, hence, the public sector plays a crucial part in lending necessary support. For example, transport infrastructure projects do not attract private finance unless the government provides expenditures for the industry. To help redistribute income and promote social welfare. ")

    st.subheader("Government spending on GDP:")

    #GDP-Government spending chart
    GDP_G=dfNew2.set_axis([i for i in range(1996,2021)], axis='index')
    GDP_G.drop(columns=['DATE',"Inflation","CPI change rate"], axis=1, inplace=True)
    st.line_chart(GDP_G)

    #Government spending on GDP comment
    st.write("From the chart, we can see that the difference between GDP and Governement spending keeps increasing, which means that the Government Spending doesn't have much effect on the acquisition of GDP. In this situation, the Fiscal Multiplier doesn't work with Vietnamese economy as the Government spending witnessed a very slight decrease but the GDP still increases. Therefore, this emphasizes that Government Spending doesn't seem relative too much to GDP, and we need to look at other elements like Consumption, Investment, and Net Export to determine the reasons for Vietnam's magnificant GDP development. ")

    #Government spending difference table
    a = np.diff(df3['Government final spending'])
    a=a.tolist()
    list1=[]
    for i in range(24):
        x=df['GDP'][i].tolist()
        y=(a[i]/x)*100
        list1.append(y)

    G_difference = pd.DataFrame(list1, columns=['Difference'],index=['1996-1997','1997-1998','1998-1999','1999-2000','2000-2001','2001-2002','2002-2003','2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020'])
    st.write("Let's take a look at Government spending's development by years")
    st.dataframe(data=G_difference)
    st.write("From the table, we can see there's no significant change in Government Spending, roughly 0 to 1%. Additionally, we can see there's a slight decrease in Government Spending but it was not so significant to care. In general, Vietnamese Government increases its spending from 1996-2020.")
    
    #Research and development expenditure on GDP analysis
    st.subheader("Research and Development on GDP")
    
    left,right=st.columns(2)
    with left:
        #Research percentage graph
        Research_plot=alt.Chart(df7).mark_bar().encode(
        x='Research and development expenditure (% of GDP):Q',
        y=alt.Y('DATE:N', sort='-x')
        )
        st.altair_chart(Research_plot)
    
    with right:
        #Research in $ graph
        brush = alt.selection(type='interval')
        Research_plot1=alt.Chart(df7).mark_point().encode(
            x='DATE',
            y='Research and development expenditure (% of GDP):Q',
            color=alt.condition(brush, ':O', alt.value('grey')),
        ).add_selection(brush)
        st.altair_chart(Research_plot1)
    
    #Research and development comment
    st.write("Research and development is a part of Government Spending that the Vietnamese Government used to invest in country's development of technology, applications. This budget varies from years to years, depending on the country's financial situation to directly took out from the GDP for researcher. We invested most during the 1996-1999 period. Vice versa, we invested least in 2008-2009 period. The two period were the same as the Asian Financial crisis and the Great Recession, but they impacted the research fund differently. We invested a lot in this section during the Asian financial crisis because that's our policy to self-develop to catch up other countries. Our GDP developed not fast enough or huge enough to invest in other components of GDP. Government spending was wisely used to create the concrete foundation of technology, and development for Vietnam to have enough power to invest more in other components. That's why in the Great recession when the inflation rate crashed the market, we have the ability to overcome it by not focusing on Research and Development. That's the difference of periods in pouring money for the Research and Development of the Government Spending. ")
    
    #Net export analysis
    st.markdown("<h1 style='text-align: left; color: red;'>Net Exports</h1>", unsafe_allow_html=True)
    st.write("Net exports are a measure of a nation's total trade. A nation that has positive net exports enjoys a trade surplus, while negative net exports mean the nation has a trade deficit. A nation's net exports are thus a component of its overall balance of trade.")
    st.write("Net Exports formula is")
    st.latex(r'''
    Exports - Imports
    ''')
    st.write("")

    col1,col2=st.columns(2)
    with col1:
        #Export graph
        Exports_plot=alt.Chart(df5).mark_area(
        line={'color':'lightblue'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='white', offset=0),
                alt.GradientStop(color='lightblue', offset=1)],
            x1=1,
            x2=1,
            y1=1,
            y2=0
        )
        ).encode(
            alt.X('DATE:O'),
            alt.Y('Exports of goods:Q')
        )
        st.altair_chart(Exports_plot)

    with col2:
        #Import graphs
        Imports_plot=alt.Chart(df4).transform_calculate(
            url='https://www.google.com/search?q=Việt Nam nhập khẩu' + alt.datum.Name
        ).mark_point().encode(
            x='DATE',
            y='Imports of goods:Q',
            href='url:N',
            tooltip=['Name:N', 'url:N']
        )
        st.altair_chart(Imports_plot)
    
    st.write("Overview: They have the same trend overall. We can see that there is an overall increasing trend in exports and exports, but there is a slight decrease in 2008-2009 period: $7,433,000,000. This is because of the Great Recession in the US. The US economy affected the world, which would make Vietnam's effort to export to the US and the world decreased. During the recession, prices increased due to the high inflation rate. This is caused by the stock market crashed, people tried to take the money out of the market, saved it for themselves by putting it in the bank. This maked the economic activities become slow, which is not good for a highly-consumed country like the US.")

    st.subheader("Net Exports on GDP")
    st.write("")
    
    #GDP-Net Export chart
    GDP_NX=dfNew4.set_axis([i for i in range(1996,2021)], axis='index')
    GDP_NX.drop(columns=['DATE',"Inflation","CPI change rate","Government final spending"], axis=1, inplace=True)
    st.area_chart(GDP_NX)
    
    #Net Export on GDP comment
    st.write("From 1996 to 2017, the GDP was still larger than both imports and exports, but from 2018 to 2020, it was smaller. Vietnam did an amazing job in expanding their export abilities with more diverse products including fruits, coffees, etc. Exports became so strong that it exceed the country's GDP, which is a good sign of our international relations to other countries. It is confirmed that Vietnamese products are good. Therefore, from 2017-2020, our Net Exports are positive, which contributes a lot to the GDP development. However, from 1996-2016, our Net Exports were still negative, which subtracted some amount of money from the GDP, but the GDP kept increasing. Currently, Vietnam succeed in protecting its own market with the policy called (logically enough) protectionism, uses barriers to keep out imports. These barriers include high tariffs—taxes or surcharges on imported goods—and strict rules about what products can be imported. That is the same principle we did with the fiscal policy during the Covid-19 recession. ")

    #Summarize components of GDP
    st.markdown("<h1 style='text-align: left; color: red;'>Summary</h1>", unsafe_allow_html=True)

    #Summary chart
    summary=alt.Chart(df9).mark_area().encode(
        x='DATE:T',
        y='Price:Q',
        color='Symbol:N',
        row=alt.Row('Symbol:N', sort=['GDP', 'Consumption', 'G', 'Imports','Exports'])
    ).properties(height=50, width=400)

    st.altair_chart(summary)

    #Summary comment
    st.write("From the chart, we can see the overall increasing trend in every components of GDP. Consumption increased mostly as it's the main component while Government Spending increased slowly, which didn't have much effect on Vietnam's GDP.")

with contact_form:
    st.write("---")
    st.markdown("<h1 style='text-align: left; color: red;'>Get in touch with me</h1>", unsafe_allow_html=True)
    st.write('##')
    contact= """
    <form action="https://formsubmit.co/buituannghia1904@gmail.com" method="POST">
    <input type ="hidden" name="_capcha" value="false">
    <input type="text" name="name" placeholder = "Your name" required>
    <input type="email" name="email" placeholder = "Your email" required>
    <textarea name= "message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    local_css(r"C:\Users\Admin\Vietnamese economy\style.css")
    
#side bar
with st.sidebar:
    selected = option_menu(
        menu_title="File used in the website",
        options=["FRED, WB Dataset"],
        icons=["clipboard-data"],
        menu_icon="cast",
        default_index=0, 
        styles={
                "container": {"padding": "0!important", "background-color": "#00000"},
                "icon": {"color": "black", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#00000",
                },
                "nav-link-selected": {"background-color": "lightblue"},
            },
    )
    if selected == 'FRED, WB Dataset':
        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')

        GDP_csv = convert_df(df)
        Inflation_csv=convert_df(df1)
        CPI_csv=convert_df(df2)
        Exports_csv=convert_df(df5)
        Import_csv=convert_df(df4)
        Gross_National_Expenditure_csv=convert_df(df3)
        Real_interest_rate_csv=convert_df(df6)
        research_expenditure_csv=convert_df(df7)
        summary_table=convert_df(dfNew6)
        st.download_button(
            label="GDP",
            data=GDP_csv,
            file_name='GDP.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Inflation",
            data=Inflation_csv,
            file_name='Inflation.csv',
            mime='text/csv',
        )

        st.download_button(
            label="CPI",
            data=CPI_csv,
            file_name='CPI.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Exports",
            data=Exports_csv,
            file_name='Exports.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Import",
            data=Import_csv,
            file_name='Imports.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Consumption",
            data=Gross_National_Expenditure_csv,
            file_name='Consumption.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Real Interest rate",
            data=Real_interest_rate_csv,
            file_name='Real Interest Rate.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Research Expenditure",
            data=research_expenditure_csv,
            file_name='Research Expenditure.csv',
            mime='text/csv',
        )
        st.download_button(
            label="Summary",
            data=summary_table,
            file_name='Summary.csv',
            mime='text/csv',
        )




