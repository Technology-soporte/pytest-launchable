import pytest
from auth import AuthService
from unittest.mock import MagicMock

# 📌 FIXTURE: Crea una instancia de AuthService para reutilizar en las pruebas
@pytest.fixture
def auth_service():
    return AuthService()

# 📌 PRUEBA PARAMETRIZADA: Testea múltiples combinaciones de usuario/contraseña
@pytest.mark.parametrize(
    "usuario, contraseña, esperado",
    [
        ("admin", "1234", "Login exitoso"),  # ✅ Caso exitoso
        ("user", "password", "Login exitoso"),  # ✅ Otro usuario válido
        ("admin", "wrongpass", "Credenciales incorrectas"),  # ❌ Contraseña incorrecta
        ("unknown", "1234", "Credenciales incorrectas"),  # ❌ Usuario inexistente
        ("unknown", "12342", "Credenciales incorrectas"),  # ❌ Usuario inexistente
    ],
)
def test_login(auth_service, usuario, contraseña, esperado):
    assert auth_service.login(usuario, contraseña) == esperado

# 📌 MOCK: Simula una base de datos externa
def test_login_con_mock():
    mock_auth = AuthService()
    mock_auth.usuarios = {"testuser": "testpass"}  # Simula datos en la "BD"
    
    assert mock_auth.login("testuser", "testpass") == "Login exitoso"
    assert mock_auth.login("testuser", "wrong") == "Credenciales incorrectas"
