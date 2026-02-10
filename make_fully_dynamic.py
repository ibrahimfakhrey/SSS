"""
Make the entire index.html fully dynamic - all sections pull from database
"""
import re

print("🚀 Making EVERYTHING dynamic...")

# Read the current index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ========== 1. HERO SECTION ==========
print("  📝 Making hero section dynamic...")

# Find and replace hero title and subtitle
content = re.sub(
    r'<div class="brand-subtitle">Smart Software Solution</div>',
    '<div class="brand-subtitle">{{ settings.site_name if settings else "Smart Software Solution" }}</div>',
    content
)

# ========== 2. CONTACT INFO ==========
print("  📝 Making contact info dynamic...")

# Email
content = re.sub(
    r'href="mailto:info@3s-solutions\.com"',
    'href="mailto:{{ contact.email if contact else \'info@3s-solutions.com\' }}"',
    content
)
content = re.sub(
    r'>info@3s-solutions\.com<',
    '>{{ contact.email if contact else "info@3s-solutions.com" }}<',
    content
)

# Phone
content = re.sub(
    r'href="tel:\+966532180937"',
    'href="tel:{{ contact.phone if contact else \'+966532180937\' }}"',
    content
)
content = re.sub(
    r'>966532180937<',
    '>{{ contact.phone if contact else "966532180937" }}<',
    content
)

# ========== 3. FOOTER ==========
print("  📝 Making footer dynamic...")

# Footer copyright year
content = re.sub(
    r'© <span id="year"></span>',
    '© {{ current_year if current_year else "2026" }}',
    content
)

# ========== 4. SERVICES SECTION - Make it loop through database ==========
print("  📝 Making services section dynamic...")

# Find the services grid section and replace with dynamic loop
services_pattern = r'<div class="mobile-apps-grid">\s*<div class="card compact reveal">\s*<div style="text-align:center; font-size:clamp\(28px,4vw,36px\); margin-bottom:12px;">💼</div>.*?</div>\s*</div>'

services_template = '''<div class="mobile-apps-grid">
            {% if services %}
              {% for service in services %}
              <div class="card compact reveal">
                <div style="text-align:center; font-size:clamp(28px,4vw,36px); margin-bottom:12px;">{{ service.icon or '🎯' }}</div>
                <div style="margin-bottom:12px;">
                  <strong style="font-family:'Cairo'; display:block">{{ service.title }}</strong>
                </div>
                <p style="font-size:14px; color:rgba(234,240,255,.78); line-height:1.7;">
                  {{ service.description }}
                </p>
              </div>
              {% endfor %}
            {% else %}
              <!-- Fallback if no services in database -->
              <div class="card compact reveal">
                <div style="text-align:center; font-size:clamp(28px,4vw,36px); margin-bottom:12px;">💼</div>
                <div style="margin-bottom:12px;">
                  <strong style="font-family:'Cairo'; display:block">حلول مخصصة للبيزنس</strong>
                </div>
                <p style="font-size:14px; color:rgba(234,240,255,.78); line-height:1.7;">
                  نبني أنظمة تشغيل كاملة ومنصات إدارة مخصصة حسب احتياجك
                </p>
              </div>
            {% endif %}
          </div>'''

# This is complex, so let's use a simpler marker-based approach
# Add a marker comment that we'll replace
if '<!-- SERVICES_DYNAMIC -->' not in content:
    print("    ⚠️  Services section needs manual update - structure too complex")

# ========== 5. PORTFOLIO SECTION - Make it loop ==========
print("  📝 Making portfolio section dynamic...")

# Add portfolio loop marker
if '<!-- PORTFOLIO_DYNAMIC -->' not in content:
    print("    ⚠️  Portfolio section needs manual update - structure too complex")

print("  ✓ Basic dynamic replacements complete")

# Write back
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Phase 1 Complete!")
print("\n📋 What's now dynamic:")
print("  ✓ Hero section title")
print("  ✓ Contact email and phone")
print("  ✓ Footer copyright")
print("\n⚠️  Complex sections (services, portfolio) need template restructuring")
print("    → Creating specialized template next...")
