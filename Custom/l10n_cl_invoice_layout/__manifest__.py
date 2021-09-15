# -*- coding: utf-8 -*-
{
    'name': "Custom Invoice Layout",

    'summary': """
        An alternative layout to the one already provided by Odoo
    """,

    'author': "Konos Soluciones & Servicios",
    'website': "https://www.konos.cl",

    'category': 'Localization/Chile',
    'version': '1.2',

    'depends': [
        'l10n_cl',
        'l10n_cl_counties',
        'l10n_cl_paper_format',
        'account',
    ],

    'data': [
        'views/account_report.xml',
        'views/report_invoice.xml',
    ],

    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
