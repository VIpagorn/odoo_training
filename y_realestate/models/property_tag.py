from odoo import models, fields

class RealestatePropertyTag(models.Model):
    _name = 'y.realestate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'name asc'

    name = fields.Char(string="Tag Name", size=100)