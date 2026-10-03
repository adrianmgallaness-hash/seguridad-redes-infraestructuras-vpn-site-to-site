# Infraestructura 2 — FortiGate ↔ Cisco Site-to-Site

![Topología lógica](../images/infraestructura-2/topologia-logica.svg)

## Objetivo

Permitir que el usuario se comunique con el servidor únicamente mediante una VPN Site-to-Site entre un FortiGate y un dispositivo Cisco.

## Requisitos

- 1 FortiGate
- 1 dispositivo Cisco
- ISP con direcciones públicas de laboratorio
- Usuario en VLAN 10
- DHCP
- Red de usuario /25
- Servidor web en red /28
- HTTPS
- NAT
- VPN Site-to-Site
- Traceroute

## VLAN y switch

La evidencia final debe identificar claramente la VLAN 10 de usuarios y el comportamiento del switch utilizado: puerto hacia el usuario, uplink y modo de cada puerto según la implementación real.

Ver [DPI, Switch, VLAN y seguridad básica](dpi-switch-vlan.md).

## DPI / inspección

Si en esta infraestructura se aplica un perfil de inspección en FortiGate, debe mostrarse la política y el perfil exacto utilizado, junto con una evidencia de log. No se documentan perfiles no verificados.

## Demostración recomendada

### FortiGate GUI
Mostrar:
- `Network → Interfaces`
- `VPN → IPsec Tunnels`
- `Policy & Objects → Firewall Policy`
- perfil de inspección si aplica

### Cisco

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
show ip nat translations
```

### Cliente

```bash
ip addr
ping -c 4 <IP_SERVIDOR>
sudo busybox traceroute -n <IP_SERVIDOR>
wget --no-check-certificate -T 5 -S -O- https://<IP_SERVIDOR>/
```

## Validación principal

- VPN activa → comunicación y HTTPS funcionan.
- VPN desactivada → el tráfico entre las dos redes debe fallar.
- VPN reactivada → la comunicación debe restablecerse.

## Configuraciones

Los running-config finales deben exportarse directamente de los equipos y guardarse en `configs/infraestructura-2/`.

No se incluyen valores no verificados en este documento.

## Evidencias pendientes

- topología real
- VLAN 10
- switch
- FortiGate interfaces
- VPN UP
- políticas
- DPI/perfil si aplica
- estado IKE/IPsec de Cisco
- NAT
- ping
- traceroute
- HTTPS
- VPN OFF/ON
