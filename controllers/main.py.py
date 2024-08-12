# controllers/main.py
from odoo import http
from odoo.http import request


class NoticeController(http.Controller):

    @http.route("/website/notices", type="http", auth="public", website=True)
    def notices(self, **kwargs):
        # If you need to import something from your module, do it here.
        # Example:
        # from odoo.addons.notice_module.models import notice
        notices = (
            request.env["website.notice"].sudo().search([("published", "=", True)])
        )
        return request.render(
            "notice_module.notice_page",
            {
                "notices": notices,
            },
        )

    @http.route(
        "/website/download/notice/<int:notice_id>",
        type="http",
        auth="public",
        website=True,
    )
    def download_notice(self, notice_id, **kwargs):
        notice = request.env["website.notice"].sudo().browse(notice_id)
        if notice.attachment_id:
            return request.make_response(
                notice.attachment_id.datas,
                [
                    ("Content-Type", "application/octet-stream"),
                    (
                        "Content-Disposition",
                        'attachment; filename="%s"' % notice.attachment_id.name,
                    ),
                ],
            )
        return request.not_found()
