import random
import string

def generate_test_file(file_path, num_vertices):
    vertices = list(string.ascii_lowercase)[:num_vertices]
    with open(file_path, 'w') as file:
        file.write(f"{num_vertices} {num_vertices*(num_vertices-1)//2}\n")
        for i in range(num_vertices):
            for j in range(i+1, num_vertices):
                u = vertices[i]
                v = vertices[j]
                w = random.randint(1, 25)  # Adjust the range of weights as needed
                file.write(f"{u} {v} {w}\n")

# Usage example
generate_test_file('/Users/jimi/Desktop/final412/cs412finalproject/graph.txt', 25)