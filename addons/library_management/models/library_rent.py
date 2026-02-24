from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryRent(models.Model):
    _name = 'library.rent'
    _description = 'Library Rent'

    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True
    )

    book_id = fields.Many2one(
        'library.book',
        string='Book',
        required=True
    )

    rent_date = fields.Date(
        string='Rent Date',
        default=fields.Date.context_today,
        required=True
    )

    return_date = fields.Date(string='Return Date')

    # 🔒 Constraint: книга не може бути видана двічі
    @api.constrains('book_id', 'return_date')
    def _check_book_availability(self):
        for record in self:
            if not record.book_id:
                continue

            # шукаємо активні оренди цієї книги
            existing_rent = self.search([
                ('book_id', '=', record.book_id.id),
                ('return_date', '=', False),
                ('id', '!=', record.id)
            ])

            if existing_rent:
                raise ValidationError(
                    "This book is already rented and not returned yet!"
                )