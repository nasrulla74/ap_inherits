# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime, date


class BookingExtend(models.TransientModel):
    _name = 'booking.extend'
    _description = 'Extend Booking Wizard'

    @api.model
    def default_get(self, fields):
        res = super(BookingExtend, self).default_get(fields)
        if(self.env.context.get('active_id')):
            bkId = self.env.context.get('active_id')

            booking = self.env['guesthouse.booking'].browse(bkId)


            res['name'] = booking.name
            res['booking_no'] = booking.booking_no
            res['room_no'] = booking.room_id.room_no
            res['arr_date'] = booking.arr_date
            res['dep_date'] = booking.dep_date

            return res

    name = fields.Char('Booking Name', readonly="1")
    booking_no = fields.Char('Booking Name', readonly="1")
    room_no = fields.Char('Room No', readonly="1")
    dep_date = fields.Date(string="Departure Date", readonly="1")
    arr_date = fields.Date(string="Departure Date", readonly="1")
    booking_id = fields.Many2one('guesthouse.booking', string="BookingId:", readonly="1")
    #room_id = fields.Many2one('gh.room', string="Room No", readonly="1")
    new_dep_date = fields.Date(string="New Departure Date", required=True)



    def action_extend_booking(self):
        dep_dt = self.dep_date
        n_date = self.new_dep_date
        bk_id = self.booking_id.id


        if(n_date > dep_dt):

            vals = {
                'dep_date': n_date,
            }
            self.env['guesthouse.booking'].browse(bk_id).write(vals)

            registers = self.env['guesthouse.register'].search([('booking_id', '=', bk_id)])

            if registers:
                for reg in registers:
                    reg['dep_date'] = n_date



        else:
            raise ValidationError(
                _('Extend date must be grater than departure date!!!'))


