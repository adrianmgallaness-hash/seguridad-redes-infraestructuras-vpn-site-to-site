# Seguridad de Redes — Infraestructuras VPN

> **Video de demostración:** [PENDIENTE: agregar enlace de YouTube o OneDrive]

Repositorio de entrega para la práctica de **Seguridad de Redes**, compuesta por tres infraestructuras implementadas en GNS3 con FortiGate, Cisco, clientes y servidores Ubuntu.

## Propósito del laboratorio

Demostrar segmentación de red, VLAN, DHCP, NAT/VIP, políticas de firewall, inspección de tráfico y diferentes modalidades de VPN para proteger la comunicación entre usuarios y servidores.

## Infraestructuras

### Infraestructura 1 — FortiGate ↔ FortiGate | VPN Site-to-Site

![Topología lógica de Infraestructura 1](images/infraestructura-1/topologia-logica.svg)

Objetivo: permitir la comunicación entre el usuario y el servidor únicamente cuando el túnel VPN Site-to-Site esté activo.

[Documentación](docs/infraestructura-1.md) · [Guía de video](docs/video-infraestructura-1.md) · [Configuración verificada](configs/infraestructura-1/configuracion-verificada.txt)

### Infraestructura 2 — FortiGate ↔ Cisco | VPN Site-to-Site

![Topología lógica de Infraestructura 2](images/infraestructura-2/topologia-logica.svg)

Pruebas realizadas: túnel operativo, traceroute hasta `10.21.39.130` y HTTPS validado.

[Documentación](docs/infraestructura-2.md) · [Guía de video](docs/video-infraestructura-2.md) · [Configuración verificada](configs/infraestructura-2/configuracion-verificada.txt)

### Infraestructura 3 — HTTPS público + SSH por VPN remota

![Topología lógica de Infraestructura 3](images/infraestructura-3/topologia-logica.svg)

Objetivo: permitir HTTPS al servidor sin VPN y restringir SSH para que sea accesible mediante VPN de acceso remoto.

[Documentación](docs/infraestructura-3.md) · [Guía de video](docs/video-infraestructura-3.md) · [Configuración](configs/infraestructura-3/configuracion-verificada.txt)

## DPI, Switch, VLAN y seguridad básica

Se incluye documentación específica para DPI/inspección, perfiles de seguridad, logs, switch, VLAN 10 y puertos Access/802.1Q según la implementación real.

[Ver DPI, Switch, VLAN y seguridad básica](docs/dpi-switch-vlan.md)

## Evidencias gráficas pendientes de incorporar

Las capturas deben provenir del laboratorio real. Faltan principalmente: topologías reales, interfaces, VPN UP, políticas, VIP de Infraestructura 3, IKE/IPsec en Cisco, pruebas de ping/HTTPS/SSH, VPN OFF/ON y evidencias de DPI/switch.

## Seguridad

No se publican contraseñas, PSK reales, claves privadas ni valores `psksecret ENC ...`.

## Estado

- Infraestructura 1: conectividad, traceroute, HTTPS y prueba VPN ON/OFF documentadas.
- Infraestructura 2: conectividad y HTTPS verificadas; documentación y guía de video actualizadas.
- Infraestructura 3: configuración y acceso remoto documentados; VIP/política HTTPS deben aparecer en la captura final de la instancia actual.
- Video: guías cortas separadas por infraestructura disponibles.
- Capturas reales finales: pendientes de subir.