from django.conf.urls import include, url
from .views import (
    CreateLogframe, EditLogframe, ManageLogframes, ResultEditor, ResultMonitor
)

logframe_management_patterns = [
    url(r'^create/', CreateLogframe.as_view(), name='create-logframe'),
    url(r'^manage/', ManageLogframes.as_view(), name='manage-logframes'),
    url(r'^update/(?P<pk>\d+)/$', EditLogframe.as_view(), name='update-logframe'),
]

urlpatterns = [
    url(r'^design/(?P<logframe_id>\d+)/result/(?P<pk>\d+)/$',
        ResultEditor.as_view(),
        name="design-result"),
    url(r'^monitor/(?P<logframe_id>\d+)/result/(?P<pk>\d+)/$',
        ResultMonitor.as_view(),
        name="monitor-result"),
    url('^logframes/', include(logframe_management_patterns))
]
