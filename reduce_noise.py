with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("opacity='0.15'", "opacity='0.08'")

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Noise reduced')
