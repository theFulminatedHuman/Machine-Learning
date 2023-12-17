# Here the function is defined
def linfit(xdat,ydat):
  # Here xbar and ybar are calculated
  xbar = np.sum(xdat)/len(xdat)
  ybar = np.sum(ydat)/len(ydat)

  # Insert calculation of m and c here. If nothing is here the data will be plotted with no linear fit
  a = 0
  b = 0
  chi = 0
  for xi, yi in zip(xdat, ydat) :
    a = a + (xi - xbar) * yi
    b = b + (xi - xbar)**2
  m = a/b
  
  c = ybar - m * xbar
  for xi, yi in zip(xdat, ydat) :
    chi = chi + (yi - m*xi - c)**2
  print(chi) 


  # Return your values as [m, c]
  return [m, c]

# Produce the plot - don't put this in the next code block
line()