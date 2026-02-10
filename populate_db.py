"""
Populate database with existing content from index.html
"""
from app import app, db, Section, Service, Portfolio, SiteSettings, ContactInfo
from werkzeug.security import generate_password_hash

def populate_database():
    with app.app_context():
        print("🔄 Populating database with existing content...")

        # Clear existing data (except user and settings)
        Section.query.delete()
        Service.query.delete()
        Portfolio.query.delete()

        # ========== SECTIONS ==========
        print("📄 Adding sections...")

        # Hero Section
        hero = Section(
            name='hero',
            title='3S Smart Software Solution',
            content='''حلول برمجية ذكية للشركات
نبني أنظمة تشغيل احترافية ومنصات ويب مخصصة للشركات في السعودية.
نحوّل فكرتك إلى منتج رقمي كامل، مع دعم مستمر بعد التسليم.''',
            section_type='hero',
            order=1,
            active=True
        )
        db.session.add(hero)

        # About Section
        about = Section(
            name='about',
            title='من نحن',
            content='''<strong>3S Smart Software Solution</strong> هو مزوّد حلول برمجية متخصّص في بناء أنظمة ومنصات تشغيل للشركات، وليس مجرد مواقع إلكترونية.
نبدأ دائمًا بفهم البزنس قبل كتابة أي سطر كود، لأن النظام الجيد هو الذي يخدم طريقة العمل، لا العكس.

نقدم منصات كاملة تشمل:
• <strong>أنظمة إدارة</strong> – لوحات تحكم + تقارير + تحليلات KPI
• <strong>تطبيقات جوال أصلية</strong> – iOS & Android Native
• <strong>واجهات ويب متقدمة</strong> – حسب احتياجك
• <strong>دعم بعد التسليم</strong> – تحديثات، صيانة، تطوير ميزات جديدة''',
            section_type='about',
            order=2,
            active=True
        )
        db.session.add(about)

        # Services Section
        services_section = Section(
            name='services',
            title='خدماتنا',
            content='نقدم حلول برمجية متكاملة ومخصصة',
            section_type='services',
            order=3,
            active=True
        )
        db.session.add(services_section)

        # Mobile Apps Section
        mobile_section = Section(
            name='mobile-apps',
            title='تطبيقات الجوال',
            content='نبني تطبيقات جوال احترافية باستخدام أحدث التقنيات',
            section_type='portfolio',
            order=4,
            active=True
        )
        db.session.add(mobile_section)

        # Pricing Section
        pricing_section = Section(
            name='pricing',
            title='الأسعار والباقات',
            content='اختر الباقة المناسبة لمشروعك',
            section_type='pricing',
            order=5,
            active=True
        )
        db.session.add(pricing_section)

        # FAQ Section
        faq_section = Section(
            name='faq',
            title='الأسئلة الشائعة',
            content='إجابات على أكثر الأسئلة شيوعًا',
            section_type='faq',
            order=6,
            active=True
        )
        db.session.add(faq_section)

        # Contact Section
        contact_section = Section(
            name='contact',
            title='تواصل معنا',
            content='نسعد بالتواصل معك ومناقشة مشروعك',
            section_type='contact',
            order=7,
            active=True
        )
        db.session.add(contact_section)

        # ========== SERVICES ==========
        print("🎯 Adding services...")

        services_data = [
            {
                'title': 'حلول مخصصة للبيزنس',
                'description': 'نبني أنظمة تشغيل كاملة ومنصات إدارة مخصصة حسب احتياجك – لوحات تحكم، تقارير، أتمتة عمليات.',
                'icon': '💼',
                'order': 1
            },
            {
                'title': 'نظام تشغيل',
                'description': 'نظام كامل يشمل: لوحة تحكم، تطبيق جوال، واجهات مستخدم، تقارير، وأتمتة عمليات البزنس.',
                'icon': '⚙️',
                'order': 2
            },
            {
                'title': 'حل مخصص',
                'description': 'نبني منصة أو تطبيق مخصص 100% حسب احتياجك – سواء ويب أو موبايل أو كلاهما.',
                'icon': '🎯',
                'order': 3
            },
            {
                'title': 'شراكة ودعم',
                'description': 'لا نسلّم المشروع ونختفي. نوفر دعم تقني مستمر، تحديثات، وتطوير ميزات جديدة حسب الطلب.',
                'icon': '🤝',
                'order': 4
            }
        ]

        for svc in services_data:
            service = Service(
                title=svc['title'],
                description=svc['description'],
                icon=svc['icon'],
                order=svc['order'],
                active=True
            )
            db.session.add(service)

        # ========== PORTFOLIO ==========
        print("💼 Adding portfolio items...")

        portfolio_data = [
            {
                'title': 'Hany Nutrition & Fitness',
                'description': 'تطبيق متكامل للتغذية واللياقة البدنية مع برامج تدريب مخصصة ومتابعة احترافية.',
                'image': 'assets/hany-fitness.webp',
                'order': 1
            },
            {
                'title': 'Kids International Academy',
                'description': 'أكاديمية تعليمية متطورة للأطفال مع برامج تعليمية تفاعلية ومحتوى تربوي متميز.',
                'image': 'assets/kia-academy.webp',
                'order': 2
            },
            {
                'title': 'IPI Drivers',
                'description': 'تطبيق السائقين الذكي لإدارة الرحلات والطلبات مع نظام متابعة متقدم.',
                'image': 'assets/drivers-ipi.webp',
                'order': 3
            },
            {
                'title': 'AlMoshtriyat',
                'description': 'منصة المشتريات الذكية - حلول متكاملة لإدارة المشتريات والموردين للشركات.',
                'image': 'assets/almoshtriyat.webp',
                'order': 4
            },
            {
                'title': 'IPI',
                'description': 'تطبيق IPI - منصة استثمار عقاري مبتكرة للتملك الجزئي مع عوائد شهرية.',
                'image': 'assets/ipi.webp',
                'order': 5
            },
            {
                'title': 'BARIQ Merchants',
                'description': 'تطبيق التجار من بارق - إدارة احترافية للمتاجر والطلبات مع تقارير مفصلة.',
                'image': 'assets/bariq-merchants.webp',
                'order': 6
            }
        ]

        for item in portfolio_data:
            portfolio = Portfolio(
                title=item['title'],
                description=item['description'],
                image=item['image'],
                order=item['order'],
                active=True
            )
            db.session.add(portfolio)

        # Commit all changes
        db.session.commit()

        print("✅ Database populated successfully!")
        print(f"   - {Section.query.count()} sections")
        print(f"   - {Service.query.count()} services")
        print(f"   - {Portfolio.query.count()} portfolio items")
        print("\n🎉 Ready! The database now has all your content!")

if __name__ == '__main__':
    populate_database()
