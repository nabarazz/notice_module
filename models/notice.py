from odoo import models, fields


class Notice(models.Model):
    _name = "website.notice"
    _description = "Notice"

    title = fields.Char(string="Title", required=True)
    subtitle = fields.Char(string="Subtitle")
    attachment_id = fields.Many2one(
        "ir.attachment", string="File Attachment", required=True
    )
    published = fields.Boolean(string="Published", default=True)
