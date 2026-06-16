import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace style block
    content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="styles.css">', content, flags=re.DOTALL)
    
    # Replace script block
    content = re.sub(r'<script>.*?</script>', '<script src="main.js" defer></script>', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('index.html')
update_file('experience.html')
print("HTML files updated")
