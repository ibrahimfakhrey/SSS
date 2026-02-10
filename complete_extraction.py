"""
Complete extraction - Pricing, FAQ, Portfolio, and make everything dynamic
"""
from app import app, db, PricingPlan, FAQ, Portfolio
import json

def complete_extraction():
    with app.app_context():
        print("🚀 Completing full extraction...\n")

        # ========== EXTRACT PRICING PLANS ==========
        print("💰 Extracting pricing plans...")
        PricingPlan.query.delete()

        pricing_plans = [
            {
                'name': 'باقة الانطلاق',
                'price': 'حسب النطاق',
                'description': 'Starter',
                'features': json.dumps([
                    'حل تقني أساسي',
                    'منصة/نظام بسيط',
                    'مناسب للشركات الناشئة'
                ], ensure_ascii=False),
                'is_featured': False,
                'order': 1,
                'active': True
            },
            {
                'name': 'باقة الأعمال',
                'price': 'حسب المتطلبات',
                'description': 'Business',
                'features': json.dumps([
                    'منصة تفاعلية + لوحة تحكم',
                    'تقارير أساسية',
                    'دعم بعد التسليم'
                ], ensure_ascii=False),
                'is_featured': True,
                'order': 2,
                'active': True
            },
            {
                'name': 'باقة المؤسسات',
                'price': 'حسب الحجم',
                'description': 'Enterprise',
                'features': json.dumps([
                    'نظام مخصص بالكامل',
                    'تقارير متقدمة + أتمتة',
                    'قابلية توسع عالية'
                ], ensure_ascii=False),
                'is_featured': False,
                'order': 3,
                'active': True
            }
        ]

        for plan in pricing_plans:
            pricing = PricingPlan(**plan)
            db.session.add(pricing)

        print(f"   ✓ Added {len(pricing_plans)} pricing plans")

        # ========== EXTRACT FAQ ==========
        print("❓ Extracting FAQ items...")
        FAQ.query.delete()

        faqs = [
            {
                'question': 'هل تقدمون مواقع أم أنظمة؟',
                'answer': 'نحن نبني أنظمة ومنصات تشغيل للشركات (إدارة + متابعة + تقارير + صلاحيات) وليس مجرد مواقع شكلية.',
                'order': 1,
                'active': True
            },
            {
                'question': 'هل الحل يكون مخصصًا؟',
                'answer': 'نعم، كل نظام يُبنى حسب نشاط الشركة وطريقة التشغيل وحجم الفريق.',
                'order': 2,
                'active': True
            },
            {
                'question': 'هل النظام قابل للتوسع مستقبلاً؟',
                'answer': 'بالتأكيد. نضع النمو في الحسبان لإضافة مستخدمين وميزات وتقارير بدون كسر النظام.',
                'order': 3,
                'active': True
            },
            {
                'question': 'هل يوجد دعم بعد التسليم؟',
                'answer': 'نعم. نوفر دعمًا وتحسينات وتطويرًا مستمرًا حسب الاتفاق، كشريك تقني لا كمورد فقط.',
                'order': 4,
                'active': True
            },
            {
                'question': 'هل يمكن ربط النظام بأنظمة أخرى؟',
                'answer': 'نعم، حسب احتياجك: بريد/إشعارات/واجهات تكامل/أنظمة داخلية… إلخ.',
                'order': 5,
                'active': True
            },
            {
                'question': 'هل يمكن إضافة تقارير وذكاء اصطناعي؟',
                'answer': 'نعم، بحسب الهدف: فلترة، تصنيف، اقتراح قرارات، Chatbots داخلية، ولوحات KPIs.',
                'order': 6,
                'active': True
            }
        ]

        for faq in faqs:
            faq_item = FAQ(**faq)
            db.session.add(faq_item)

        print(f"   ✓ Added {len(faqs)} FAQ items")

        # Commit all
        db.session.commit()

        print("\n✅ Extraction complete!")
        print(f"\n📊 Database now has:")
        print(f"   • {PricingPlan.query.count()} pricing plans")
        print(f"   • {FAQ.query.count()} FAQ items")
        print(f"   • {Portfolio.query.count()} portfolio items")

if __name__ == '__main__':
    complete_extraction()
