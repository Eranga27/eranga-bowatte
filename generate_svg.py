import math
import re

def polar_to_cartesian(cx, cy, r, angle_deg):
    angle_rad = math.radians(angle_deg - 90)
    return (cx + r * math.cos(angle_rad), cy + r * math.sin(angle_rad))

def create_arc(cx, cy, r_outer, r_inner, start_angle, end_angle):
    start_outer = polar_to_cartesian(cx, cy, r_outer, end_angle)
    end_outer = polar_to_cartesian(cx, cy, r_outer, start_angle)
    start_inner = polar_to_cartesian(cx, cy, r_inner, end_angle)
    end_inner = polar_to_cartesian(cx, cy, r_inner, start_angle)
    large_arc = 1 if end_angle - start_angle > 180 else 0
    d = [
        f"M {start_outer[0]:.2f} {start_outer[1]:.2f}",
        f"A {r_outer} {r_outer} 0 {large_arc} 0 {end_outer[0]:.2f} {end_outer[1]:.2f}",
        f"L {end_inner[0]:.2f} {end_inner[1]:.2f}",
        f"A {r_inner} {r_inner} 0 {large_arc} 1 {start_inner[0]:.2f} {start_inner[1]:.2f}",
        "Z"
    ]
    return " ".join(d)

paths = []
for i in range(6):
    mid_angle = (i*60 + 2 + (i+1)*60 - 2) / 2
    # Calculate a small translation vector for hover effect
    tx = 12 * math.cos(math.radians(mid_angle - 90))
    ty = 12 * math.sin(math.radians(mid_angle - 90))
    
    url = [
        'communication.html',
        'leadership.html',
        'creative.html',
        'human-resources.html',
        'business-development.html',
        'technology.html'
    ][i]

    paths.append(f'<g class="donut-segment" data-index="{i}" onclick="window.location.href=\'{url}\'" style="--tx: {tx:.2f}px; --ty: {ty:.2f}px;">\n            <path d="{create_arc(300, 300, 250, 100, i*60 + 2, (i+1)*60 - 2)}" class="donut-path" fill="url(#img-{i})" />\n          </g>')

print("\n".join(paths))
