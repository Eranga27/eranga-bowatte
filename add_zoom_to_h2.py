import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace <h2 class="some-class"> with <h2 class="some-class reveal-zoom">
    # and <h2> with <h2 class="reveal-zoom">
    # But ONLY if it doesn't already have reveal-zoom
    
    def replace_h2(match):
        full_tag = match.group(0)
        if 'reveal-zoom' in full_tag:
            return full_tag
            
        if 'class="' in full_tag:
            return full_tag.replace('class="', 'class="reveal-zoom ')
        else:
            return full_tag.replace('<h2', '<h2 class="reveal-zoom"')
            
    # Find all <h2 ...> or <h2> tags
    new_content = re.sub(r'<h2[^>]*>', replace_h2, content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated h2 tags in {f}')
