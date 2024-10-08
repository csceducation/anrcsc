from django.contrib import admin
from django.urls import path

from .views import (
    ClassCreateView,
    ClassDeleteView,
    ClassListView,
    ClassUpdateView,
    CurrentSessionAndTermView,
    IndexView,
    SessionCreateView,
    SessionDeleteView,
    SessionListView,
    SessionUpdateView,
    SiteConfigView,
    SubjectCreateView,
    SubjectDeleteView,
    SubjectListView,
    SubjectUpdateView,
    TermCreateView,
    TermDeleteView,
    TermListView,
    TermUpdateView,
    BookCreateView,
    BookDeleteView,
    BookListView,
    BookUpdateView,
    ExamCreateView,
    ExamDeleteView,
    ExamListView,
    ExamUpdateView,
    TimeCreateView,
    TimeDeleteView,
    TimeListView,
    TimeUpdateView,
    redirector,
    BillDetailView,
    BillUpdateView,
    save_gst_percent,
    save_gst_number,
)

urlpatterns = [
    path("", IndexView.index, name="home"),
    path("site-config", SiteConfigView.as_view(), name="configs"),
    path(
        "current-session/", CurrentSessionAndTermView.as_view(), name="current-session"
    ),
    path("session/list/", SessionListView.as_view(), name="sessions"),
    path("session/create/", SessionCreateView.as_view(), name="session-create"),
    path(
        "session/<int:pk>/update/",
        SessionUpdateView.as_view(),
        name="session-update",
    ),
    path(
        "session/<int:pk>/delete/",
        SessionDeleteView.as_view(),
        name="session-delete",
    ),
    path("term/list/", TermListView.as_view(), name="terms"),
    path("term/create/", TermCreateView.as_view(), name="term-create"),
    path("term/<int:pk>/update/", TermUpdateView.as_view(), name="term-update"),
    path("term/<int:pk>/delete/", TermDeleteView.as_view(), name="term-delete"),
    path("class/list/", ClassListView.as_view(), name="classes"),
    path("class/create/", ClassCreateView.as_view(), name="class-create"),
    path("class/<int:pk>/update/", ClassUpdateView.as_view(), name="class-update"),
    path("class/<int:pk>/delete/", ClassDeleteView.as_view(), name="class-delete"),
    path("subject/list/", SubjectListView.as_view(), name="subjects"),
    path("subject/create/", SubjectCreateView.as_view(), name="subject-create"),
    path(
        "subject/<int:pk>/update/",
        SubjectUpdateView.as_view(),
        name="subject-update",
    ),
    path(
        "subject/<int:pk>/delete/",
        SubjectDeleteView.as_view(),
        name="subject-delete",
    ),
    path("book/list/", BookListView.as_view(), name="book"),
    path("book/create/", BookCreateView.as_view(), name="book-create"),
    path(
        "book/<int:pk>/update/",
        BookUpdateView.as_view(),
        name="book-update",
    ),
    path(
        "book/<int:pk>/delete/",
        BookDeleteView.as_view(),
        name="bookdelete",
    ),
    path("exam/list/", ExamListView.as_view(), name="exam"),
    path("exam/create/", ExamCreateView.as_view(), name="exam-create"),
    path(
        "exam/<int:pk>/update/",
        ExamUpdateView.as_view(),
        name="exam-update",
    ),
    path(
        "exam/<int:pk>/delete/",
        ExamDeleteView.as_view(),
        name="examdelete",
    ),
    path("time/list/", TimeListView.as_view(), name="time"),
    path("time/create/", TimeCreateView.as_view(), name="time-create"),
    path(
        "time/<int:pk>/update/",
        TimeUpdateView.as_view(),
        name="time-update",
    ),
    path(
        "time/<int:pk>/delete/",
        TimeDeleteView.as_view(),
        name="timedelete",
    ),
    path("redirector/",redirector,name="redirector"),
    path('bill/', BillDetailView.as_view(), name='bill-detail'),
    path('bill/edit/', BillUpdateView.as_view(), name='bill-update'),
    path('modify_gst',save_gst_percent,name='save_gst'),
    path('modify_gst_number',save_gst_number,name='save_gst_number')
]
