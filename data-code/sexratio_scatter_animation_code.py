import pandas as pd
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go #has more control, customizable
import plotly.io as pio #produce an html file
import plotly.express as px #fast, low effort
import altair as alt
import numpy as np

#######################################################################################
############################## Interactive scatter plot ##############################
ratio_df = pd.read_csv("ratio_df.csv")

ratio_df2=ratio_df[(ratio_df["Year"]>=1960)]

TS1=px.scatter(ratio_df2, x="Ratio_at_five", y="Ratio_at_birth",
               animation_frame="Year", 
               animation_group="Country",
               symbol="Continent",
               #size="pop",
               log_x=True, 
               color="Continent", hover_name="Country", 
               #range_y=[90,125], range_x=[75,125],
               range_x=[90,120], range_y=[90,120],
               size_max=55,
               symbol_sequence = ["circle","diamond","square","x","cross","star"],
               color_discrete_sequence=["#C6C37C",  # Asia
                                        "#8CC093",  # Europe
                                        "#E3ABB0", # Africa
                                        "#A7B9EB", # North America
                                        px.colors.qualitative.Plotly[3], # South America
                                        px.colors.qualitative.Plotly[8] # Oceania
                                       ]
              )

TS1.update_layout(
    xaxis=dict(title_text="Sex Ratio At Five-Year-Old (males per 100 females) <br><sup>Figure-3: Sex ratio at birth vs at five years old from 1960 to 2015. The general occurring sex ratio is around 105.</sup>"),
    yaxis=dict(title_text="Sex Ratio At Birth (males per 100 females)"),
    autosize=False,
    width=700,
    height=700,
    title_text='<b>How Have The Sex Ratios For Different Continents Changed Over Time?</b>', title_x=0.5,
    paper_bgcolor='rgba(0,0,0,0)',
    #margin=dict(l=50, r=20, t=20, b=200),
    plot_bgcolor='rgba(0,0,0,0)'
)

TS1.update_xaxes(showgrid=True, gridwidth=1,gridcolor="lightgray")
TS1.update_yaxes(showgrid=True, gridwidth=1,gridcolor="lightgray")

TS1.add_shape(
    type="line", line_color="red", line_width=3, opacity=1, line_dash="dot",
    x0=0, x1=0.53, xref="paper", y0=105, y1=105, yref="y"
)

TS1.add_shape(
    type="line", line_color="red", line_width=3, opacity=1, line_dash="dot",
    x0=105, x1=105, xref="x", y0=0, y1=0.5, yref="paper"
)

TS1['layout']['updatemenus'][0]['pad']=dict(r= 10, t= 120)
TS1['layout']['sliders'][0]['pad']=dict(r= 10, t= 120)


TS1.update_xaxes(tickfont=dict(color='#7f7f7f', size=10))
TS1.update_yaxes(tickfont=dict(color='#7f7f7f', size=10))



TS1.show()