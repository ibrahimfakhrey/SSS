"""
Make index.html dynamic by replacing hardcoded content with Jinja2 variables
"""

# Read the current index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔄 Making index.html dynamic...")

# 1. Replace CSS color variables
print("  📝 Updating CSS colors...")
content = content.replace(
    "      --bg: #060024;",
    "      --bg: {{ settings.primary_color if settings else '#060024' }};"
)
content = content.replace(
    "      --bg2:#060024;",
    "      --bg2:{{ settings.primary_color if settings else '#060024' }};"
)
content = content.replace(
    "      --cyan:#0ed1ff;",
    "      --cyan:{{ settings.secondary_color if settings else '#0ed1ff' }};"
)

# 2. Replace meta tags
print("  📝 Updating meta tags...")
content = content.replace(
    '<title>3S — Smart Software Solution</title>',
    '<title>{{ settings.site_title if settings else "3S — Smart Software Solution" }}</title>'
)
content = content.replace(
    'content="#060024" />',
    'content="{{ settings.primary_color if settings else \'#060024\' }}" />'
)

# 3. Replace logo references
print("  📝 Updating logo...")
content = content.replace(
    'href="assets/3S Logo-07.png"',
    'href="{{ settings.logo if settings else \'assets/3S Logo-07.png\' }}"'
)
content = content.replace(
    'src="assets/3S Logo-07.png"',
    'src="{{ settings.logo if settings else \'assets/3S Logo-07.png\' }}"'
)

# 4. Replace WhatsApp number
print("  📝 Updating WhatsApp...")
content = content.replace(
    'https://wa.me/966532180937',
    'https://wa.me/{{ contact.whatsapp if contact else "966532180937" }}'
)

# 5. Update header brand name
print("  📝 Updating site name...")
content = content.replace(
    '<strong style="font-size:16px; color: var(--cyan);">Smart Software Solution</strong>',
    '<strong style="font-size:16px; color: var(--cyan);">{{ settings.site_name if settings else "Smart Software Solution" }}</strong>'
)

# Write the updated content
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Index.html is now dynamic!")
print("\n📋 Changes made:")
print("  ✓ CSS colors use database values")
print("  ✓ Logo uses database value")
print("  ✓ Meta tags use database values")
print("  ✓ WhatsApp number uses database value")
print("  ✓ Site name uses database value")
print("\n🎉 Done! Refresh the page to see changes from the database!")
