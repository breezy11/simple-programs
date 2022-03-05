## Write a function called best that take two arguments: the 2-character abbreviated name of a state and an
## outcome name. The function reads the outcome-of-care-measures.csv file and returns a character vector
## with the name of the hospital that has the best (i.e. lowest) 30-day mortality for the specified outcome
## in that state. The hospital name is the name provided in the Hospital.Name variable. The outcomes can
## be one of “heart attack”, “heart failure”, or “pneumonia”. Hospitals that do not have data on a particular
## outcome should be excluded from the set of hospitals when deciding the rankings.

best <- function(state, outcome) {
  
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
  
  ## Return hospital name in that state with lowest 30-day death
  
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
  
  ## Print the hospital name with the least mortality numbers
  outcome_data$Hospital.Name[1]
}

best("SC", "heart attack")

best("NY", "pneumonia")

best("AK", "pneumonia")

best("TX", "heart attack")

best("TX", "heart failure")

best("MD", "heart attack")

best("MD", "pneumonia")

best("NY", "hert attack")