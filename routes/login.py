def login_routes(app):
    @app.route('/login')
    def login():
        github_auth_url = (
            'https://github.com/login/oauth/authorize'
            f'?client_id={CLIENT_ID}&scope=read:user'
        )
        return redirect(github_auth_url)

    @app.route('/callback')
    def callback():
        code = request.args.get('code')

        token_res = requests.post(
            'https://github.com/login/oauth/access_token',
            headers={'Accept': 'application/json'},
            data={
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'code': code,
            }
        )
        token = token_res.json()['access_token']

        user_res = requests.get(
            'https://api.github.com/user',
            headers={'Authorization': f'token {token}'}
        )
        user = user_res.json()
        return f"<h1>Logged in as {user['login']}</h1><img src='{user['avatar_url']}' width=100 />"