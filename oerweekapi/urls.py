from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.urls import path

from web import views

from django.views.generic.base import RedirectView

from rest_framework import routers
import rest_framework_jwt.views

from web.views import (
    PageViewSet,
    ResourceViewSet,
    EventViewSet,
    EventSummaryView,
    ExportResources,
    ResourceImageViewSet,
    SubmissionViewSet,
    TwitterSearchResults,
    EmailTemplateView,
    RequestAccessView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"pages", PageViewSet, basename="Page")
router.register(r"resource", ResourceViewSet, basename="Resource")
router.register(r"resource-image", ResourceImageViewSet, basename="ResourceImage")
router.register(r"event", EventViewSet, basename="Event")
router.register(r"submission", SubmissionViewSet, basename="Submission")
router.register(r"email-templates", EmailTemplateView)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    # url(r'^api/submission/', SubmissionView.as_view()),
    url(r"^api/events-summary/", EventSummaryView.as_view()),
    url(r"^api/twitter/", TwitterSearchResults.as_view()),
    url(r"^api/request-access/", RequestAccessView.as_view()),
    url(r"^admin/", admin.site.urls),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^api-token-auth/", rest_framework_jwt.views.obtain_jwt_token),
    url(r"^api-token-refresh/", rest_framework_jwt.views.refresh_jwt_token),
    url(r"^export/resources/$", ExportResources.as_view(), name="resource_export"),

    url(r'^$', views.index, name='web_index'),
    # url(r'^$', RedirectView.as_view(url='https://www.oeglobal.org/activities/open-education-week/', permanent=False), name='root_redirect'),

    # url(r'^page/what-is-open-education-week/$', views.page__what_is_open_education_week),
    # url(r'^page/faq/$', views.page__faq),
    # url(r'^page/contribute/$', views.page__contribute),
    url(r'^submit$', RedirectView.as_view(url='/contribute/', permanent=False)),
    url(r'^submit/$', RedirectView.as_view(url='/contribute/', permanent=False)),
    url(r'^submit-activity$', RedirectView.as_view(url='/contribute-activity/', permanent=False)),
    url(r'^submit-activity/$', RedirectView.as_view(url='/contribute-activity/', permanent=False)),
    url(r'^submit-asset$', RedirectView.as_view(url='/contribute-asset/', permanent=False)),
    url(r'^submit-asset/$', RedirectView.as_view(url='/contribute-asset/', permanent=False)),

    url(r'^contribute$', RedirectView.as_view(url='/contribute/', permanent=False)),
    url(r'^contribute-activity$', RedirectView.as_view(url='/contribute-activity/', permanent=False)),
    url(r'^contribute-asset$', RedirectView.as_view(url='/contribute-asset/', permanent=False)),
    # 2022-04-05 -- replaced contribute links with redirects
    # url(r'^contribute/$', views.contribute),
    # url(r'^contribute-activity/$', views.contribute_activity),
    # url(r'^contribute-asset/$', views.contribute_asset),
    url(r'^contribute/$', RedirectView.as_view(url='/', permanent=False)),
    url(r'^contribute-activity/$', RedirectView.as_view(url='/', permanent=False)),
    url(r'^contribute-asset/$', RedirectView.as_view(url='/', permanent=False)),

    path('edit/<uuid:identifier>/', views.edit_resource),
    # OLD: url(r'^edit/$', views.edit_resource),
    # url(r'^page/materials/$', views.page__materials),
    url(r'^thanks/$', views.thanks),

    url(r'^schedule$', RedirectView.as_view(url='/events/', permanent=False)),
    url(r'^schedule/$', RedirectView.as_view(url='/events/', permanent=False)),
    url(r'^events$', RedirectView.as_view(url='/events/', permanent=False)),
    url(r'^events/$', views.show_events),
    url(r'^resources$', RedirectView.as_view(url='/resources/', permanent=False)),
    url(r'^resources/$', views.show_resources),
    path('events/<int:year>/<str:slug>/', views.show_event_detail),
    path('resources/<int:year>/<str:slug>/', views.show_resource_detail),

    # url(r'^page/home/$', views.index, name='web_index'),
] \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

