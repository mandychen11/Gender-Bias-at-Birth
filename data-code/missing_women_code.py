import pandas as pd
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go #has more control, customizable
import plotly.io as pio #produce an html file
import plotly.express as px #fast, low effort
import altair as alt
import numpy as np

#######################################################################################
############################ Missing women data cleaning ##############################

missing_women = pd.read_csv("missing-female.csv")
missing_women.loc[missing_women['Country'] == "China", 'Country_2'] = "China"
missing_women.loc[missing_women['Country'] == "India", 'Country_2'] = "India"
missing_women.Country_2 = missing_women.Country_2.fillna("Other Country")
women_2=missing_women.groupby(["Country_2", "Year_with_next_five_years"]).sum()
women_2=women_2.reset_index() 

############################### Altail #####################################
# https://altair-viz.github.io/gallery/scatter_with_layered_histogram.html
selector = alt.selection_single(empty='all',
                                on='mouseover',
                                fields=['Country_2'])
base = alt.Chart(women_2).properties(
    width=250,
    height=250
).add_selection(selector)


line1=base.mark_line(point=True, strokeWidth=5).encode(
    x=alt.X('Year_with_next_five_years',
            title='Year'),
    y=alt.Y('Missing_female_births',
            scale=alt.Scale(domain=[0,1800000]),
            title='Missing Female Births (per year)'),
    color=alt.condition(selector,
                        'Country_2:N',
                       alt.value('lightgray'),
                        legend=alt.Legend(title="Country"),
                        scale=alt.Scale(scheme="accent")
                       ),
    size=alt.condition(~selector, alt.value(3), alt.value(5)
                      )
)


line2=base.mark_line().encode(
    x=alt.X('Year_with_next_five_years',
            #scale=alt.Scale(domain=[0,84])
            title='Year'),
    y=alt.Y('Excess_female_deaths',
            scale=alt.Scale(domain=[0,1800000]),
            title='Excess Female Deaths (per year)'),
    color=alt.condition(selector,
                        'Country_2:N',
                       alt.value('lightgray'),
                       legend=alt.Legend(title="Country"),
                       scale=alt.Scale(scheme="accent")),
    size=alt.condition(~selector, alt.value(3), alt.value(5)
                      )
).transform_filter(
    selector
)
    
    
linked=(line1 | line2).properties(
    title={
      "text": ["Annual Number Of Missing Female Births And Excess Mortality", "",""], 
      "color": "black",
        "fontSize":16,
        "anchor":'middle'
    }
)
