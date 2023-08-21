# -*- coding: utf-8 -*-

from odoo import fields, models, api

class AddServiceChargePOS(models.Model):
    _inherit = 'pos.order'

    usd_total = fields.Float('Custom USD Rate', default=0, digits=(12, 2))


    @api.model
    def create(self, vals_list):
        custom_usd_rate = self.env['ir.config_parameter'].sudo().get_param('ap_inherits.custom_usd_rate')
        if custom_usd_rate:
            custom_usd_rate = float(custom_usd_rate)

            if custom_usd_rate > 0:
                amount_total = vals_list['amount_total']
                usd_total = round(amount_total / custom_usd_rate, 2)
                vals_list['usd_total'] = usd_total

                #Decimal(subtotal * 0.0475).quantize(Decimal("0.00"))
                print('sub_total', amount_total)
                print('usd_total', usd_total)
                print('new vals_list', vals_list)
        res = super(AddServiceChargePOS, self).create(vals_list)



        # do the custom coding here
        return res