# Video — Infraestructura 1

## Orden corto

1. Mostrar topologia en GNS3.
2. FortiGate-1 GUI:
   - Interfaces.
   - VLAN10-USERS / DHCP.
   - VPN Site-to-Site en estado UP.
   - Firewall Policy.
3. FortiGate-2 GUI:
   - Interfaces.
   - VPN en estado UP.
   - Firewall Policy.
4. Ubuntu Client:

```bash
ip addr show ens33
ping -c 4 10.21.39.130
sudo busybox traceroute -n 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

5. Desactivar VPN desde GUI.
6. Repetir ping: debe fallar.
7. Reactivar VPN.
8. Repetir ping: debe funcionar.

## Narracion de cierre

> Con la VPN activa el usuario puede comunicarse con el servidor. Al desactivar el tunel la comunicacion se pierde y al restaurarlo vuelve a funcionar.
