from flask_login import login_manager

login_manager.blueprint_login_views = {
    'first': '/first',
    'logout':'/logout'
}