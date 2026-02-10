"""
3S Smart Software Solution - Dashboard App
Flask application with admin dashboard to customize the website
"""
from flask import Flask, render_template, redirect, url_for, flash, request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Add custom Jinja2 filter for JSON parsing
@app.template_filter('from_json')
def from_json_filter(s):
    """Parse JSON string"""
    if s:
        return json.loads(s)
    return []

# ============= DATABASE MODELS =============

class User(UserMixin, db.Model):
    """Admin user model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SiteSettings(db.Model):
    """Global site settings - colors, logo, etc."""
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(200), default='3S Smart Software Solution')
    site_title = db.Column(db.String(200), default='3S — Smart Software Solution')
    site_description = db.Column(db.Text, default='حلول برمجية ذكية للشركات')
    primary_color = db.Column(db.String(7), default='#060024')
    secondary_color = db.Column(db.String(7), default='#0ed1ff')
    text_color = db.Column(db.String(7), default='#ffffff')
    logo = db.Column(db.String(200), default='assets/3S Logo-07.png')
    favicon = db.Column(db.String(200), default='assets/3S Logo-07.png')
    keywords = db.Column(db.Text)
    author = db.Column(db.String(100))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Section(db.Model):
    """Dynamic sections for the website"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    section_type = db.Column(db.String(50))
    order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    extra_data = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Service(db.Model):
    """Services/Features"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    image = db.Column(db.String(200))
    order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Portfolio(db.Model):
    """Portfolio/Projects"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    url = db.Column(db.String(300))
    app_store_url = db.Column(db.String(300))
    play_store_url = db.Column(db.String(300))
    order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    tags = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PricingPlan(db.Model):
    """Pricing plans"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(50))
    description = db.Column(db.Text)
    features = db.Column(db.Text)
    is_featured = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ContactInfo(db.Model):
    """Contact information"""
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    address = db.Column(db.Text)
    whatsapp = db.Column(db.String(50))
    facebook = db.Column(db.String(200))
    twitter = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    instagram = db.Column(db.String(200))
    youtube = db.Column(db.String(200))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class FAQ(db.Model):
    """Frequently Asked Questions"""
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Testimonial(db.Model):
    """Client testimonials"""
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100))
    testimonial = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
    rating = db.Column(db.Integer, default=5)
    order = db.Column(db.Integer, default=0)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ============= PUBLIC ROUTES =============

@app.route('/')
def index():
    """Main public website"""
    settings = SiteSettings.query.first()
    sections = Section.query.order_by(Section.order).all()
    services = Service.query.filter_by(active=True).order_by(Service.order).all()
    portfolio = Portfolio.query.filter_by(active=True).order_by(Portfolio.order).all()
    pricing_plans = PricingPlan.query.filter_by(active=True).order_by(PricingPlan.order).all()
    faqs = FAQ.query.filter_by(active=True).order_by(FAQ.order).all()
    contact = ContactInfo.query.first()

    return render_template('index.html',
                         settings=settings,
                         sections=sections,
                         services=services,
                         portfolio=portfolio,
                         pricing_plans=pricing_plans,
                         faqs=faqs,
                         contact=contact)

@app.route('/test-db')
def test_db():
    """Test page to show database content"""
    settings = SiteSettings.query.first()
    sections = Section.query.order_by(Section.order).all()
    services = Service.query.filter_by(active=True).order_by(Service.order).all()
    portfolio = Portfolio.query.filter_by(active=True).order_by(Portfolio.order).all()
    contact = ContactInfo.query.first()

    return render_template('test_db.html',
                         settings=settings,
                         sections=sections,
                         services=services,
                         portfolio=portfolio,
                         contact=contact)

# ============= AUTH ROUTES =============

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Admin login"""
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('dashboard/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# ============= DASHBOARD ROUTES =============

@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard overview"""
    settings = SiteSettings.query.first()
    sections_count = Section.query.count()
    services_count = Service.query.count()
    portfolio_count = Portfolio.query.count()

    return render_template('dashboard/dashboard.html',
                         settings=settings,
                         sections_count=sections_count,
                         services_count=services_count,
                         portfolio_count=portfolio_count)

@app.route('/dashboard/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """Site settings - colors, logo, general settings"""
    site_settings = SiteSettings.query.first()

    if request.method == 'POST':
        # Update settings
        site_settings.site_name = request.form.get('site_name')
        site_settings.site_title = request.form.get('site_title')
        site_settings.site_description = request.form.get('site_description')
        site_settings.primary_color = request.form.get('primary_color')
        site_settings.secondary_color = request.form.get('secondary_color')
        site_settings.text_color = request.form.get('text_color')

        # Handle logo upload
        if 'logo' in request.files:
            file = request.files['logo']
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                site_settings.logo = f'uploads/{filename}'

        # Handle favicon upload
        if 'favicon' in request.files:
            file = request.files['favicon']
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                site_settings.favicon = f'uploads/{filename}'

        db.session.commit()
        flash('Settings updated successfully!', 'success')
        return redirect(url_for('settings'))

    return render_template('dashboard/settings.html', settings=site_settings)

@app.route('/dashboard/sections', methods=['GET'])
@login_required
def sections():
    """Manage sections"""
    all_sections = Section.query.order_by(Section.order).all()
    return render_template('dashboard/sections.html', sections=all_sections)

@app.route('/dashboard/sections/add', methods=['POST'])
@login_required
def add_section():
    """Add new section"""
    section = Section(
        name=request.form.get('name'),
        title=request.form.get('title'),
        content=request.form.get('content'),
        section_type=request.form.get('section_type'),
        order=Section.query.count() + 1,
        active=True
    )
    db.session.add(section)
    db.session.commit()
    flash('Section added successfully!', 'success')
    return redirect(url_for('sections'))

@app.route('/dashboard/sections/edit/<int:id>', methods=['POST'])
@login_required
def edit_section(id):
    """Edit section"""
    section = Section.query.get_or_404(id)
    section.name = request.form.get('name')
    section.title = request.form.get('title')
    section.content = request.form.get('content')
    section.section_type = request.form.get('section_type')
    section.active = request.form.get('active') == 'on'
    db.session.commit()
    flash('Section updated successfully!', 'success')
    return redirect(url_for('sections'))

@app.route('/dashboard/sections/delete/<int:id>')
@login_required
def delete_section(id):
    """Delete section"""
    section = Section.query.get_or_404(id)
    db.session.delete(section)
    db.session.commit()
    flash('Section deleted successfully!', 'success')
    return redirect(url_for('sections'))

@app.route('/dashboard/services', methods=['GET', 'POST'])
@login_required
def services():
    """Manage services"""
    if request.method == 'POST':
        service = Service(
            title=request.form.get('title'),
            description=request.form.get('description'),
            icon=request.form.get('icon'),
            order=Service.query.count() + 1,
            active=True
        )
        db.session.add(service)
        db.session.commit()
        flash('Service added successfully!', 'success')
        return redirect(url_for('services'))

    all_services = Service.query.order_by(Service.order).all()
    return render_template('dashboard/services.html', services=all_services)

@app.route('/dashboard/portfolio', methods=['GET', 'POST'])
@login_required
def portfolio():
    """Manage portfolio"""
    if request.method == 'POST':
        portfolio_item = Portfolio(
            title=request.form.get('title'),
            description=request.form.get('description'),
            order=Portfolio.query.count() + 1,
            active=True
        )

        # Handle image upload
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename:
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                portfolio_item.image = f'uploads/{filename}'

        db.session.add(portfolio_item)
        db.session.commit()
        flash('Portfolio item added successfully!', 'success')
        return redirect(url_for('portfolio'))

    all_portfolio = Portfolio.query.order_by(Portfolio.order).all()
    return render_template('dashboard/portfolio.html', portfolio=all_portfolio)

@app.route('/dashboard/contact', methods=['GET', 'POST'])
@login_required
def contact():
    """Manage contact information"""
    contact_info = ContactInfo.query.first()

    if request.method == 'POST':
        contact_info.phone = request.form.get('phone')
        contact_info.email = request.form.get('email')
        contact_info.address = request.form.get('address')
        contact_info.whatsapp = request.form.get('whatsapp')
        contact_info.facebook = request.form.get('facebook')
        contact_info.twitter = request.form.get('twitter')
        contact_info.linkedin = request.form.get('linkedin')
        contact_info.instagram = request.form.get('instagram')

        db.session.commit()
        flash('Contact information updated successfully!', 'success')
        return redirect(url_for('contact'))

    return render_template('dashboard/contact.html', contact=contact_info)

# ============= API ROUTES =============

@app.route('/api/upload-image', methods=['POST'])
@login_required
def upload_image():
    """Handle image uploads via AJAX"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'success': True, 'path': f'uploads/{filename}'}), 200

# ============= INIT DATABASE =============

def init_db():
    """Initialize database with default data"""
    with app.app_context():
        db.create_all()

        # Create admin user if not exists
        if not User.query.filter_by(username='shalaby').first():
            admin = User(
                username='shalaby',
                password=generate_password_hash('shalaby', method='pbkdf2:sha256')
            )
            db.session.add(admin)

        # Create default settings if not exists
        if not SiteSettings.query.first():
            settings = SiteSettings(
                site_name='3S Smart Software Solution',
                site_title='3S — Smart Software Solution',
                site_description='حلول برمجية ذكية للشركات',
                primary_color='#060024',
                secondary_color='#0ed1ff',
                logo='assets/3S Logo-07.png',
                favicon='assets/3S Logo-07.png'
            )
            db.session.add(settings)

        # Create default contact info if not exists
        if not ContactInfo.query.first():
            contact = ContactInfo(
                phone='966532180937',
                whatsapp='966532180937',
                email='info@3s-solutions.com'
            )
            db.session.add(contact)

        db.session.commit()
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
