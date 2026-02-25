from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryRent(models.Model):
    """Модель оренди книг"""
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

    @api.constrains('book_id', 'return_date')
    def _check_book_availability(self):
        for record in self:
            if not record.book_id:
                continue

            # Перевіряємо, чи вже хтось орендував цю книгу
            existing_rent = self.search([
                ('book_id', '=', record.book_id.id),
                ('return_date', '=', False),
                ('id', '!=', record.id)
            ])

            if existing_rent:
                raise ValidationError(
                    "This book is already rented and not returned yet!"
                )

    def write(self, vals):
        # Викликаємо стандартний write
        res = super(LibraryRent, self).write(vals)

        # Якщо оновлюється return_date, робимо книгу доступною
        if 'return_date' in vals:
            for rent in self:
                if rent.return_date:
                    rent.book_id.is_available = True

        return res