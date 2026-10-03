# Práctica 2 — Infraestructura 2 | FortiGate ↔ Cisco Site-to-Site

![Topología lógica](../images/infraestructura-2/topologia-logica.svg)

## Objetivo

Permitir que el usuario se comunique con el servidor remoto mediante una VPN Site-to-Site entre un FortiGate y un dispositivo Cisco.

## Direccionamiento observado

| Elemento | Dirección |
|---|---|
| FortiGate port1 | 198.51.100.22/30 |
| Gateway ISP | 198.51.100.21 |
| FortiGate port2 | 192.168.57.1/24 |
| VLAN10-USERS | 10.21.39.1/25 |
| Red usuarios | 10.21.39.0/25 |
| Red remota | 10.21.39.128/28 |
| Servidor | 10.21.39.130 |
| Extremo remoto del túnel | 203.0.113.38 |

Ruta observada:

```text
S 10.21.39.128/28 via VPN-FGT1-CISCO tunnel 203.0.113.38
```

## Evidencia Cisco

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
```

## Pruebas

```bash
ping -c 4 10.21.39.130
sudo busybox traceroute -n 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

Resultado HTTPS verificado: `HTTP/1.0 200 OK`.

## Validación

- VPN activa → comunicación funciona.
- VPN desactivada → tráfico entre redes falla.
- VPN reactivada → comunicación restaurada.

## Video

Esta infraestructura se muestra dentro del **video único de la Práctica 2**.
