def next_step(f, J, H):
  return -H @ J

# Click into this cell and press [Shift-Enter] to start.
%run
"readonly/sandpit-exercises.ipynb"
sandpit_gradient(next_step)
