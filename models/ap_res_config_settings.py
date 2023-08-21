# -*- coding: utf-8 -*-


from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #service_charge = fields.Float('Service Charge', default=0, config_parameter='ap_inherits.service_charge') - no need - add as a TAX
    custom_usd_rate = fields.Float('Custom USD Rate', default=0, config_parameter='ap_inherits.custom_usd_rate')
    green_tax_rate = fields.Float('Green Tax Rate', default=0, config_parameter='ap_inherits.green_tax_rate')
