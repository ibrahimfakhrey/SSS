"""
Replace the services section with dynamic Jinja2 loop
"""

print("🔄 Making services section dynamic...")

# Read the index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the services section (starts around line 1226)
start_marker = None
end_marker = None

for i, line in enumerate(lines):
    if '<div class="grid-3" style="margin-top:18px">' in line and start_marker is None:
        # Check if this is the services grid (has "أنظمة إدارة" nearby)
        if i + 10 < len(lines) and 'أنظمة إدارة الشركات' in ''.join(lines[i:i+15]):
            start_marker = i

    if start_marker and '</div>' in line and 'grid-3' in lines[start_marker]:
        # Found the closing div - count divs to find the right one
        if i > start_marker + 50:  # Make sure we're past the services
            end_marker = i + 1
            break

if start_marker and end_marker:
    print(f"   Found services section: lines {start_marker+1} to {end_marker+1}")

    # Create dynamic services section
    dynamic_services = '''        <div class="grid-3" style="margin-top:18px">
          {% if services %}
            {% for service in services %}
          <div class="card {% if loop.index == 2 %}featured {% endif %}reveal">
            <div class="top">
              <div class="iconbox">{{ service.icon or 'SV' }}</div>
              <span class="pill">{% if loop.index == 2 %}Featured{% else %}Service{% endif %}</span>
            </div>
            <h4>{{ service.title }}</h4>
            <p>{{ service.description }}</p>
          </div>
            {% endfor %}
          {% else %}
            <!-- Fallback if no services -->
          <div class="card reveal">
            <div class="top">
              <div class="iconbox">SV</div>
              <span class="pill">Service</span>
            </div>
            <h4>خدماتنا</h4>
            <p>قم بإضافة الخدمات من لوحة التحكم</p>
          </div>
          {% endif %}
        </div>
'''

    # Replace the section
    new_lines = lines[:start_marker] + [dynamic_services] + lines[end_marker:]

    # Write back
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("   ✓ Services section is now dynamic!")
    print(f"   ✓ Replaced {end_marker - start_marker} lines with dynamic template")
else:
    print("   ⚠️  Could not find services section automatically")
    print("   Manual update needed")

print("\n✅ Done! The services section now pulls from the database.")
print("   Refresh the page to see changes!")
