import math

def polar_to_cartesian(cx, cy, r, angle_deg):
    angle_rad = math.radians(angle_deg - 90)
    return cx + r * math.cos(angle_rad), cy + r * math.sin(angle_rad)

def generate_donut_segment(cx, cy, inner_r, outer_r, start_angle, end_angle):
    start_outer = polar_to_cartesian(cx, cy, outer_r, start_angle)
    end_outer = polar_to_cartesian(cx, cy, outer_r, end_angle)
    start_inner = polar_to_cartesian(cx, cy, inner_r, start_angle)
    end_inner = polar_to_cartesian(cx, cy, inner_r, end_angle)
    
    large_arc_flag = 1 if end_angle - start_angle > 180 else 0

    return (f"M {start_outer[0]:.2f} {start_outer[1]:.2f} "
            f"A {outer_r} {outer_r} 0 {large_arc_flag} 1 {end_outer[0]:.2f} {end_outer[1]:.2f} "
            f"L {end_inner[0]:.2f} {end_inner[1]:.2f} "
            f"A {inner_r} {inner_r} 0 {large_arc_flag} 0 {start_inner[0]:.2f} {start_inner[1]:.2f} "
            f"Z")

def main():
    cx, cy = 300, 300
    outer_r = 250
    inner_r = 100
    num_segments = 5
    angle_step = 360 / num_segments
    
    labels = [
        "Communication\\nPortfolio",
        "Leadership\\nPortfolio",
        "HR\\nPortfolio",
        "Creative\\nPortfolio",
        "IT Projects\\nPortfolio"
    ]
    
    images = [
        "images/mic1.jpg",
        "images/team.jpg",
        "images/virtusa-training-1.jpg",
        "images/solo-branding-1.jpg",
        "images/iit-business-1.jpg"
    ]
    
    # Gap in degrees between segments
    gap = 2
    
    svg = f'<svg viewBox="0 0 600 600" class="portfolio-donut" xmlns="http://www.w3.org/2000/svg">\n'
    svg += '  <defs>\n'

    for i in range(num_segments):
        svg += f'    <pattern id="img-{i}" patternUnits="userSpaceOnUse" width="600" height="600">\n'
        svg += f'      <image href="{images[i]}" x="0" y="0" width="600" height="600" preserveAspectRatio="xMidYMid slice"/>\n'
        # Add a dark overlay pattern so the text is readable
        svg += f'      <rect x="0" y="0" width="600" height="600" fill="#0B0A09" fill-opacity="0.6"/>\n'
        svg += f'    </pattern>\n'

    svg += '  </defs>\n'

    links = ["communication", "leadership", "hr", "creative", "it"]

    for i in range(num_segments):
        start_angle = i * angle_step + gap / 2
        end_angle = (i + 1) * angle_step - gap / 2
        
        # Segment path
        path_d = generate_donut_segment(cx, cy, inner_r, outer_r, start_angle, end_angle)
        
        # Center of the segment for text/icon placement
        mid_angle = (start_angle + end_angle) / 2
        mid_r = (inner_r + outer_r) / 2
        text_x, text_y = polar_to_cartesian(cx, cy, mid_r, mid_angle)
        
        # Calculate radial offset for hover translate (push out from center)
        # We want to push out by ~10px in the angle direction
        offset_dist = 12
        tx = offset_dist * math.cos(math.radians(mid_angle - 90))
        ty = offset_dist * math.sin(math.radians(mid_angle - 90))
        
        lines = labels[i].split("\\n")
        
        svg += f'  <g class="donut-segment" data-index="{i}" onclick="window.location.href=\'#{links[i]}\'" style="--tx: {tx:.2f}px; --ty: {ty:.2f}px;">\n'
        svg += f'    <path d="{path_d}" class="donut-path" fill="url(#img-{i})" />\n'
        
        # Add Text
        svg += f'    <text x="{text_x}" y="{text_y - 6}" class="donut-text" text-anchor="middle">\n'
        svg += f'      <tspan x="{text_x}" dy="0">{lines[0]}</tspan>\n'
        if len(lines) > 1:
            svg += f'      <tspan x="{text_x}" dy="22">{lines[1]}</tspan>\n'
        svg += f'    </text>\n'
        svg += f'  </g>\n'

    svg += '</svg>\n'
    
    with open('donut.svg', 'w') as f:
        f.write(svg)
    print("Donut SVG generated.")

if __name__ == "__main__":
    main()
