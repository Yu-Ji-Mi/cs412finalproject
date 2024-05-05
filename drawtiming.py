import matplotlib.pyplot as plt
import numpy as np


def drawtimingplot(times):
    input_times = list(range(1, len(times) + 1))
    _, ax = plt.subplots(figsize=(10, 6))
    ax.plot(input_times, times)
    ax.set_xlabel('Look Ahead')
    ax.set_ylabel('Time (seconds)')
    ax.set_title("Timings VS Node Look-Ahead")
    ax.set_xticks(input_times)
    ax.set_xticklabels(input_times)
    plt.show()
