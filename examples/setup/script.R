library(rjson)

args <- commandArgs(TRUE)
config <- fromJSON(file=args[1])

config$data
d <- read.csv(file=config$data)

config$runs
d$a1+d$a2

