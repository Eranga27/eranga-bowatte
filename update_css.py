with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make background more noticeable
css = css.replace("opacity='0.04'", "opacity='0.15'")
css = css.replace("rgba(195,140,6,0.15)", "rgba(195,140,6,0.22)")
css = css.replace("rgba(180,120,4,0.12)", "rgba(180,120,4,0.18)")
css = css.replace("rgba(150,100,3,0.08)", "rgba(150,100,3,0.12)")

# Add keyframe animation for donut
if '@keyframes spinDonut' not in css:
    css += '''\n
@keyframes spinDonut {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.portfolio-donut {
  animation: spinDonut 50s linear infinite;
}
.portfolio-donut.paused {
  animation-play-state: paused;
}
'''

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('styles updated successfully')
