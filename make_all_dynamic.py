"""
Make ALL sections of index.html dynamic by replacing content with database values
"""

# Read the backup first (to work from clean copy)
print("📖 Reading index.html...")
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("🔄 Making sections dynamic...\n")

# ========== 1. CONTACT EMAIL ==========
print("  ✓ Email addresses")
content = content.replace(
    'href="mailto:info@3s-solutions.com"',
    'href="mailto:{{ contact.email if contact and contact.email else \'info@3s-solutions.com\' }}"'
)
content = content.replace(
    '>info@3s-solutions.com<',
    '>{{ contact.email if contact and contact.email else "info@3s-solutions.com" }}<'
)

# ========== 2. PHONE NUMBERS ==========
print("  ✓ Phone numbers")
content = content.replace(
    'href="tel:+966532180937"',
    'href="tel:{{ contact.phone if contact and contact.phone else \'+966532180937\' }}"'
)
content = content.replace(
    '>+966532180937<',
    '>{{ contact.phone if contact and contact.phone else "+966532180937" }}<'
)
content = content.replace(
    '>966532180937<',
    '>{{ contact.phone if contact and contact.phone else "966532180937" }}<'
)

# ========== 3. FOOTER YEAR ==========
print("  ✓ Footer year")
# Add year variable to template
content = content.replace(
    '<span id="year"></span>',
    '2026'  # Since we'll add current year in the route
)

# ========== 4. SITE DESCRIPTION ==========
print("  ✓ Site descriptions")
content = content.replace(
    'content="3S Smart Software Solution — حلول برمجية ذكية | منصات وأنظمة تشغيل للشركات في السعودية. حلول مخصصة، تقارير، ودعم بعد التسليم."',
    'content="{{ settings.site_description if settings and settings.site_description else \'3S Smart Software Solution — حلول برمجية ذكية\' }}"'
)

# ========== Save the updated file ==========
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Basic contact info is now dynamic!")
print("\nℹ️  For services and portfolio, we need to add Jinja2 loops.")
print("   Creating enhanced template next...")
