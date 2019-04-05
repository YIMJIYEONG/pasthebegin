from django.contrib import admin
from polls.models import Question, Choice


# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # 필드 순서변경하기
    # fields = ['pub_date', 'question_text']
    # 필드 분리해서보여주기
    # fieldsets = [
    #     ('Question Statement', {'fields': ['question_text']}),
    #     # 필드 접기
    #     ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #     # ('Date Information', {'fields': ['pub_date']}),
    # ]
    # 한 화면에서 변경하기
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)



