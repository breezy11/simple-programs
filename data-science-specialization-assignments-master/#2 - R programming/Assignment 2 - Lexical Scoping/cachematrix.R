## Put comments here that give an overall description of what your
## functions do

## Write a short comment describing this function

# Function that creates the functions needed to work with the matrix.

makeCacheMatrix <- function(x = matrix()) {
  inv <- NULL
  set <- function(y){
    x <<- y 
    inv <<- NULL
  }
  get <- function() {x}
  setInverse <- function(inverse) {inv <<- inverse}
  getInverse <- function(){inv}
  list(set = set, get = get, setInverse = setInverse, getInverse = getInverse)
}


## Write a short comment describing this function

# Function calculates the inverse of the matrix if it hasn't been calculated yet.
# First it checks the cache, if the returned value is NULL it calculates the inverse.

cacheSolve <- function(x, ...) {
  ## Return a matrix that is the inverse of 'x'
  
  inv <- x$getInverse()
  
  if(!is.null(inv)){
    message("getting cached data")
    return(inv)
  }
  
  mat <- x$get()
  inv <- solve(mat, ...)
  x$setInverse(inv)
  inv
}

# Create a 2 by 2 matrix
pmatrix <- makeCacheMatrix(matrix(1:4, nrow=2, ncol=2))

# Getting the matrix and printing it
pmatrix$get()

# Trying to get the inverse of function, but it returns NULL because it hasn't been cached yet
pmatrix$getInverse()

# Caching the matrix
cacheSolve(pmatrix)

# 2nd time running this function, we will get the inverse out of the cache
cacheSolve(pmatrix)

# 2nd time running this function, we get the inverse
pmatrix$getInverse()
