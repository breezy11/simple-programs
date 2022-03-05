x <- list(a = 1:4, b = rnorm(10), c = rnorm(20,1), d = rnorm(100,5))

sapply(x, mean)

lapply(x, mean)

x <- list(a = matrix(1:4, 2, 2), b = matrix(1:6, 3, 2))

lapply(x, function(elt) elt[,1])

x <- matrix(rnorm(200), 20, 10)

apply(x, 2, mean)

apply(x, 1, mean)

apply(x, 1, quantile, probs = c(0.25, 0.75))

noise <- function(n, mean, sd){
  rnorm(n, mean, sd)
}

mapply(noise, 1:5, 1:5, 2)