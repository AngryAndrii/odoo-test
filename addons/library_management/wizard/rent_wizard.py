from odoo import models, fields, api

class LibraryRentWizard(models.TransientModel):
    _name = "library.rent.wizard"
    _description = "Wizard to rent book"

    partner_id = fields.Many2one('res.partner', string="User", required=True)
    book_id = fields.Many2one('library.book', string="Book", required=True)

    def action_confirm_rent(self):
        rent = self.env['library.rent'].create({
            'partner_id': self.partner_id.id,
            'book_id': self.book_id.id,
        })

        self.book_id.is_available = False
        return {'type': 'ir.actions.act_window_close'}