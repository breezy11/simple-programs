## Write a function called rankall that takes two arguments: an outcome name (outcome) and a hospital ranking (num). The function reads the outcome-of-care-measures.csv file and returns a 2-column data frame
## containing the hospital in each state that has the ranking specified in num. For example the function call
## rankall("heart attack", "best") would return a data frame containing the names of the hospitals that
## are the best in their respective states for 30-day heart attack death rates. The function should return a value
## for every state (some may be NA). The first column in the data frame is named hospital, which contains
## the hospital name, and the second column is named state, which contains the 2-character abbreviation for
## the state name. Hospitals that do not have data on a particular outcome should be excluded from the set of
## hospitals when deciding the rankings.

rankall <- function(outcome, num = "best") {
  
  ## Read outcome data
  outcome_data <- read.csv("data/outcome-of-care-measures.csv", colClasses = "character", na.strings="Not Available")
  
  ## Transfer the outcome arguments to all lowercase letters
  outcome <- tolower(outcome)
  
  ## Check that outcome is valid
  
  if(!any(sapply(c("heart attack","heart failure","pneumonia"), function(x) outcome==x))){
    stop("invalid outcome")
  }
  
  # Create a dataframe that will be returned
  states <- unique(outcome_data$State) 
  states <- sort(states, decreasing = FALSE)
  hospitals <- character(length(states))
  df <- data.frame(hospitals, states)
  
  ## For each state, find the hospital of the given rank
  for(i in 1:length(states)){
    
    data <- read.csv("data/outcome-of-care-measures.csv", colClasses = "character", na.strings="Not Available")
    
    data = data %>% filter(State == df$states[i])
    
    colnames(data)[11] <- "heart attack"
    colnames(data)[17] <- "heart failure"
    colnames(data)[23] <- "pneumonia"
    
    data <- select(data, "Hospital.Name", "State" , outcome)
    
    data <- data[!is.na(data[outcome]),]
    
    data[outcome] <- lapply(data[outcome], as.numeric)
    
    data <- data[order(data[outcome], data$Hospital.Name), ]
    
    if(num=="best"){
      df[i, "hospitals"] <- data$Hospital.Name[1]
    }else if(num=="worst"){
      df[i, "hospitals"] <- tail(data$Hospital.Name, 1)
    }else{
        df[i, "hospitals"] <- data[num, "Hospital.Name"]
    }
    }
  
  
  ## Return a data frame with the hospital names and the
  ## (abbreviated) state name
  
  df
}

head(rankall("heart attack", 20), 10)

tail(rankall("pneumonia", "worst"), 3)

tail(rankall("heart failure"), 10)

r <- rankall("heart attack", 4)
as.character(subset(r, states == "HI")$hospital)

r <- rankall("pneumonia", "worst")
as.character(subset(r, states == "NJ")$hospital)

r <- rankall("heart failure", 10)
as.character(subset(r, states == "NV")$hospital)
