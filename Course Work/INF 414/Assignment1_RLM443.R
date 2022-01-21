# Install required libraries if not already installed
if (!(require(deSolve))) install.packages("deSolve")
library(deSolve)

# ODE SYSTEM FUNCTION
SIR_ode = function(t, y, params)
{
  with(as.list(c(y, params)),
  {
    # STORAGE
    ## We need to have a vector of size equal to the number of ODEs in the system
    dydt = rep(0, 3)
    
    # Equations
    dydt[1] = -beta * y[1] * y[2]                 # S, susceptible hosts
    dydt[2] = beta * y[1] * y[2] - gamma * y[2]   # I, infectious hosts
    dydt[3] = gamma * y[2]                        # R, recovered/removed hosts
    
    return(list(dydt))
    
  })
}

# Specify parameter values
beta = 1.0
gamma = 1.0/10.0
R_Naught = beta/gamma

print(paste0("R_Naught = ", R_Naught))

# Store parameters in a named list
params = c(
  beta = beta,
  gamma = gamma
)

# Specify the initial conditions
# S+I+R = 1
S_t0 = 0.999
I_t0 = 1 - S_t0
R_t0 = 0

# Store initial conditions in a vector
inits = c(S_t0, I_t0, R_t0)

# Each time step that will be solved
time_ode = seq(0, 100, by = 0.1)

# Run ODE
out = ode(
  y = inits,
  times = time_ode,
  func = SIR_ode,
  method = "ode45",  # Runge-Kutta 4-5 method
  parms = params
)

# Object 'out' is a matrix
# Specify the column names, convert to a data frame
colnames(out) = c("time", "S", "I", "R")
out = data.frame(out)

# Set up a blank plot
plot(
  x = NA,
  y = NA,
  xlim = c(0, max(time_ode)),
  ylim = c(0, 1),
  xlab = "Time (Days)",
  ylab = "Fraction of the Population"
)

# Plot one line at a time:
# lines(out$S ~ out$time, lty = 1, col = "black")
# lines(out$I ~ out$time, lty = 1, col = "red")
# lines(out$R ~ out$time, lty = 1, col = "blue")

these_cols = c("black", "red", "blue")

# Plot same graph, but using a loop
for (i in 1:3)
{
  lines(out[,(i+1)] ~ out$time, lty = 1, col = these_cols[i])
}

S_vals = seq(0.1, 0.3, length.out = 10)

