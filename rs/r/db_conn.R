readRenviron(".Renviron")

library(RPostgreSQL)

conn <- dbConnect(
  RPostgreSQL::PostgreSQL(),
  host = Sys.getenv("DB_HOST"), # 'localhost' for local RStudio
  port = Sys.getenv("DB_PORT"), # '15432' for local RStudio
  dbname = Sys.getenv("DB_NAME"),
  user = Sys.getenv("DB_USER"),
  password = Sys.getenv("DB_PASS"))

res <- dbGetQuery(conn, "SELECT VERSION();")

print(res)

dbDisconnect(conn)

