# Reading from mysql

ucscDB <- dbConnect(MySQL(), user="genome",
                    host="genome-mysql.cse.ucsc.edu")
result <- dbGetQuery(ucscDB, "show databases;");
dbDisconnect(ucscDB);

result

hg19 <- dbConnect(MySQL(), user="genome", db="hg19",
                  host="genome-mysql.cse.ucsc.edu")
allTables <- dbListTables(hg19)
length(allTables)

allTables[1:5]

dbListFields(hg19, "affyU133Plus2")

dbGetQuery(hg19, "select count(*) from affyU133Plus2")

affyData <- dbReadTable(hg19, "affyU133Plus2")
head(affyData)

query <- dbSendQuery(hg19, "select * from affyU133Plus2 where misMatches between 1 and 3")
affyMis <- fetch(query);
quantile(affyMis$misMatches)

affyMisSmall <- fetch(query, n=10);
dbClearResult(query);

dim(affyMisSmall)

dbDisconnect(hg19)

# reading from the web

con = url("http://scholar.google.com/citations?user=HI-I6C0AAAAJ&hl=en")
htmlCode = readLines(con)
close(con)
htmlCode

url <-"http://scholar.google.com/citations?user=HI-I6C0AAAAJ&hl=en"
html <- htmlTreeParse(url, useInternalNodes=T)

# Error failed to load external entity

xpathSApply(html, "//title", xmlValue)

# Get from the httr package

library(httr)
html2 = GET(url)
content2 = content(html2, as="text")
parseHtml = htmlParse(content2, asText=TRUE)
xpathSApply(parsedHtml, "//title", xmlValue)


# Reading from APIs

# Accessing Twitter from R

myapp = oauth_app("twitter", 
                  key="my consumer key", secret = "consumer secret")
sig = sign_oauth1.0(myapp, 
                    token = "token here",
                    token_secret = "token secret here")
homeTL = GET("https:linkOdApia-a", sig)

# Converting the json object

json1 = content(homeTL)
json2 = jsonlite::fromJSON(toJSON(json1))
json2[1, 1:4]

# Reading from other sources

s