# Seguridad de Redes — Infraestructuras VPN

> **Video de demostración:** [PENDIENTE: agregar enlace de YouTube o OneDrive]

Repositorio de entrega para la práctica de **Seguridad de Redes**, compuesta por tres infraestructuras implementadas en GNS3 con FortiGate, dispositivos de red, clientes y servidores Ubuntu.

## Propósito del laboratorio

Demostrar el uso de segmentación de red, VLAN, DHCP, NAT, políticas de firewall y diferentes modalidades de VPN para proteger la comunicación entre usuarios y servidores.

## Infraestructuras

### Infraestructura 1 — FortiGate ↔ FortiGate | VPN Site-to-Site
Objetivo: permitir la comunicación entre el usuario y el servidor únicamente cuando el túnel VPN Site-to-Site esté activo.

- 2 FortiGate
- ISP con direccionamiento público de laboratorio
- Usuario en VLAN 10 con DHCP
- Red de usuario /25
- Servidor web en red /28
- HTTPS
- NAT
- VPN Site-to-Site
- Traceroute
- Validación VPN ON/OFF

[Ver documentación](docs/infraestructura-1.md)

### Infraestructura 2 — FortiGate ↔ Cisco | VPN Site-to-Site
Objetivo: permitir la comunicación entre el usuario y el servidor únicamente cuando el túnel VPN Site-to-Site entre FortiGate y Cisco esté activo.

[Ver documentación](docs/infraestructura-2.md)

### Infraestructura 3 — Acceso remoto para SSH
Objetivo: permitir HTTPS al servidor sin VPN y acceso SSH únicamente mediante VPN de acceso remoto.

[Ver documentación](docs/infraestructura-3.md)

## Estructura del repositorio

```text
.
├── README.md
├── docs/
│   ├── infraestructura-1.md
│   ├── infraestructura-2.md
│   ├── infraestructura-3.md
│   ├── pruebas-validaciones.md
│   └── video-demostracion.md
├── configs/
│   ├── README.md
│   └── sanitizacion.md
├── scripts/
│   ├── README.md
│   └── https_server.py
└── images/
    └── README.md
```

## Evidencias requeridas

- Topología completa de cada infraestructura
- Interfaces y direccionamiento
- VLAN 10 y DHCP
- Políticas de firewall
- NAT/VIP cuando aplique
- Estado de los túneles VPN
- Ping
- Traceroute
- HTTPS
- SSH en Infraestructura 3
- Prueba de pérdida de conectividad con VPN desactivada en los escenarios Site-to-Site

## Seguridad

No se publican contraseñas, PSK reales, claves privadas ni secretos. Utilizar marcadores como:

```text
<PSK_DEL_LAB>
<PASSWORD_DEL_USUARIO_VPN>
```

## Estado de validación

- Infraestructura 1: conectividad, traceroute y HTTPS validados
- Infraestructura 3: HTTPS sin VPN y SSH mediante VPN validados
- Infraestructura 2: pendiente de incorporar evidencias y running-config finales verificados
- Video final: pendiente de agregar enlace
