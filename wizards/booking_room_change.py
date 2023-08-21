# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class BookingRoomChange(models.TransientModel):
    _name = 'booking.room.change'
    _description = 'Room Change Wizard'

    @api.model
    def default_get(self, fields):
        res = super(BookingRoomChange, self).default_get(fields)
        if(self.env.context.get('active_id')):
            bkId = self.env.context.get('active_id')

            booking = self.env['guesthouse.booking'].browse(bkId)


            res['name'] = booking.name
            res['booking_no'] = booking.booking_no
            res['room_no'] = booking.room_id.room_no
            res['room_id'] = booking.room_id.id
            res['arr_date'] = booking.arr_date
            res['dep_date'] = booking.dep_date
            res['credit_account'] = booking.credit_account.id

            return res

    name = fields.Char('Booking Name', readonly="1")
    booking_no = fields.Char('Booking Name', readonly="1")
    room_no = fields.Char('Room No', readonly="1")
    dep_date = fields.Date(string="Departure Date", readonly="1")
    arr_date = fields.Date(string="Departure Date", readonly="1")
    booking_id = fields.Many2one('guesthouse.booking', string="BookingId:", readonly="1")
    new_room_id = fields.Many2one('gh.room', string="New Room No")
    room_id = fields.Many2one('gh.room', string="New Room No", readonly="1")
    credit_account = fields.Many2one('res.partner', string="Credit Account", readonly="1")


    def action_room_change_booking(self):
        if(self.room_id != self.new_room_id):
            #print("credit account", self.credit_account.name)
            new_account_name = self.credit_account.name.replace(self.room_no, self.new_room_id.room_no)
            #print("credit new account", new_account_name)

            bk_id = self.booking_id.id
            acc_id = self.credit_account.id
            vals = {
                    'room_id': self.new_room_id,
                }
            vals_acc = {
                'name': new_account_name,
            }
            self.env['guesthouse.booking'].browse(bk_id).write(vals)
            self.env['res.partner'].browse(acc_id).write(vals_acc)

            registers = self.env['guesthouse.register'].search([('booking_id', '=', bk_id)])
            if registers:
                for reg in registers:
                    reg['room_id'] = self.new_room_id

        else:
            raise ValidationError(
                _('New room must be a different room!!'))





