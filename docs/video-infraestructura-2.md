# Video — Infraestructura 2

## FortiGate <-> Cisco Site-to-Site

1. Mostrar topologia en GNS3.
2. FortiGate GUI:
   - Interfaces.
   - VLAN10-USERS / DHCP.
   - VPN-FGT1-CISCO en estado UP.
   - Firewall Policy.
3. Cisco:

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
```

4. Ubuntu Client:

```bash
ip addr show ens33
ping -c 4 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

5. Desactivar VPN desde FortiGate.
6. Ping al servidor: debe fallar.
7. Reactivar VPN.
8. Ping al servidor: debe funcionar.

## Narracion de cierre

> Estas pruebas demuestran el funcionamiento de la VPN Site-to-Site entre FortiGate y Cisco y que el acceso a la red remota depende del tunel.
