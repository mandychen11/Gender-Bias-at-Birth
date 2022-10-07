library(tidyverse)
library(plotly)
library(htmlwidgets)
library(readxl)

ratio_brith = read.csv("Sex_ratio_rate_at_birth.csv")
ratio_five = read.csv("sex-ratio-at-birth-vs-five-years-old.csv")
region = read.csv("region.csv")

ratio_df = ratio_brith[, c(1, 3, 4)] %>% 
  left_join(ratio_five[, c(1, 3, 5)],
            by = c('Entity' = 'Entity', 
                   "Year" = "Year"))
ratio_df = ratio_df %>%
  left_join(region[, c(1, 4)],
            by = c("Entity" = "Entity"))

colnames(ratio_df) = c("Country", "Year", "Ratio_at_birth",
                       "Ratio_at_five", "Continent")

write.csv(na.omit(ratio_df),
          "ratio_df.csv",
          row.names = FALSE)