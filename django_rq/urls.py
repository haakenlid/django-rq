from django.urls import include, re_path

from . import views

detail_routes = [
    re_path('^$', views.job_detail, name='rq_job_detail'),
    re_path(r'^/delete/$', views.delete_job, name='rq_delete_job'),
    re_path(r'^/requeue/$', views.requeue_job_view, name='rq_requeue_job'),
    re_path(r'^/enqueue/$', views.enqueue_job_view, name='rq_enqueue_job'),
]

urlpatterns = [
    re_path(r'^$',
            views.stats, name='rq_home'),
    re_path(r'^stats.json/(?P<token>[\w]+)?/?$',
            views.stats_json, name='rq_home_json'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/$',
            views.jobs, name='rq_jobs'),
    re_path(r'^workers/(?P<queue_index>[\d]+)/$',
            views.workers, name='rq_workers'),
    re_path(r'^workers/(?P<queue_index>[\d]+)/(?P<key>[-\w\.\:\$]+)/$',
            views.worker_details, name='rq_worker_details'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/finished/$',
            views.finished_jobs, name='rq_finished_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/failed/$',
            views.failed_jobs, name='rq_failed_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/scheduled/$',
            views.scheduled_jobs, name='rq_scheduled_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/started/$',
            views.started_jobs, name='rq_started_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/deferred/$',
            views.deferred_jobs, name='rq_deferred_jobs'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/empty/$',
            views.clear_queue, name='rq_clear'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/requeue-all/$',
            views.requeue_all, name='rq_requeue_all'),
    re_path(r'^queues/confirm-action/(?P<queue_index>[\d]+)/$',
            views.confirm_action, name='rq_confirm_action'),
    re_path(r'^queues/actions/(?P<queue_index>[\d]+)/$',
            views.actions, name='rq_actions'),
    re_path(r'^queues/(?P<queue_index>[\d]+)/(?P<job_id>[-A-Za-z0-9_~.%]+)/',
            include(detail_routes)),
]
