"""
Full extraction - Extract ALL content from HTML and populate database
"""
from app import app, db, Service, Portfolio, Section

def full_extraction():
    with app.app_context():
        print("🔄 Starting FULL extraction from HTML...\n")

        # ========== CLEAR EXISTING DATA ==========
        print("🗑️  Clearing existing services...")
        Service.query.delete()

        # ========== EXTRACT SERVICES ==========
        print("🎯 Extracting 6 services from HTML...")

        services_data = [
            {
                'title': 'أنظمة إدارة الشركات',
                'description': 'CRM، إدارة المبيعات والطلبات، سير العمل، المهام والموافقات. النتيجة: تنظيم · تتبع · تقارير · تحكم',
                'icon': 'BS',
                'order': 1,
                'active': True
            },
            {
                'title': 'أنظمة مخصصة حسب النشاط',
                'description': 'نظام يُبنى على طبيعة تشغيل شركتك، لا على قالب جاهز. مناسب لـ: المقاولات · معاهد التدريب · B2B · الإدارات الداخلية',
                'icon': 'CS',
                'order': 2,
                'active': True
            },
            {
                'title': 'منصات ويب احترافية',
                'description': 'بوابات عملاء/موردين، تسجيل ودخول، لوحات تحكم، صلاحيات. النتيجة: تجربة احترافية + إدارة واضحة',
                'icon': 'WP',
                'order': 3,
                'active': True
            },
            {
                'title': 'التقارير والتحليل',
                'description': 'Dashboards، KPIs، تقارير تشغيلية، تصدير بيانات. لغة المديرين وأصحاب القرار',
                'icon': 'BI',
                'order': 4,
                'active': True
            },
            {
                'title': 'الأتمتة وربط الأنظمة',
                'description': 'تقليل العمل اليدوي، ربط الأنظمة، إشعارات تلقائية، عمليات بدون تدخل. النتيجة: وقت أقل · أخطاء أقل · إنتاجية أعلى',
                'icon': 'AU',
                'order': 5,
                'active': True
            },
            {
                'title': 'حلول مدعومة بالذكاء الاصطناعي',
                'description': 'فلترة طلبات، تصنيف بيانات، اقتراح قرارات، Chatbots داخلية. النتيجة: تشغيل أذكى وقرارات أسرع',
                'icon': 'AI',
                'order': 6,
                'active': True
            }
        ]

        for svc in services_data:
            service = Service(**svc)
            db.session.add(service)

        print(f"   ✓ Added {len(services_data)} services")

        # ========== EXTRACT ABOUT SECTION ==========
        print("📋 Extracting About section...")

        about_content = '''<strong style="background: linear-gradient(135deg, var(--gold), var(--gold-light)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">3S Smart Software Solution</strong> هو مزوّد حلول برمجية متخصّص في بناء أنظمة ومنصات تشغيل للشركات، وليس مجرد مواقع إلكترونية.
نبدأ دائمًا بفهم البزنس قبل كتابة أي سطر كود، لأن النظام الجيد هو الذي يخدم طريقة العمل، لا العكس.'''

        # Update or create about section
        about = Section.query.filter_by(section_type='about').first()
        if about:
            about.content = about_content
        else:
            about = Section(
                name='about',
                title='من نحن',
                content=about_content,
                section_type='about',
                order=2,
                active=True
            )
            db.session.add(about)

        print("   ✓ About section updated")

        # ========== EXTRACT PROCESS STEPS ==========
        print("🔄 Extracting Process section...")

        process_content = '''منهجية واضحة تساعدك على تحويل المتطلبات إلى نظام قابل للتشغيل والتوسع، مع توثيق وتسليم ودعم مستمر.

1. فهم وتشخيص التشغيل الحالي - نحدد طريقة العمل اليومية ونقاط الهدر والأولويات
2. تحليل المتطلبات وتحديد النطاق - تحديد ما يجب بناؤه الآن وما يؤجل للمرحلة التالية
3. تصميم تجربة المستخدم والهيكلة - رسم الشاشات والأدوار والصلاحيات
4. بناء النظام باستخدام أحدث التقنيات - كود نظيف وبنية قابلة للتوسع
5. اختبار شامل قبل التسليم - Unit Tests + Integration + UAT
6. نشر وتشغيل على البيئة الحقيقية - تدريب الفريق والدعم المستمر'''

        process = Section.query.filter_by(section_type='process').first()
        if not process:
            process = Section(
                name='process',
                title='كيف نعمل؟',
                content=process_content,
                section_type='process',
                order=4,
                active=True
            )
            db.session.add(process)

        print("   ✓ Process section added")

        # Commit all changes
        db.session.commit()

        print("\n✅ Full extraction complete!")
        print(f"\n📊 Database now has:")
        print(f"   • {Service.query.count()} services")
        print(f"   • {Portfolio.query.count()} portfolio items")
        print(f"   • {Section.query.count()} sections")

if __name__ == '__main__':
    full_extraction()
