from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

User: AbstractUser = get_user_model()


def create_employee_with_token(employee_data=None) -> tuple[AbstractUser, RefreshToken]:
    if not employee_data:
        employee_data = {
            "username": "regofalcao",
            "email": "rego.falcao@gmail.com",
            "birthdate": "1999-09-09",
            "first_name": "rego",
            "last_name": "falcao",
            "password": "1234",
            "is_employee": True,
        }

    employee = User.objects.create_superuser(**employee_data)
    employee_token = RefreshToken.for_user(employee)

    return employee, employee_token


def create_non_employee_with_token() -> tuple[AbstractUser, RefreshToken]:
    non_employee_data = {
        "username": "rego_common",
        "email": "rego.falcao_common@mail.com",
        "birthdate": "1999-09-09",
        "first_name": "rego",
        "last_name": "falcao",
        "password": "1111",
    }
    non_employee = User.objects.create_user(**non_employee_data)
    non_employee_token = RefreshToken.for_user(non_employee)

    return non_employee, non_employee_token
