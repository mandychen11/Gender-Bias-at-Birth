# Library
library(ggplot2)
library(dplyr)
library(hrbrthemes)
library(tidyverse)
library(ggpubr)
library(treemap)
library(sunburstR)
library(CGPfunctions)
library(plotly)
setwd("~/Desktop/ANLY 503/Project/Project_Xiaomeng")
mydf <- read_csv("trafficking_factors.csv")
names(mydf) <- c("Regions","Sex","Sexual Exploitaton","Forced Labour","Other Forms of exploitation")
mydf.1 <- mydf %>% pivot_longer(cols=`Sexual Exploitaton`:`Other Forms of exploitation`, names_to='Factors', values_to='Counts')
head(mydf.1) 

# Reformat mydf.1 for the sunburstR package
mydf.2 <- mydf.1 %>%
  filter(Regions != "") %>%
  mutate(path = paste(Regions, Factors, Sex, sep="-")) %>%
  dplyr::select(path, Counts)
str(mydf.2)
# Plot
# p.2 <- sunburst(mydf.2, legend=TRUE)
# p.2
# htmlwidgets::saveWidget(as_widget(p.2), "sunburst.html")

sb4 <- sund2b(mydf.2, width="100%", showLabels = TRUE,
              colors = list(range = RColorBrewer::brewer.pal(9, "Set3")))
sb4
