getwd()
setwd('C:\\Users\\cgt\\Desktop\\scrap_convenio')

arq  <- read.csv('teste_grav.csv')
rm(arq)


arq2 <- read.csv('teste_grav.csv')
typeof(arq2)
df_arq2 <- data.frame(arq2)
str(df_arq2)

# library(xlsx)
# write.xlsx(df_arq2, "C:\\Users\\cgt\\Desktop\\scrap_convenio\\")

write.csv(arq2, file = "C:\\Users\\cgt\\Desktop\\scrap_convenio\\OSR2500_plan.csv", row.names = FALSE)
?write.csv

main <- read.csv("OR25000.csv")
rm(main)
getwd()
library(XML)

doc.html <- htmlTreeParse('savedrecs.html', useInternal = TRUE)

rawHTML <- paste(readLines("savedrecs.html"), collapse="\n")


