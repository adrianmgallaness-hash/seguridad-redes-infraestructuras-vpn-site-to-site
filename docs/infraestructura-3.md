# Práctica 2 — Infraestructura 3 | HTTPS sin VPN y SSH mediante VPN remota

![Topología lógica](../images/infraestructura-3/topologia-logica.svg)

## Objetivo

Permitir HTTPS hacia el servidor sin VPN y exigir una VPN de acceso remoto para SSH.

## Direccionamiento

- Red usuarios: `10.21.39.0/25`
- Gateway usuarios: `10.21.39.1`
- Cliente: `10.21.39.10/25`
- FortiGate port1: `198.51.100.22/30`
- Gateway ISP: `198.51.100.21`
- Red servidor: `10.21.39.128/28`
- Gateway servidor: `10.21.39.129`
- Servidor: `10.21.39.130/28`

## Publicación HTTPS

```text
Nombre: WEB-HTTPS-VIP
Interfaz: port1
IP externa: 198.51.100.22
IP mapeada: 10.21.39.130
TCP 443 -> 443
```

Política:

```text
Nombre: WAN-to-WEB-HTTPS
Entrada: port1
Salida: port2
Destino: WEB-HTTPS-VIP
Servicio: HTTPS
Acción: ACCEPT
NAT: OFF
```

## VPN de acceso remoto

- Túnel: `VPN-REMOTE-SSH`
- Grupo: `VPN-USERS`
- Pool: `10.99.99.10 - 10.99.99.20`
- Red protegida: `10.21.39.128/28`
- Acceso permitido: SSH

## Demostración

HTTPS sin VPN:

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

SSH sin VPN:

```bash
ssh adrian@10.21.39.130
```

Activar VPN:

```bash
sudo ipsec up VPN-REMOTE-SSH
```

SSH con VPN:

```bash
ssh adrian@10.21.39.130
```

## Video

Esta infraestructura se muestra dentro del **video único de la Práctica 2**.
