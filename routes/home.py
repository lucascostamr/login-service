def home_routes(app):
    @app.route('/')
    def home():
        return '<a href="/login">Login with GitHub</a>'