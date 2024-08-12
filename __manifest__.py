# __manifest__.py
{
    "name": "Notice Module",
    "version": "1.0",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/notice_form.xml",
        "views/notice_page.xml",
        "views/templates.xml",
    ],
    "installable": True,
}
