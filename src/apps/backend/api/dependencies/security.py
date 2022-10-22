# from fastapi import (
#     Depends,
#     HTTPException,
#     status
# )
# from fastapi.security import (
#     OAuth2PasswordBearer,
#     SecurityScopes
# )
# from jose import (
#     JWTError,
#     jwt
# )
# from pydantic import ValidationError
#
# from unity.app.backend.api.dependencies.common import get_service
# from unity.app.backend.config import settings
# from unity.app.backend.schemas.auth import TokenSchema
# from unity.app.backend.schemas.user import UserSchema
# from unity.app.backend.services.user import UserService
#
# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl=settings.SECURITY_ACCESS_TOKEN_URL,
#     scopes=SCOPES
# )
#
#
# async def get_current_user(
#         security_scopes: SecurityScopes,
#         token: str = Depends(oauth2_scheme),
#         user: UserService = Depends(get_service(UserService))
# ) -> UserSchema:
#     if security_scopes.scopes:
#         authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
#     else:
#         authenticate_value = f"Bearer"
#
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": authenticate_value},
#     )
#
#     try:
#         payload = jwt.decode(token, settings.SECURITY_SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
#
#         username: str = payload.get("sub")
#
#         if username is None:
#             raise credentials_exception
#
#         token = TokenSchema(scopes=payload.get("scopes", []), username=username)
#
#         role = await user.get_by_username(token.username)
#
#         if role is None or role.disabled:
#             raise credentials_exception
#
#         role = UserSchema.from_orm(role)
#     except (JWTError, ValidationError):
#         raise credentials_exception
#
#     if SUPERUSER_SCOPE not in token.scopes:
#         for scope in security_scopes.scopes:
#             if scope not in token.scopes:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail="Not enough permissions",
#                     headers={"WWW-Authenticate": authenticate_value},
#                 )
#
#     return role
