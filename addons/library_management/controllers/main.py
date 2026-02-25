from odoo import http
from odoo.http import request

class LibraryController(http.Controller):
    """ роутер на отримання JSON з книгами """
    @http.route(
        '/library/books',
        type='json',      # повертаємо JSON
        auth='public',
        methods=['GET'],
        csrf=False
    )
    def get_books(self):
        books = request.env['library.book'].sudo().search([])

        result = []
        # проходимося по книгам, якщо вони є і додаємо до результату
        for book in books:
            result.append({
                'id': book.id,
                'name': book.name,
                'author': book.author,
                'published_date': book.published_date,
                'is_available': book.is_available,
            })
        # повертаємо результат
        return result
