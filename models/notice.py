# models/notice.py
from odoo import models, fields


class WebsiteNotice(models.Model):
    _name = "website.notice"
    _description = "Notice"

    title = fields.Char(string="Title", required=True)
    subtitle = fields.Char(string="Subtitle")
    attachment_id = fields.Many2one("ir.attachment", string="Attachment")
    published = fields.Boolean(string="Published", default=True)
