import os

# Config
TARGET_DIR = "."  # or "visuals" if you're storing HTMLs in a subfolder
OUTPUT_FILE = "index.html"
EXCLUDE_FILES = {"index.html"}

# Scan for HTML files
html_files = [
    f for f in os.listdir(TARGET_DIR)
    if f.endswith(".html") and f not in EXCLUDE_FILES
]

# Sort alphabetically
html_files.sort()

# Build HTML list
list_items = "\n".join([
    f'<li><a href="#" onclick="openPopup(\'{f}\')">{f}</a></li>'
    for f in html_files
])

# HTML Template
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HTML Visual Gallery</title>
  <style>
    body {{ font-family: sans-serif; padding: 2rem; }}
    li {{ margin-bottom: 0.5rem; }}
    .modal {{ display: none; position: fixed; top: 0; left: 0;
             width: 100%; height: 100%; background: rgba(0,0,0,0.8);
             justify-content: center; align-items: center; }}
    iframe {{ width: 80vw; height: 80vh; border: none; }}
    .close {{ position: absolute; top: 20px; right: 40px; font-size: 2rem; color: white; cursor: pointer; }}
  </style>
</head>
<body>
  <h1>📊 HTML Visuals</h1>
  <ul id="fileList">
    {list_items}
  </ul>

  <div class="modal" id="modal">
    <span class="close" onclick="closePopup()">×</span>
    <iframe id="modalFrame"></iframe>
  </div>

  <script>
    function openPopup(src) {{
      document.getElementById('modalFrame').src = src;
      document.getElementById('modal').style.display = 'flex';
    }}
    function closePopup() {{
      document.getElementById('modal').style.display = 'none';
      document.getElementById('modalFrame').src = '';
    }}
    document.getElementById('modal').addEventListener('click', function(e) {{
      if (e.target === this) closePopup();
    }});
  </script>
</body>
</html>
"""

# Write to file
with open(OUTPUT_FILE, "w") as f:
    f.write(html_template)

print(f"✅ index.html generated with {len(html_files)} HTML files.")
