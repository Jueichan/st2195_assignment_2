# scrape_csv.R
# ST2195 Assignment 2 - R version

# install.packages("rvest")  # Run once if not already installed
library(rvest)

# Define the target URL
url <- "https://en.wikipedia.org/wiki/Delimiter-separated_values"

# Read HTML from the page
page <- read_html(url)

# Extract all tables
tables <- html_table(page, fill = TRUE)

# Show first few rows
head(tables[[1]])

# Save to CSV
write.csv(tables[[1]], "csv_example_r.csv", row.names = FALSE)

# Verify it
verified <- read.csv("csv_example_r.csv")
head(verified)
