from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('templates', views.TemplateViewSet, basename='template')
router.register('documents', views.DocumentViewSet, basename='document')

urlpatterns = [
    # HTML pages
    path('', views.home, name='home'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
    path('templates/', views.all_templates_view, name='all_templates'),
    path('template/<int:template_id>/clone/', views.template_clone_view, name='template_clone'),
    path('category/<str:category>/', views.category_view, name='category'),
    path('editor/<int:template_id>/', views.editor_view, name='editor'),
    path('documents/', views.documents_view, name='documents'),
    path('about/', views.about_view, name='about'),
    path('features/', views.features_view, name='features'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'),
    path('compare/', views.compare_view, name='compare'),
    path('compare-templates/<str:category>/', views.compare_templates_view, name='compare_templates'),

    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('brand-kit/', views.brand_kit_view, name='brand_kit'),
    path('api/brand-kit/', views.brand_kit_api, name='brand_kit_api'),

    # Mock payment
    path('checkout/<str:plan>/', views.checkout_view, name='checkout'),

    # Public share
    path('share/<str:token>/', views.share_doc_view, name='share_doc'),
    path('api/doc/<int:doc_id>/share/', views.make_doc_public, name='make_public'),

    # Analytics
    path('analytics/', views.analytics_view, name='analytics'),

    # AI Template Generator
    path('ai-template/', views.ai_template_view, name='ai_template'),
    path('api/ai/template/', views.ai_generate_template, name='ai_generate_template'),

    # Bulk export
    path('bulk-export/', views.bulk_export_view, name='bulk_export'),

    # API
    path('api/', include(router.urls)),
    path('api/ai/enhance/', views.ai_enhance, name='ai_enhance'),
    path('api/ai/translate/', views.ai_translate, name='ai_translate'),
    path('api/ai/image/', views.ai_image, name='ai_image'),
    path('api/check-download/', views.check_download, name='check_download'),
]
