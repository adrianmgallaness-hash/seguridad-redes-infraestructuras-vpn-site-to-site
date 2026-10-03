# Video de demostración

> Duración máxima: **10 minutos**.

> El video debe mostrar fecha/hora, rostro visible y voz audible.

La demostración debe enfocarse en comprobar que las topologías cumplen los objetivos, sin explicar cada línea de configuración.

## Infraestructura 1 — Guion corto

1. Mostrar topología completa en GNS3.
2. FortiGate-1:
   - `Network → Interfaces`
   - VLAN 10 / DHCP
   - `VPN → IPsec Tunnels` → UP
   - `Policy & Objects → Firewall Policy`
3. FortiGate-2:
   - interfaces
   - VPN → UP
   - Firewall Policy
4. Cliente:

```bash
ip addr show ens33
ping -c 4 10.21.39.130
sudo busybox traceroute -n 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

5. Desactivar VPN desde GUI.
6. Repetir ping → debe fallar.
7. Reactivar VPN.
8. Repetir ping → debe funcionar nuevamente.

Narración sugerida:

> “Con la VPN activa, el usuario puede comunicarse con el servidor y acceder al servicio HTTPS. Al desactivar el túnel, la comunicación se pierde. Al restaurarlo, vuelve a funcionar. Esto demuestra que la comunicación entre ambas redes depende de la VPN Site-to-Site.”

## Infraestructura 2 — Guion corto

1. Topología.
2. FortiGate: interfaces, VPN UP y políticas.
3. Cisco:

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
```

4. Cliente: ping, traceroute y HTTPS.
5. VPN OFF → ping falla.
6. VPN ON → ping vuelve.

## Infraestructura 3 — Guion corto

1. Topología.
2. FortiGate:
   - interfaces
   - VIP
   - políticas
   - VPN remota
   - grupo VPN
3. Mostrar HTTPS sin VPN.
4. Mostrar SSH sin VPN fallando.
5. Establecer VPN:

```bash
sudo ipsec up VPN-REMOTE-SSH
```

6. Mostrar SSH funcionando.

## Cierre

> “Con estas pruebas se demuestra el funcionamiento de las tres infraestructuras: dos escenarios Site-to-Site y un escenario de acceso remoto, aplicando segmentación, políticas de seguridad y control del tráfico mediante VPN.”
