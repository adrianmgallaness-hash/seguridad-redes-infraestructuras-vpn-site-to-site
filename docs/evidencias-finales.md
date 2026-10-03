# Evidencias finales

Esta lista sirve para verificar que las capturas subidas provienen del laboratorio real y cubren los requisitos principales.

## Infraestructura 1

- [ ] Topología real en GNS3
- [ ] Interfaces FortiGate-1
- [ ] VLAN10-USERS y DHCP
- [ ] VPN Site-to-Site UP
- [ ] Políticas de firewall
- [ ] Ping al servidor
- [ ] Traceroute
- [ ] HTTPS 200 OK
- [ ] VPN OFF: ping falla
- [ ] VPN ON: ping vuelve

## Infraestructura 2

- [ ] Topología real en GNS3
- [ ] Interfaces FortiGate
- [ ] VLAN10-USERS / DHCP
- [ ] VPN-FGT1-CISCO UP
- [ ] Firewall Policy
- [ ] `show ip interface brief`
- [ ] `show crypto isakmp sa`
- [ ] `show crypto ipsec sa`
- [ ] Ping/HTTPS al servidor
- [ ] VPN OFF/ON

## Infraestructura 3

- [ ] Topología real
- [ ] Interfaces FortiGate
- [ ] WEB-HTTPS-VIP
- [ ] WAN-to-WEB-HTTPS
- [ ] VPN-REMOTE-SSH
- [ ] VPN-USERS
- [ ] HTTPS sin VPN
- [ ] SSH sin VPN fallando
- [ ] VPN establecida
- [ ] SSH funcionando por VPN

## DPI / Switch / VLAN

- [ ] Política donde se aplica inspección
- [ ] Perfil de seguridad real
- [ ] Log de inspección
- [ ] VLAN 10 en switch
- [ ] Puerto hacia usuario
- [ ] Uplink
- [ ] Modo Access/802.1Q según implementación real

## Seguridad antes de publicar

- [ ] No aparece PSK
- [ ] No aparecen contraseñas
- [ ] No aparecen claves privadas
- [ ] No aparece `psksecret ENC ...`
- [ ] No hay datos innecesarios expuestos