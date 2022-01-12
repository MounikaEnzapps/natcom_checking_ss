# -*- coding: utf-8 -*-
{
    'name': "Natcom mail DateTIME",
    'author':
        'Enzapps',
    'summary': """
This module is for creating api for Invoices.
""",

    'description': """
        This module consist of track page of cargo which extend the website.
        It consist of 2 tabs Brief and History
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['sale','purchase','base','account','natcom_dec_last','natcom_orders_sequences','natcom_remarks','natcom_orders_sequences','natcom_checking_s'],
    "images": ['static/description/icon.png'],
    'data': [
              'views/account_move.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
