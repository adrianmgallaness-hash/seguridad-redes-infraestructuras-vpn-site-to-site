# Sanitización de configuraciones

Antes de subir un running-config al repositorio público:

1. Buscar PSK y contraseñas.
2. Eliminar valores cifrados que representen secretos.
3. No subir `key.pem` ni ninguna clave privada.
4. Sustituir credenciales por marcadores.

Ejemplo FortiGate:

```text
set psksecret "<PSK_DEL_LAB>"
```

Ejemplo StrongSwan:

```text
198.51.100.22 : PSK "<PSK_DEL_LAB>"
vpnuser : XAUTH "<PASSWORD_DEL_USUARIO_VPN>"
```

Nunca publicar las credenciales reales utilizadas en el laboratorio.
