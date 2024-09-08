from django.contrib import admin
from .models import Student, Grade
from semantic_admin import SemanticModelAdmin, SemanticStackedInline, SemanticTabularInline

from semantic_forms.filters import SemanticFilterSet


class GradeInline(SemanticTabularInline):
    model = Grade
    extra = 3


class StudentAdmin(SemanticModelAdmin):
    fieldsets = [
        (None, {"fields": ["student_name"]}),
        ("Date information", {"fields": ["birthday"]}),
    ]
    inlines = [GradeInline]
    list_display = ["student_name", "birthday"]
    list_filter = ["birthday"]
    search_fields = ["student_name"]


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Grade)
