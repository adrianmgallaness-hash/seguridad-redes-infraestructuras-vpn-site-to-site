# Video — Infraestructura 3

## HTTPS sin VPN + SSH mediante VPN remota

1. Mostrar topologia en GNS3.
2. FortiGate GUI:
   - Interfaces.
   - WEB-HTTPS-VIP.
   - WAN-to-WEB-HTTPS.
   - VPN-REMOTE-SSH.
   - VPN-USERS.
3. Ubuntu Client, sin VPN:

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
ssh adrian@10.21.39.130
```

HTTPS debe funcionar y SSH directo debe fallar.

4. Activar VPN:

```bash
sudo ipsec up VPN-REMOTE-SSH
```

5. Repetir SSH:

```bash
ssh adrian@10.21.39.130
```

Debe funcionar mediante la VPN.

## Narracion de cierre

> HTTPS se encuentra publicado sin necesidad de VPN, mientras que SSH solo esta disponible para usuarios conectados mediante la VPN de acceso remoto.
