## Write a function called rankhospital that takes three arguments: the 2-character abbreviated name of a
## state (state), an outcome (outcome), and the ranking of a hospital in that state for that outcome (num).
## The function reads the outcome-of-care-measures.csv file and returns a character vector with the name
## of the hospital that has the ranking specified by the num argument. For example, the call
## rankhospital("MD", "heart failure", 5)
## would return a character vector containing the name of the hospital with the 5th lowest 30-day death rate
## for heart failure. The num argument can take values “best”, “worst”, or an integer indicating the ranking
## (smaller numbers are better). If the number given by num is larger than the number of hospitals in that
## state, then the function should return NA. Hospitals that do not have data on a particular outcome should
## be excluded from the set of hospitals when deciding the rankings.

rankhospital <- function(state, outcome, num = "best") {
  ## Read outcome data
  outcome_data <- read.csv("data/outcome-of-care-measures.csv", colClasses = "character", na.strings="Not Available")
  
  ## Transfer the outcome arguments to all lowercase letters
  outcome <- tolower(outcome)
  
  ## Check that state and outcome are valid
  
  if(!any(sapply(outcome_data$State, function(x) state==x))){
    stop("invalid state")
  }
  
  if(!any(sapply(c("heart attack","heart failure","pneumonia"), function(x) outcome==x))){
    stop("invalid outcome")
  }
  
  ## Return hospital name in that state with the given rank
  ## 30-day death rate
  
  ## Filter the data by state
  outcome_data = outcome_data %>% filter(State == state)
  
  ## Change the name of the mortality columns
  colnames(outcome_data)[11] <- "heart attack"
  colnames(outcome_data)[17] <- "heart failure"
  colnames(outcome_data)[23] <- "pneumonia"
  
  ## Keep only the important columns
  outcome_data <- select(outcome_data, "Hospital.Name", "State" , outcome)
  
  ## Remove the na values
  outcome_data <- outcome_data[!is.na(outcome_data[outcome]),]
  
  ## Transform the character data into numeric
  outcome_data[outcome] <- lapply(outcome_data[outcome], as.numeric)
  
  ## Order by outcome
  outcome_data <- outcome_data[order(outcome_data[outcome], outcome_data$Hospital.Name), ]
  
  if(num=="best"){
    outcome_data$Hospital.Name[1]
  }else if(num=="worst"){
    return(tail(outcome_data$Hospital.Name, 1))
  }else{
    if(is.null(outcome_data[num, "Hospital.Name"])){
      return("NA")
    }else{
      return(outcome_data[num, "Hospital.Name"])
    }
  }
}

rankhospital("NC", "heart attack", "worst")

rankhospital("WA", "heart attack", 7)

rankhospital("TX", "pneumonia", 10)

rankhospital("NY", "heart attack", 7)

rankhospital("TX", "heart failure", 4)

rankhospital("MD", "heart attack", "worst")

rankhospital("MN", "heart attack", 5000)