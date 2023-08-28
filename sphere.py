import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wireframe Sphere")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Camera settings
fov = 400
distance = 5
zoom_speed = 0.1

# Sphere settings
radius = 2
segments = 20
vertical_lines = 20

# Calculate points for the wireframe sphere
vertices = []
for v in range(vertical_lines + 1):
    phi = v * math.pi / vertical_lines
    for h in range(segments):
        theta = h * 2 * math.pi / segments
        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)
        vertices.append((x, y, z))

# Define edges by connecting vertices
edges = []
for v in range(vertical_lines):
    for h in range(segments):
        edges.append((v * segments + h, v * segments + (h + 1) % segments))
        edges.append((v * segments + h, (v + 1) * segments + h))

# Main loop
clock = pygame.time.Clock()
angle_x = 0
angle_y = 0
angle_z = 0
dragging = False

running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            dragging = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Scroll Up
            distance -= zoom_speed
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Scroll Down
            distance += zoom_speed

    if dragging:
        rel = pygame.mouse.get_rel()
        angle_x += rel[1] * 0.01
        angle_y += rel[0] * 0.01

    transform_matrix = [
        [math.cos(angle_y) * math.cos(angle_z), -math.cos(angle_x) * math.sin(angle_z) + math.sin(angle_x) * math.sin(angle_y) * math.cos(angle_z), math.sin(angle_x) * math.sin(angle_z) + math.cos(angle_x) * math.sin(angle_y) * math.cos(angle_z)],
        [math.cos(angle_y) * math.sin(angle_z), math.cos(angle_x) * math.cos(angle_z) + math.sin(angle_x) * math.sin(angle_y) * math.sin(angle_z), -math.sin(angle_x) * math.cos(angle_z) + math.cos(angle_x) * math.sin(angle_y) * math.sin(angle_z)],
        [-math.sin(angle_y), math.sin(angle_x) * math.cos(angle_y), math.cos(angle_x) * math.cos(angle_y)]
    ]

    transformed_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        new_x = transform_matrix[0][0] * x + transform_matrix[0][1] * y + transform_matrix[0][2] * z
        new_y = transform_matrix[1][0] * x + transform_matrix[1][1] * y + transform_matrix[1][2] * z
        new_z = transform_matrix[2][0] * x + transform_matrix[2][1] * y + transform_matrix[2][2] * z
        transformed_vertices.append((new_x, new_y, new_z))

    for edge in edges:
        x1, y1, z1 = transformed_vertices[edge[0]]
        x2, y2, z2 = transformed_vertices[edge[1]]
        x1, y1 = (x1 * fov / (z1 + distance) + width / 2), (y1 * fov / (z1 + distance) + height / 2)
        x2, y2 = (x2 * fov / (z2 + distance) + width / 2), (y2 * fov / (z2 + distance) + height / 2)
        pygame.draw.line(screen, white, (x1, y1), (x2, y2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
