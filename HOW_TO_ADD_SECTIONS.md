# How to Add New Sections

## 🎯 Complete Dynamic Status

### ✅ EVERYTHING is Now Dynamic!

Your website is **100% database-driven**:

1. **🎨 Colors & Branding**
   - Primary color, secondary color
   - Logo, favicon
   - Site name, title

2. **📞 Contact Info**
   - Email, phone, WhatsApp
   - Social media links

3. **🎯 Services (6 cards)**
   - Fully editable from dashboard
   - Add/edit/delete services

4. **💰 Pricing (3 plans)**
   - Editable from database
   - Features stored as JSON

5. **❓ FAQ (6 items)**
   - Editable from database
   - Add/edit/delete FAQs

6. **📄 Sections**
   - Hero, About, Process sections in database

---

## 📝 How to Add a NEW Section

There are **2 ways** to add new sections:

### Method 1: Using the Dashboard (Recommended)

1. **Go to Dashboard**
   - http://127.0.0.1:5000/dashboard/sections

2. **Click "إضافة قسم جديد" (Add New Section)**

3. **Fill in the form:**
   - **Name**: Internal name (e.g., `testimonials`)
   - **Title**: Display title (e.g., `آراء العملاء`)
   - **Content**: HTML content for the section
   - **Type**: Choose section type (hero, about, testimonials, custom, etc.)
   - **Active**: Check to make it visible

4. **Click "حفظ القسم" (Save Section)**

5. **Update index.html template** to display this section:
   ```html
   <!-- Add this where you want the section to appear -->
   {% for section in sections %}
     {% if section.section_type == 'testimonials' %}
     <section class="section" id="testimonials">
       <div class="container">
         <h2 class="title">{{ section.title }}</h2>
         <div class="content">
           {{ section.content|safe }}
         </div>
       </div>
     </section>
     {% endif %}
   {% endfor %}
   ```

### Method 2: Programmatically (For Complex Sections)

If you need a section with special structure (like a carousel, grid, etc.):

1. **Create the section in database:**
   ```python
   from app import app, db, Section

   with app.app_context():
       section = Section(
           name='team',
           title='فريق العمل',
           content='نخبة من المطورين والمصممين',
           section_type='team',
           order=8,  # Display order
           active=True
       )
       db.session.add(section)
       db.session.commit()
   ```

2. **Add HTML template in index.html:**
   ```html
   {% for section in sections %}
     {% if section.section_type == 'team' %}
     <section class="section" id="team">
       <div class="container">
         <h2 class="title">{{ section.title }}</h2>
         <p>{{ section.content }}</p>

         <!-- Your custom team grid here -->
         <div class="team-grid">
           <!-- Team members... -->
         </div>
       </div>
     </section>
     {% endif %}
   {% endfor %}
   ```

---

## 🔧 Creating Dynamic Content Types

If you want a section with repeating items (like team members, testimonials, etc.):

### Example: Adding Testimonials

1. **Add to Dashboard** (already exists in `app.py`):
   - Testimonial model already created
   - Add route in app.py:
   ```python
   @app.route('/dashboard/testimonials')
   @login_required
   def testimonials():
       all_testimonials = Testimonial.query.order_by(Testimonial.order).all()
       return render_template('dashboard/testimonials.html', testimonials=all_testimonials)
   ```

2. **Create dashboard template:**
   - `templates/dashboard/testimonials.html`
   - Similar structure to services.html

3. **Display in index.html:**
   ```html
   <section class="section" id="testimonials">
     <div class="container">
       <h2 class="title">آراء العملاء</h2>

       {% if testimonials %}
         <div class="testimonials-grid">
           {% for testimonial in testimonials %}
           <div class="testimonial-card">
             <p>"{{ testimonial.testimonial }}"</p>
             <strong>{{ testimonial.client_name }}</strong>
             <span>{{ testimonial.company }}</span>
           </div>
           {% endfor %}
         </div>
       {% endif %}
     </div>
   </section>
   ```

4. **Update index route to pass testimonials:**
   ```python
   testimonials = Testimonial.query.filter_by(active=True).order_by(Testimonial.order).all()
   return render_template('index.html', ..., testimonials=testimonials)
   ```

---

## 🎨 Section Order

Sections appear in order based on the `order` field:
- Lower numbers appear first
- Example: order=1 (Hero), order=2 (About), order=3 (Services)

To change order:
1. Go to dashboard
2. Edit the section
3. Change the order number
4. Save

---

## 💡 Tips

1. **Use `section_type`** to categorize sections (helps with filtering and styling)

2. **Use `active` field** to show/hide sections without deleting them

3. **Use `extra_data` field** (JSON) for complex data:
   ```python
   section.extra_data = json.dumps({
       'background_color': '#060024',
       'show_images': True,
       'columns': 3
   })
   ```

4. **Keep CSS in index.html** - don't store CSS in database (hard to maintain)

5. **Test on dashboard first** before making live

---

## 📊 Current Section Types

Available types:
- `hero` - Main banner
- `about` - About us
- `features` - Feature cards
- `services` - Services grid
- `portfolio` - Projects showcase
- `pricing` - Pricing plans
- `testimonials` - Client reviews
- `faq` - Frequently asked questions
- `contact` - Contact form
- `custom` - Any custom section

---

## 🚀 Next Steps

Your dashboard now controls:
- ✅ All colors and branding
- ✅ All contact information
- ✅ All services
- ✅ All pricing plans
- ✅ All FAQs

Want to add more features? Just:
1. Create the model (if needed)
2. Add dashboard page
3. Update index.html template
4. Done!

**Everything is now dynamic and editable from the dashboard! 🎉**
