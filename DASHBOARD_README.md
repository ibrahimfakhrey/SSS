# 3S Smart Software Solution - Dashboard

## 🎉 Dashboard is Ready!

Your Flask dashboard is now running and ready to use!

## 🔐 Login Credentials

- **Username:** `shalaby`
- **Password:** `shalaby`

## 🌐 Access Points

- **Main Website:** http://127.0.0.1:5000/
- **Dashboard Login:** http://127.0.0.1:5000/login
- **Dashboard:** http://127.0.0.1:5000/dashboard (after login)

## 📋 Features

### 1. **General Settings** (`/dashboard/settings`)
   - ✏️ Edit site name, title, description
   - 🎨 Change colors (Primary & Secondary)
   - 🖼️ Upload logo and favicon
   - 💡 Preview colors in real-time

### 2. **Sections Management** (`/dashboard/sections`)
   - ➕ Add new sections dynamically
   - ✏️ Edit existing sections
   - 🗑️ Remove sections
   - 📑 Support for different section types:
     - Hero (البانر الرئيسي)
     - About (من نحن)
     - Features (المميزات)
     - Services (الخدمات)
     - Portfolio (المشاريع)
     - Pricing (الأسعار)
     - Testimonials (آراء العملاء)
     - FAQ (الأسئلة الشائعة)
     - Contact (التواصل)
     - Custom (مخصص)

### 3. **Services** (`/dashboard/services`)
   - ➕ Add services/features
   - 🎯 Add icons (emoji or icon class)
   - ✏️ Edit service details
   - 🗑️ Delete services

### 4. **Portfolio/Projects** (`/dashboard/portfolio`)
   - ➕ Add new projects
   - 📸 Upload project images
   - ✏️ Edit project details
   - 🗑️ Remove projects

### 5. **Contact Information** (`/dashboard/contact`)
   - 📞 Update phone number
   - 📧 Update email
   - 📍 Update address
   - 💬 Update WhatsApp number
   - 📱 Update social media links (Facebook, Twitter, LinkedIn, Instagram)

## 🚀 How to Run

### First Time Setup:
```bash
cd "/Users/ibrahim/Desktop/my projects/code_verse"
pip3 install -r requirements.txt
python3 app.py
```

### Daily Use:
```bash
cd "/Users/ibrahim/Desktop/my projects/code_verse"
python3 app.py
```

Then open your browser and go to:
- Main site: http://127.0.0.1:5000/
- Dashboard: http://127.0.0.1:5000/login

## 📁 File Structure

```
code_verse/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Public website (edit from dashboard)
│   └── dashboard/             # Dashboard templates
│       ├── login.html         # Login page
│       ├── base.html          # Dashboard layout
│       ├── dashboard.html     # Main dashboard
│       ├── settings.html      # Settings page
│       ├── sections.html      # Sections management
│       ├── services.html      # Services management
│       ├── portfolio.html     # Portfolio management
│       └── contact.html       # Contact info management
├── static/
│   ├── uploads/               # Uploaded images go here
│   └── assets/                # Original assets
└── instance/
    └── site.db                # SQLite database
```

## 💾 Database

The dashboard uses SQLite database stored at `instance/site.db`

### Default Data:
- **Admin User:** shalaby / shalaby
- **Site Colors:**
  - Primary: #060024 (dark blue)
  - Secondary: #0ed1ff (cyan)
- **Logo:** assets/3S Logo-07.png
- **WhatsApp:** 966532180937

## 🎨 Customization Tips

1. **Colors:**
   - Use HEX color codes (#xxxxxx)
   - Primary color is for backgrounds
   - Secondary color is for accents and buttons

2. **Images:**
   - Logo: PNG with transparent background (200x200px)
   - Favicon: PNG or ICO (32x32px or 64x64px)
   - Project images: PNG or WEBP (800x600px)

3. **Sections:**
   - Each section can have custom HTML content
   - Use the section type to organize your content
   - Toggle active/inactive to show/hide sections

4. **Icons:**
   - Use emoji for simple icons: 🎯 💼 🚀 ⚡ 🌟
   - Or use icon classes like: `fas fa-rocket`

## 🔒 Security Notes

⚠️ **Important:** This is a development server!

For production use:
1. Change the SECRET_KEY in app.py
2. Use a production WSGI server (gunicorn, uwsgi)
3. Use a proper database (PostgreSQL, MySQL)
4. Enable HTTPS
5. Add CSRF protection
6. Implement proper user management

## ❓ Troubleshooting

### App won't start:
```bash
# Make sure you're in the right directory
cd "/Users/ibrahim/Desktop/my projects/code_verse"

# Check if packages are installed
pip3 install -r requirements.txt

# Try again
python3 app.py
```

### Can't login:
- Username: `shalaby`
- Password: `shalaby`
- Make sure the database is initialized

### Changes not showing:
- Refresh the browser (Cmd+Shift+R)
- Check if the section is marked as "active"

## 📞 Support

If you need help, check:
1. The Flask app terminal output for errors
2. Browser console for JavaScript errors
3. Make sure all files are in the correct locations

---

**Built with ❤️ using Flask, SQLAlchemy, and modern web technologies**

**Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>**
