import numpy as np


def next_step(f, J, H):

    B = 0.5
    a = 0.5

    v = np.zeros(2, 1)

    max_iterations = 100
    iteration = 0

    while iteration < max_iterations:
        V = B * v + (1 - B) * J @ H
        step = -a * V
        if np.linalg.norm(step) < 1 * np.exp(-5):
            break

        iteration += 1

    return step


%run "readonly/sandpit-exercises.ipynb"
sandpit_gradient(next_step)

