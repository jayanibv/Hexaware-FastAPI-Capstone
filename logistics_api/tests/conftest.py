import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.core.security import create_access_token, hash_password
from app.models.user import User, UserRole

# Test database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db():
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

@pytest.fixture
def test_user(db):
    user = User(
        email="test@example.com",
        password_hash=hash_password("password123"),
        role=UserRole.customer
    )
    db.add(user)
    db.flush()
    db.refresh(user)
    return user

@pytest.fixture
def test_admin(db):
    user = User(
        email="admin@example.com",
        password_hash=hash_password("password123"),
        role=UserRole.admin
    )
    db.add(user)
    db.flush()
    db.refresh(user)
    return user

@pytest.fixture
def test_agent(db):
    user = User(
        email="agent@example.com",
        password_hash=hash_password("password123"),
        role=UserRole.agent
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture
def admin_token(test_admin):
    return create_access_token(data={"sub": str(test_admin.id), "role": "admin"})

@pytest.fixture
def agent_token(test_agent):
    return create_access_token(data={"sub": str(test_agent.id), "role": "agent"})

@pytest.fixture
def customer_token(test_user):
    return create_access_token(data={"sub": str(test_user.id), "role": "customer"})
