from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import CounterTable, doctor, ReportType, Patient,paid_installment
# Register your models here.

admin.site.site_header = 'MEDI-CENTER ADMIN PANEL'
admin.site.site_title = 'MEDI-CENTER ADMINISTRATION'
admin.site.index_title = 'MEDI-CENTER DASHBOARD'

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(CounterTable)
admin.site.register(doctor)
admin.site.register(ReportType)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    @admin.display(description="Name")
    def upper_case_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".upper()

    list_display = [ 'upper_case_name', 'mobile', 'doctor_id', 'report_type', 'total_amount', 'paid_amount', 'remaining_amount', 'address']
    list_display_links = ['upper_case_name']
    list_filter = ['payment_status', 'doctor_id']
    search_fields = ['first_name', 'mobile']
    list_editable = ['mobile', 'doctor_id', 'report_type']
    list_per_page = 2

    fieldsets = [
        (
            "Personal Information",
            {
                "fields": ["first_name", "last_name", "mobile", "address"],
                "description": "This section includes personal information such as first name, last name, mobile number, and address.",
            },
        ),
        (
            "Doctor Information",
            {
                "classes": ["collapse"],
                "fields": ["doctor_id"],
            },
        ),
         (
            "Lab Information",
            {
                "fields": ["report_type"],
            },
        ),
        (
            "Payment Information",
            {
                "classes": ["collapse"],
                "fields": ["payment_status", "total_amount", "paid_amount", "remaining_amount"],
            },
        ),
    ]

# admin.site.register(Patient)
admin.site.register(paid_installment)
