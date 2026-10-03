# Infraestructura 1 — FortiGate ↔ FortiGate Site-to-Site

![Topología lógica](../images/infraestructura-1/topologia-logica.svg)

## Objetivo

Permitir que el usuario de la VLAN 10 se comunique con el servidor remoto mediante un túnel VPN Site-to-Site entre dos FortiGate y demostrar que el tráfico deja de funcionar cuando el túnel se desactiva.

## Direccionamiento verificado

| Elemento | Dirección |
|---|---|
| Usuario | 10.21.39.10/25 |
| VLAN 10 | 10.21.39.0/25 |
| FortiGate-1 WAN | 198.51.100.22/30 |
| ISP hacia FortiGate-1 | 198.51.100.21/30 |
| ISP hacia FortiGate-2 | 203.0.113.37/30 |
| FortiGate-2 WAN | 203.0.113.38/30 |
| Red del servidor | 10.21.39.128/28 |
| Servidor | 10.21.39.130/28 |

## Segmentación VLAN y Switch

La red de usuarios se encuentra separada mediante **VLAN 10 USERS**, con direccionamiento `10.21.39.0/25`.

Durante la validación del FortiGate se observó al cliente mediante ARP en:

```text
10.21.39.10    VLAN10-USERS
```

Para la evidencia final deben mostrarse también los puertos del switch utilizados para el usuario y el uplink, indicando su modo real (Access o 802.1Q) y la VLAN asignada.

Ver: [DPI, Switch, VLAN y seguridad básica](dpi-switch-vlan.md).

## DPI / inspección

Además de las pruebas de conectividad, la entrega incluye una sección específica de DPI para documentar la política, el perfil de seguridad aplicado y la evidencia/log de inspección.

> El nombre exacto del perfil debe obtenerse de la configuración real del laboratorio; no se inventa en la documentación.

## Qué mostrar en GUI

### FortiGate-1
- `Network → Interfaces`
- `VLAN10-USERS` y DHCP
- `VPN → IPsec Tunnels` con el túnel en estado **UP**
- `Policy & Objects → Firewall Policy`
- política/perfil de inspección utilizado, si aplica

### FortiGate-2
- `Network → Interfaces`
- interfaz WAN y red del servidor
- `VPN → IPsec Tunnels` en estado **UP**
- `Policy & Objects → Firewall Policy`

## Pruebas verificadas

### IP del cliente

```bash
ip addr show ens33
```

Resultado esperado:

```text
10.21.39.10/25
```

### Ping

```bash
ping -c 4 10.21.39.130
```

Resultado verificado: comunicación exitosa.

### Traceroute

```bash
sudo busybox traceroute -n 10.21.39.130
```

Recorrido observado:

```text
10.21.39.1
203.0.113.38
10.21.39.130
```

### HTTPS

```bash
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

Resultado verificado:

```text
HTTP/1.0 200 OK
Servidor HTTPS - Seguridad de Redes
Ubuntu Server 10.21.39.130
```

## Validación principal

1. Con la VPN activa, el ping y HTTPS funcionan.
2. Desactivar temporalmente el túnel desde `VPN → IPsec Tunnels`.
3. Repetir:

```bash
ping -c 4 10.21.39.130
```

4. Debe fallar.
5. Reactivar el túnel y confirmar que el ping vuelve a funcionar.

## Nota de administración

Durante las pruebas, la GUI de FortiGate-1 se recuperó mediante HTTP administrativo:

```text
http://198.51.100.22:8080
```

La interfaz administrativa tenía habilitado `http` y el puerto administrativo HTTP configurado en 8080.

## Evidencias recomendadas

Guardar en `images/infraestructura-1/`:

- topología
- interfaces y VLAN 10
- DHCP
- switch/VLAN
- VPN UP
- políticas
- DPI/perfil de inspección
- IP del cliente
- ping
- traceroute
- HTTPS 200 OK
- ping fallando con VPN OFF
- ping funcionando nuevamente con VPN ON
