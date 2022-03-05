URL <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv"
x <- getURL(URL)

out <- read.csv(textConnection(x))

sum(!is.na(out$VAL[out$VAL == 24]))

fileUrl <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx"
download.file(fileUrl, destfile = "question3.xlsx", method="curl")
dateDownloaded <- date()

df <- read_excel("question3.xlsx")

str(df)


dat <- df[18:23, 7-15]

