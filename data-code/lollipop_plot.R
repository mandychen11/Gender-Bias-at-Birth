# Library
library(ggplot2)
library(dplyr)
library(hrbrthemes)
library(tidyverse)
library(ggpubr)
setwd("~/Desktop/ANLY 503/Project")
mydf <- read_csv("infant_mortality.csv")

mydf.high <- filter(mydf,`World Bank Income Group` == "High income")
mydf.low <- filter(mydf,`World Bank Income Group` == "Low income")
mydf.lower <- filter(mydf,`World Bank Income Group` == "Lower middle income")
mydf.upper <- filter(mydf,`World Bank Income Group` == "Upper middle income")


mydf <- mydf %>% 
  rowwise() %>% 
  mutate( mymean = mean(c(Male,Female) )) %>% 
  arrange(mymean) %>% 
  mutate(Country=factor(Country, Country))

# Plot
high = ggplot(mydf.high) +
  geom_segment( aes(x=Country, xend=Country, y=Male, yend=Female), color="grey") +
  geom_point( aes(x=Country, y=Male), color=rgb(0.2,0.7,0.1,0.5), size=3 ) +
  geom_point( aes(x=Country, y=Female), color=rgb(0.7,0.2,0.1,0.5), size=3 ) +
  coord_flip()+
  # theme_ipsum() +
  theme(
    legend.position = "none",
  ) +
  xlab("") +
  ylab("Mortality Rate") +
  labs(title = "High Income Countries",
       subtitle = "High-income countries tend to have smaller gaps between female and male's infant mortality rates, \n except for several outliers such as Nauru, Palau, Oman.",
       caption = "UN Interagency Group on Mortality Estimates") +
  theme_minimal()

low = ggplot(mydf.low) +
  geom_segment( aes(x=Country, xend=Country, y=Male, yend=Female), color="grey") +
  geom_point( aes(x=Country, y=Male), color=rgb(0.2,0.7,0.1,0.5), size=3 ) +
  geom_point( aes(x=Country, y=Female), color=rgb(0.7,0.2,0.1,0.5), size=3 ) +
  coord_flip()+
  theme(
    legend.position = "none",
  ) +
  xlab("") +
  ylab("Mortality Rate") + 
  labs(title = "Low Income Countries",
       subtitle = "Low-income countries have been suffering from a relatively severe \n discrepancy between gender's infant survival.",
       caption = "UN Interagency Group on Mortality Estimates") +
  theme_minimal()

lower = ggplot(mydf.lower) +
  geom_segment( aes(x=Country, xend=Country, y=Male, yend=Female), color="grey") +
  geom_point( aes(x=Country, y=Male), color=rgb(0.2,0.7,0.1,0.5), size=3 ) +
  geom_point( aes(x=Country, y=Female), color=rgb(0.7,0.2,0.1,0.5), size=3 ) +
  coord_flip()+
  theme_ipsum() +
  theme(
    legend.position = "right",
  ) +
  xlab("") +
  ylab("Mortality Rate") + 
  labs(title = "Lower Middle Income Countries",
       subtitle = "Most lower-middle income countries are having serious gender bias. \n India is special as its two dots are closely located, further analysis should be addressed with its population structure.",
       caption = "UN Interagency Group on Mortality Estimates") +
  theme_minimal()


upper = ggplot(mydf.upper) +
  geom_segment( aes(x=Country, xend=Country, y=Male, yend=Female), color="grey") +
  geom_point( aes(x=Country, y=Male), color=rgb(0.2,0.7,0.1,0.5), size=3 ) +
  geom_point( aes(x=Country, y=Female), color=rgb(0.7,0.2,0.1,0.5), size=3 ) +
  coord_flip()+
  theme_ipsum() +
  theme(
    legend.position = "right",
  ) +
  xlab("") +
  ylab("Mortality Rate") + 
  labs(title = "Upper Middle Income Countries",
       subtitle = "Situations have worsened in upper-middle income countries, \n Equatorial Guinea is still having significant gender bias.",
       caption = "UN Interagency Group on Mortality Estimates") +
  theme_minimal()


plot <- ggarrange(high, upper, lower, low, ncol = 2, nrow = 2)
annotate_figure(plot, top = text_grob("Infant Mortality Rate (Per 1000 Live Births) By Income Group, 2019", 
                                      color = "black", face = "bold", size = 24))
