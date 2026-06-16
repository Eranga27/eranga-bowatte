with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Body background
old_body = """body{
    background: #0B0A09;
    background-image:
      radial-gradient(ellipse 90% 60% at 0% 0%,   rgba(195,140,6,0.10) 0%, transparent 55%),
      radial-gradient(ellipse 80% 55% at 100% 100%, rgba(180,120,4,0.08) 0%, transparent 55%),
      radial-gradient(ellipse 60% 40% at 50% 50%,  rgba(150,100,3,0.04) 0%, transparent 65%);
    background-attachment: fixed;"""
new_body = """body{
    background: #0B0A09;
    background-image:
      url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.04'/%3E%3C/svg%3E"),
      radial-gradient(ellipse 90% 60% at 0% 0%, rgba(195,140,6,0.15) 0%, transparent 60%),
      radial-gradient(ellipse 80% 55% at 100% 100%, rgba(180,120,4,0.12) 0%, transparent 60%),
      radial-gradient(ellipse 60% 40% at 50% 50%, rgba(150,100,3,0.08) 0%, transparent 65%);
    background-attachment: fixed;"""
css = css.replace(old_body, new_body)

# Nav desktop
old_nav = """    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    background: rgba(11, 10, 9, 0.65);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);"""
new_nav = """    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    background: rgba(11, 10, 9, 0.35);
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);"""
css = css.replace(old_nav, new_nav)

# Nav mobile
old_nav_mob = """      background: rgba(11, 10, 9, 0.75);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);"""
new_nav_mob = """      background: rgba(11, 10, 9, 0.35);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);"""
css = css.replace(old_nav_mob, new_nav_mob)

# Mobile Menu
old_menu = """      background: rgba(11, 10, 9, 0.85);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);"""
new_menu = """      background: rgba(11, 10, 9, 0.5);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);"""
css = css.replace(old_menu, new_menu)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS updated")
