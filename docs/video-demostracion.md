# Práctica 2 — Video de demostración

> La **Práctica 2** se presenta en un único video con las tres infraestructuras.

▶️ **Video completo:** [Ver en YouTube](https://youtu.be/vsI622JK9Ig)

> Duración máxima recomendada: **10 minutos**.

La demostración se enfoca en comprobar el funcionamiento de cada escenario sin explicar cada línea de configuración.

## Infraestructura 1 — FortiGate ↔ FortiGate

1. Mostrar topología en GNS3.
2. Mostrar interfaces, VLAN 10 / DHCP, VPN UP y políticas en FortiGate.
3. Desde Ubuntu Client:

```bash
ip addr show ens33
ping -c 4 10.21.39.130
sudo busybox traceroute -n 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

4. Desactivar la VPN y mostrar que el ping falla.
5. Reactivar la VPN y mostrar que vuelve la conectividad.

## Infraestructura 2 — FortiGate ↔ Cisco

1. Mostrar topología.
2. FortiGate: interfaces, VPN `VPN-FGT1-CISCO` UP y Firewall Policy.
3. Cisco:

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
```

4. Ubuntu Client:

```bash
ping -c 4 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

5. Mostrar brevemente VPN OFF/ON y restauración de conectividad.

## Infraestructura 3 — HTTPS sin VPN + SSH por VPN remota

1. Mostrar topología.
2. FortiGate:
   - interfaces
   - `WEB-HTTPS-VIP`
   - `WAN-to-WEB-HTTPS`
   - `VPN-REMOTE-SSH`
   - `VPN-USERS`
3. Probar HTTPS sin VPN:

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

4. Probar SSH sin VPN y mostrar que no funciona.
5. Activar VPN:

```bash
sudo ipsec up VPN-REMOTE-SSH
```

6. Repetir SSH y mostrar acceso exitoso.

## Cierre

> “Con estas pruebas se demuestra el funcionamiento de las tres infraestructuras de la Práctica 2: dos escenarios VPN Site-to-Site y un escenario de acceso remoto, aplicando segmentación, políticas de seguridad y control del tráfico.”
