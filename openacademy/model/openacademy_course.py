from openerp import fields, models

'''
This module creates the model of Course
'''

class Course(models.Model):
    '''
    This class creates the model of Course
    '''
    _name = 'openacademy.course' # Model odoo name
    
    name = fields.Char(string='Title', required=True)  #  Field reserved to identified name rec
    description = fields.Text(string='Description')
