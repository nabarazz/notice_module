# controllers/main.py
from odoo import http
from odoo.http import request


class NoticeController(http.Controller):

    @http.route("/website/notices", type="http", auth="public", website=True)
    def notices(self, **kwargs):
        # Fetch notices to display on the website
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
        # Handle file downloads for public users
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
