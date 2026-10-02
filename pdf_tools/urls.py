from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "pdf_tools"

urlpatterns = [
    path("merge/", views.merge_pdf, name="merge"),
    path("pdf-to-jpg/", views.pdf_to_jpg, name="pdf_to_jpg"),
    path("protect-pdf/", views.protect_pdf, name="protect_pdf"),
    path("compress-pdf/", views.compress_pdf, name="compress_pdf"),
    path("pdf-to-text/", views.pdf_to_text, name="pdf_to_text"),
    path("pdf-to-word/", views.pdf_to_word, name="pdf_to_word"),
    path("pdf-to-speech/", views.pdf_to_speech, name="pdf_to_speech"),
    path("split-pdf/", views.split_pdf, name="split_pdf"),
    path("unlock-pdf/", views.unlock_pdf, name="unlock_pdf"),
    path("pdf-to-excel/", views.pdf_to_excel, name="pdf_to_excel"),
    path("excel-to-pdf/", views.excel_to_pdf, name="excel_to_pdf"),
    path("image-to-pdf/", views.image_to_pdf, name="image_to_pdf"),
    path("crop-pdf/", views.crop_pdf, name="crop_pdf"),
    
    # Naye Edit PDF ke URLs
    path("edit-pdf/", views.edit_pdf, name="edit_pdf"),
    path("editor/", TemplateView.as_view(template_name="editor.html"), name="editor"),
    path("", TemplateView.as_view(template_name="editor.html"), name="home"),
]
