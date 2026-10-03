# Configuraciones — Infraestructura 3

Incluidos:
- `configuracion-verificada.txt`: VIP, política HTTPS, VPN remota y comportamiento a demostrar.
- `strongswan-ipsec.conf.example`: configuración cliente sanitizada.

Antes de entregar, comprobar que WEB-HTTPS-VIP y WAN-to-WEB-HTTPS aparecen en la instancia actual y guardar capturas.

Si se requiere running-config completo, exportarlo desde FortiGate después de eliminar PSK, contraseñas, claves privadas y `psksecret ENC ...`.