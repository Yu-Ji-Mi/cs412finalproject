import random
import string

def generate_test_file(file_path, num_vertices, num_edges):
    vertices = list(string.ascii_lowercase)[:num_vertices]
    with open(file_path, 'w') as file:
        file.write(f"{num_vertices} {num_edges}\n")
        for _ in range(num_edges):
            u = random.choice(vertices)
            v = random.choice(vertices)
            while u == v:
                v = random.choice(vertices)
            w = random.randint(-50, 50)  # Adjust the range of weights as needed
            file.write(f"{u} {v} {w}\n")

# Usage example
generate_test_file('/Users/jimi/Desktop/final412/cs412finalproject/graph.txt', 50, 100)
