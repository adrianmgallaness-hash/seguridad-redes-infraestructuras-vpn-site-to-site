# Seguridad de Redes — Infraestructuras VPN

> **Video de demostración:** [PENDIENTE: agregar enlace de YouTube o OneDrive]

Repositorio de entrega para la práctica de **Seguridad de Redes**, compuesta por tres infraestructuras implementadas en GNS3 con FortiGate, dispositivos de red, clientes y servidores Ubuntu.

## Propósito del laboratorio

Demostrar el uso de segmentación de red, VLAN, DHCP, NAT, políticas de firewall, inspección de tráfico y diferentes modalidades de VPN para proteger la comunicación entre usuarios y servidores.

## Infraestructuras

### Infraestructura 1 — FortiGate ↔ FortiGate | VPN Site-to-Site

![Topología lógica de Infraestructura 1](images/infraestructura-1/topologia-logica.svg)

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

![Topología lógica de Infraestructura 2](images/infraestructura-2/topologia-logica.svg)

Objetivo: permitir la comunicación entre el usuario y el servidor únicamente cuando el túnel VPN Site-to-Site entre FortiGate y Cisco esté activo.

[Ver documentación](docs/infraestructura-2.md)

### Infraestructura 3 — Acceso remoto para SSH

![Topología lógica de Infraestructura 3](images/infraestructura-3/topologia-logica.svg)

Objetivo: permitir HTTPS al servidor sin VPN y acceso SSH únicamente mediante VPN de acceso remoto.

[Ver documentación](docs/infraestructura-3.md)

## DPI, Switch, VLAN y seguridad básica

A partir de la retroalimentación recibida en una entrega anterior, el repositorio incluye una sección específica para documentar:

- DPI / inspección profunda
- perfiles de seguridad aplicados
- evidencia de inspección/logs
- switch
- VLAN 10
- puertos Access/802.1Q según la implementación real
- seguridad básica del switch

[Ver documentación de DPI y Switch/VLAN](docs/dpi-switch-vlan.md)

## Estructura del repositorio

```text
.
├── README.md
├── docs/
│   ├── infraestructura-1.md
│   ├── infraestructura-2.md
│   ├── infraestructura-3.md
│   ├── dpi-switch-vlan.md
│   ├── pruebas-validaciones.md
│   └── video-demostracion.md
├── configs/
├── scripts/
└── images/
    ├── infraestructura-1/
    ├── infraestructura-2/
    ├── infraestructura-3/
    └── controles/
```

## Evidencias requeridas

- Topología visual de cada infraestructura
- Interfaces y direccionamiento
- VLAN 10 y DHCP
- Switch y configuración de puertos
- Políticas de firewall
- DPI/perfiles de inspección cuando aplique
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
- DPI/Switch/VLAN: sección documental creada; faltan insertar las capturas reales de la configuración aplicada
- Video final: pendiente de agregar enlace
