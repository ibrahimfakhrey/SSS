"""
Make pricing and FAQ sections dynamic
"""

print("🔄 Making pricing and FAQ sections dynamic...")

# Read the index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# ========== PRICING SECTION ==========
print("  💰 Finding pricing section...")

pricing_start = None
pricing_end = None

for i, line in enumerate(lines):
    if 'id="pricing"' in line and pricing_start is None:
        pricing_start = i

    if pricing_start and i > pricing_start:
        # Find the grid-3 with pricing cards
        if '<div class="grid-3"' in line and 'margin-top:18px' in line:
            grid_start = i
            # Find the closing div for this grid
            for j in range(i+1, min(i+200, len(lines))):
                if '</div>' in lines[j] and j > grid_start + 40:  # Pricing section is large
                    pricing_end = j + 1
                    break
            if pricing_end:
                break

if pricing_start and pricing_end:
    print(f"    Found pricing: lines {pricing_start+1} to {pricing_end+1}")

    # Find exact grid start
    for i in range(pricing_start, pricing_end):
        if '<div class="grid-3"' in lines[i]:
            grid_start = i
            break

    # Create dynamic pricing
    dynamic_pricing = '''        <div class="grid-3" style="margin-top:18px">
          {% if pricing_plans %}
            {% for plan in pricing_plans %}
          <div class="card {% if plan.is_featured %}featured {% endif %}reveal">
            <div class="price-title">
              <h4 style="margin:0;font-family:'Cairo'">{{ plan.name }}</h4>
              <span class="pill">{{ plan.description }}</span>
            </div>
            <ul class="price-list">
              {% set features = plan.features|from_json %}
              {% for feature in features %}
              <li><span class="check">✓</span><span>{{ feature }}</span></li>
              {% endfor %}
            </ul>
            <div class="form-actions" style="margin-top:14px">
              <a class="btn" href="#contact">اطلب عرض</a>
            </div>
          </div>
            {% endfor %}
          {% endif %}
        </div>
'''

    lines = lines[:grid_start] + [dynamic_pricing] + lines[pricing_end:]
    print("    ✓ Pricing section is now dynamic!")
else:
    print("    ⚠️  Could not find pricing section")

# ========== FAQ SECTION ==========
print("  ❓ Finding FAQ section...")

faq_start = None
faq_end = None

for i, line in enumerate(lines):
    if 'id="faq"' in line and faq_start is None:
        faq_start = i

    if faq_start and i > faq_start:
        if '<div class="faq">' in line:
            faq_div_start = i
            # Find closing div for FAQ
            div_count = 1
            for j in range(i+1, min(i+100, len(lines))):
                if '<div' in lines[j]:
                    div_count += 1
                if '</div>' in lines[j]:
                    div_count -= 1
                    if div_count == 0:
                        faq_end = j + 1
                        break
            if faq_end:
                break

if faq_start and faq_end:
    print(f"    Found FAQ: lines {faq_start+1} to {faq_end+1}")

    # Find the faq div start
    for i in range(faq_start, faq_end):
        if '<div class="faq">' in lines[i]:
            faq_div_start = i
            break

    # Create dynamic FAQ
    dynamic_faq = '''        <div class="faq">
          {% if faqs %}
            {% for faq in faqs %}
          <details class="reveal">
            <summary>{{ faq.question }} <span class="chev">⌄</span></summary>
            <p>{{ faq.answer }}</p>
          </details>
            {% endfor %}
          {% else %}
          <details class="reveal">
            <summary>لا توجد أسئلة حالياً <span class="chev">⌄</span></summary>
            <p>قم بإضافة الأسئلة الشائعة من لوحة التحكم</p>
          </details>
          {% endif %}
        </div>
'''

    lines = lines[:faq_div_start] + [dynamic_faq] + lines[faq_end:]
    print("    ✓ FAQ section is now dynamic!")
else:
    print("    ⚠️  Could not find FAQ section")

# Write back
with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("\n✅ Pricing and FAQ are now dynamic!")
print("   Refresh the page to see database content!")
