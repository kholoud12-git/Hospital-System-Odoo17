# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Mangment System Odoo 17 Test',
    'version': '1.0.0',
    'category': '',
    'summary': 'This My Fisrt Practical Application On Odoo 17',
    'description': """
    This App For Hospital Mangment System 
""",
    'license': 'OPL-1',
    'price': 0,
    'currency': 'USD',
    'author': 'Kholoud Samir',
    'support': 'kholoyssokar31@gmail.com',
    'depends': ['base', 'mail','account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'views/main_manu.xml',
        'views/hos_patient.xml',
        'views/hos_doctor.xml',
        'views/users_view.xml',
        'views/hos_appointments.xml',
        'views/hos_department.xml',
        'views/hos_medical_record.xml',
        'views/hos_invoice.xml',
        'views/hos_medication.xml',
        'views/hos_admission.xml',
        'views/hos_lab.xml',
        'views/hos_operation_room.xml',
        'views/hos_surgery.xml',
        'views/hos_nurse.xml',
        'views/hos_lab_appointment.xml',
        'views/hos_monthly_report.xml',
        'report/patient_report.xml',
        'report/prescription_report.xml',
        'data/hospital_demo.xml',
    ],
    'application': True,
}
