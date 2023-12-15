library(readxl)
library(data.table)
library(dplyr)

ei39 <- read_excel("data/ecoinvent-3.9-biosphere.xlsx") |> as.data.table()
ei310 <- read_excel("data/ecoinvent-3.10-biosphere.xlsx") |> as.data.table()

delete <- anti_join(ei39, ei310, by = "uuid") |> pull(uuid) # deleted 428
create <- anti_join(ei310, ei39, by = "uuid") |> pull(uuid) # added 72

ei39_harmonized <- ei39[!uuid %in% delete]
ei310_harmonized <- ei310[!uuid %in% create]

anti_join(ei39_harmonized, ei310_harmonized, by = "uuid")
anti_join(ei39_harmonized, ei310_harmonized, by = "id")

inner_join(ei39_harmonized, ei310_harmonized, by = "id")


ei39[uuid == "38a622c6-f086-4763-a952-7c6b3b1c42ba"]
ei310[uuid == "38a622c6-f086-4763-a952-7c6b3b1c42ba"]
