# Infraestructura 3 — HTTPS sin VPN y SSH mediante VPN de acceso remoto

![Topología lógica](../images/infraestructura-3/topologia-logica.svg)

## Objetivo

Permitir que el usuario acceda al servidor web mediante HTTPS sin VPN, pero exigir una VPN de acceso remoto para acceder al servidor mediante SSH.

## Direccionamiento verificado

### VLAN 10 USERS
- Red: `10.21.39.0/25`
- Gateway: `10.21.39.1`
- Cliente DHCP: `10.21.39.10/25`

### Cisco WAN
- `203.0.113.38/30`
- Gateway ISP: `203.0.113.37`

### FortiGate
- `port1`: `198.51.100.22/30`
- Gateway: `198.51.100.21`
- `port2`: `10.21.39.129/28`

### Servidor
- IP: `10.21.39.130/28`
- Gateway: `10.21.39.129`
- HTTPS: TCP/443
- SSH: TCP/22

## Switch y VLAN 10

En esta infraestructura se utiliza VLAN 10 para la red de usuarios. La documentación final debe incluir captura del switch y mostrar el puerto hacia el cliente y el uplink, con sus modos reales.

Ver [DPI, Switch, VLAN y seguridad básica](dpi-switch-vlan.md).

## Publicación HTTPS

VIP:

```text
Nombre: WEB-HTTPS-VIP
Interfaz: port1
IP externa: 198.51.100.22
IP mapeada: 10.21.39.130
TCP 443 → 443
```

Política:

```text
Nombre: WAN-to-WEB-HTTPS
Entrada: port1
Salida: port2
Destino: WEB-HTTPS-VIP
Servicio: HTTPS
NAT: deshabilitado
```

Prueba sin VPN:

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

Resultado validado: `HTTP/1.0 200 OK`.

## VPN de acceso remoto

- Túnel: `VPN-REMOTE-SSH`
- Grupo: `VPN-USERS`
- Pool: `10.99.99.10 - 10.99.99.20`
- Red protegida: `10.21.39.128/28`
- Política VPN hacia servidor restringida a SSH

## Pruebas

### Sin VPN

HTTPS público funciona:

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

SSH directo no funciona:

```bash
ssh adrian@10.21.39.130
```

### Con VPN

```bash
sudo ipsec up VPN-REMOTE-SSH
sudo ipsec statusall
```

Se verificó:
- autenticación XAuth exitosa
- IKE SA establecida
- IP virtual `10.99.99.10`
- CHILD SA establecida
- tráfico protegido hacia `10.21.39.128/28`

Después:

```bash
ssh adrian@10.21.39.130
```

Resultado validado: acceso SSH exitoso.

## Seguridad

No publicar PSK, contraseñas ni `psksecret ENC ...`. Sustituir por:

```text
<PSK_DEL_LAB>
<PASSWORD_DEL_USUARIO_VPN>
```

## Evidencias pendientes

- topología real
- switch y VLAN 10
- DHCP
- VIP HTTPS
- políticas
- túnel remoto
- grupo VPN
- HTTPS sin VPN
- SSH fallando sin VPN
- VPN establecida
- SSH funcionando mediante VPN
