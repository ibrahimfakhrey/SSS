"""
Make sections display automatically - no manual HTML editing needed
Add this universal section renderer to index.html
"""

print("🔄 Adding automatic section display...")

# Read index.html
with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to insert (before the contact form section)
# Look for the contact section
contact_marker = '<!-- Contact -->'

if contact_marker in content:
    # Create universal section renderer
    universal_renderer = '''
  <!-- ========== DYNAMIC SECTIONS - Auto Display ========== -->
  <!-- All sections added from dashboard will appear here automatically -->
  {% if sections %}
    {% for section in sections %}
      {% if section.active and section.section_type not in ['hero', 'about', 'services', 'pricing', 'faq'] %}

      <!-- Section: {{ section.name }} -->
      <section class="section {% if section.section_type == 'cta' %}compact{% endif %}"
               id="{{ section.name }}"
               {% if section.section_type == 'cta' %}style="background: linear-gradient(135deg, rgba(14,209,255,.15), rgba(14,209,255,.05))"{% endif %}>
        <div class="container">

          {% if section.section_type == 'cta' %}
          <!-- Call to Action Style -->
          <div class="card reveal" style="text-align:center; padding:60px 40px; background:rgba(14,209,255,.08); border:2px solid rgba(14,209,255,.3)">
            <h2 class="title" style="margin-bottom:15px">{{ section.title }}</h2>
            <div style="font-size:18px; color:rgba(234,240,255,.85); margin-bottom:30px">
              {{ section.content|safe }}
            </div>
            <div class="form-actions" style="justify-content:center">
              <a href="#contact" class="btn" style="padding:15px 40px; font-size:18px">تواصل معنا الآن</a>
            </div>
          </div>

          {% elif section.section_type == 'testimonials' %}
          <!-- Testimonials Style -->
          <div class="reveal">
            <h2 class="title">{{ section.title }}</h2>
            <p class="subtitle">{{ section.content|safe }}</p>
          </div>

          {% elif section.section_type == 'stats' %}
          <!-- Stats Style -->
          <div class="reveal">
            <h2 class="title">{{ section.title }}</h2>
          </div>
          <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:20px; margin-top:24px">
            <div class="reveal" style="text-align:center; padding:30px; background:rgba(14,209,255,.05); border:1px solid rgba(14,209,255,.2); border-radius:15px">
              {{ section.content|safe }}
            </div>
          </div>

          {% else %}
          <!-- Default Style -->
          <div class="reveal">
            <h2 class="title">{{ section.title }}</h2>
            <div class="subtitle" style="margin-top:18px">
              {{ section.content|safe }}
            </div>
          </div>

          {% endif %}

        </div>
      </section>

      {% endif %}
    {% endfor %}
  {% endif %}
  <!-- ========== END DYNAMIC SECTIONS ========== -->

  '''

    # Insert before contact section
    content = content.replace(contact_marker, universal_renderer + '\n' + contact_marker)

    # Write back
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Success! Sections now display automatically!")
    print("\n📋 What this means:")
    print("   • Add section in dashboard → Appears on website instantly!")
    print("   • Edit section → Updates on website")
    print("   • Delete section → Removes from website")
    print("   • Toggle active/inactive → Show/hide section")
    print("\n🎯 No more HTML editing needed!")
else:
    print("⚠️  Could not find contact section marker")
    print("   Will add at the end instead...")

    # Add before </main> tag
    if '</main>' in content:
        content = content.replace('</main>', universal_renderer + '\n</main>')
        with open('templates/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Added at end of main content!")
