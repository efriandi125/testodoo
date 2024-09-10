# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Picking(models.Model):
    _inherit = 'stock.picking'

   
    
    @api.model
    def _get_status(self):
               
        State=[
                    ('draft', 'Draft'),
                    ('waiting', 'Waiting Another Operation'),
                    ('confirmed', 'Waiting'),
                    ('assigned', 'Ready') if self._context.get('restricted_picking_type_code')!='internal' else ('assigned', 'Approved'),
                    ('done', 'Delivered'),
                    ('cancel', 'Cancelled'),
                ]
        return State

              
    state = fields.Selection(selection=_get_status, string='Status', compute='_compute_state',
        copy=False, index=True, readonly=True, store=True, tracking=True,
        help=" * Draft: The transfer is not confirmed yet. Reservation doesn't apply.\n"
             " * Waiting another operation: This transfer is waiting for another operation before being ready.\n"
             " * Waiting: The transfer is waiting for the availability of some products.\n(a) The shipping policy is \"As soon as possible\": no product could be reserved.\n(b) The shipping policy is \"When all products are ready\": not all the products could be reserved.\n"
             " * Ready: The transfer is ready to be processed.\n(a) The shipping policy is \"As soon as possible\": at least one product has been reserved.\n(b) The shipping policy is \"When all products are ready\": all product have been reserved.\n"
             " * Done: The transfer has been processed.\n"
             " * Cancelled: The transfer has been cancelled.")