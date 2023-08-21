odoo.define('get_total_pos_receipt.models', function (require) {
"use strict";

    var { Order } = require('point_of_sale.models');
    var Registries = require('point_of_sale.Registries');

    const CustomTotalAmount = (Order) => class CustomOrder extends Order {
        export_for_printing() {
            var result = super.export_for_printing(...arguments);
//            result.total_amount = parseFloat(this.get_total_without_tax() / 15).toFixed(2);
            result.total_amount = parseFloat(this.get_total_with_tax() / 15).toFixed(2);

            return result;
            }
        }
        Registries.Model.extend(Order, CustomTotalAmount);
    });