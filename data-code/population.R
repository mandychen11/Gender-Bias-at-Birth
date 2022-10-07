library(tidyverse)
library(CGPfunctions)
library(ggthemes)
library(ggplot2)
library(dplyr)
setwd("~/Desktop/ANLY 503/Project/Project_Xiaomeng")
# World population - slope chart
## READ
world_pop <- read_csv('World_Pop_By_Sex.csv')
## MELT
world_pop.1 <- world_pop %>% pivot_longer(cols=`1990`:`2020`, names_to='Year', values_to='Counts')
head(world_pop.1) # chr+chr+dbl
world_pop.1 <- na.omit(world_pop.1)
world_pop.1$Counts <- world_pop.1$Counts/1000
world_pop.1$Counts <- round(world_pop.1$Counts, digits = 2)
## PLOT
# newggslopegraph(world_pop.1, Year, Counts, Region,
#                 Title = "World Population",
#                 SubTitle = "Total population (both sexes combined) by region, annually for 1990-2020 (thousands)",
#                 TitleTextSize = 25, SubTitleTextSize = 15, YTextSize = 3.5,
#                 TitleJustify = "center", SubTitleJustify = "center",
#                 DataTextSize = 2.5)
newggslopegraph(world_pop.1, Year, Counts, Region,
                Title = "World Population",
                SubTitle = "Total population (both sexes combined) by continents, annually for 1990-2020 (millions)",
                Caption = "Figure-1: This slope chart gives a basic overview of world's population structure from 1990 to 2020 on a five-year basis. \n The number shown in each line denotes real absolute population in millions.\n Except Europe, every continent's population has been increasing in the last three decades, where Asia is on the top of others and has biggest increase.",
                TitleTextSize = 25, SubTitleTextSize = 15, CaptionTextSize = 15, YTextSize = 5.5,
                TitleJustify = "center", SubTitleJustify = "center",CaptionJustify = "left",
                DataTextSize = 4.5, WiderLabels = TRUE, ThemeChoice = "gdocs")


# Under five mortality - Grouped Bubble Chart
gpd_per_capita <- read_csv('GDP_Per_Capita.csv')
deaths <- read_csv('Deaths.csv')
mortality_rates <- read_csv('Mortality_Rates.csv')
group <- read_csv('Income_group.csv')
## MERGE and CLEAN
mydf <- merge(gpd_per_capita[,c(1,5)], deaths[,c(1,4)], by = 1, all = TRUE)
mydf <- merge(mydf, mortality_rates[,c(1,4)], by = 1, all = TRUE)
mydf <- merge(mydf, group, by = 1, all = TRUE)

mydf$GDP = gsub('[-]','',mydf$GDP)
mydf$GDP <- as.numeric(mydf$GDP)
mydf$Geographic_area <- as.factor(mydf$Geographic_area)
mydf$Income_group <- as.factor(mydf$Income_group)
mydf <- na.omit(mydf)
str(mydf)
mydf <- mydf[!mydf$log_GDP == "#VALUE!", ]



## PLOT
library(hrbrthemes)
library(viridis)


# mydf %>%
#   arrange(desc(Counts)) %>%
#   mutate(Geographic_area = factor(Geographic_area, Geographic_area)) %>%
#   ggplot(aes(x=log_GDP, y=Rates, size = Counts, color=Income_group)) +
#   geom_point(alpha=0.5) +
#   scale_size(range = c(.1, 24), name="Under-five Deaths") +
#   scale_fill_viridis(discrete=TRUE, guide="none", option="A") +
#   theme_ipsum() +
#   theme(legend.position="bottom") +
#   labs(title = "Under-five Mortality Rates, 2019 and GDP per capita by Country") +
#   ylab("Under-five Mortality Rates (per 1,000 lives)") +
#   xlab("GDP per Capita (log)") +
#   theme(legend.position = "right",  axis.text.x=element_blank())
# 
# levels(mydf$Income_group)
# mydf$Income_group <- factor(mydf$Income_group, levels = c("High income", "Upper middle income", "Lower middle income", "Low income"))

p <- mydf %>%
  # prepare text for tooltip
  mutate(text = paste("Country: ", Geographic_area, "\nUnder-Five Deaths: ", Counts, "\nMortality Rate: ", Rates, "\nGDP Per Capita (Log): ", log_GDP, 
                      "\nIncome Group: ", Income_group, sep="")) %>%
  
  # Classic ggplot
  ggplot( aes(x=log_GDP, y=Rates, size = Counts, color = Income_group,text=text)) +
  geom_point(alpha=0.6) +
  scale_size(range = c(1.4, 19), name="Under-Five Deaths") +
  scale_color_viridis(discrete=TRUE, guide="none",option="C") +
  # scale_fill_discrete(breaks=c('High income', 'Upper-middle income', 'Lower-middle income', 'Low income')) + 
  ggtitle("Under-Five Mortality Rates, 2019. How Does It Relate To GDP And Income Group?") +
  theme(plot.title = element_text(hjust = 0.5))+
  ylab("Under-Five Mortality Rates (Per 1,000 Lives)") +
  xlab("GDP Per Capita (Log)") +
  theme(legend.position = "right", axis.text.x=element_blank())

# turn ggplot interactive with plotly
pp <- ggplotly(p, tooltip="text")
pp
htmlwidgets::saveWidget(as_widget(pp), "bubble.html")
