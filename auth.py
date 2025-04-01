class AuthService:
    def __init__(self):
        # Diccionario que simula una base de datos de usuarios
        self.usuarios = {"admin": "1234", "user": "password"}

    def login(self, usuario, contraseña):
        if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
            return "Login exitoso"
        return "Credenciales incorrectas"
