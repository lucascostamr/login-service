login_service/
├── main.py
├── api/
│   └── routers/
│       └── login_router.py
├── domain/
│   ├── dtos/
│   │   └── login_dto.py
│   └── services/
│       ├── login_service.py
│       └── strategies/
│           ├── auth_strategy_interface.py
│           ├── github_oauth.py
│           ├── google_oauth.py
│           └── user_password.py
├── infrastructure/
│   └── security/
│       └── jwt_handler.py
├── config/
│   └── settings.py
└── .env