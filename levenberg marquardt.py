def next_step(f, J, H) :
    gamma = 0.5

    step = -linalg.inv(H) @ J
    if step @ -J <= 0 or linalg.norm(step) > 2 :
        step = -gamma * J

    return step

# Click into this cell and press [Shift-Enter] to start.
%run "readonly/sandpit-exercises.ipynb"
sandpit_gradient(next_step)
