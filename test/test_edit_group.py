
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username='admin', password='secret')
    app.group.edit_first_group(Group(name="124", header="678", footer="0-76785"))
    app.session.logout()
