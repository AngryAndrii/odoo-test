from odoo import fields, models


class CollegeStudent(models.Model):
    _name = "college.student"
    _description = "College Student"

    admission_no = fields.Char(string="Admission Name", required=True)
    admission_date = fields.Date(string="admission Date", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    father_name = fields.Char(string="Father Name", required=True)
    mother_name = fields.Char(string="Mother Name", required=True)
    communication_address = fields.Text(string="Communication address", required=True)
