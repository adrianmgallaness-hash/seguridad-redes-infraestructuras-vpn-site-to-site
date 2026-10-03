# Pruebas y validaciones

## Infraestructura 1

### IP del cliente
```bash
ip addr show ens33
```

Esperado: `10.21.39.10/25`.

### Ping al servidor
```bash
ping -c 4 10.21.39.130
```

Validado: comunicación exitosa con VPN activa.

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

Validado:
```text
HTTP/1.0 200 OK
Servidor HTTPS - Seguridad de Redes
Ubuntu Server 10.21.39.130
```

### Prueba VPN OFF
Desactivar temporalmente el túnel Site-to-Site y repetir:

```bash
ping -c 4 10.21.39.130
```

Debe fallar.

### Prueba VPN ON
Reactivar el túnel y repetir el ping. Debe volver a funcionar.

---

## Infraestructura 2

Cliente:

```bash
ip addr
ping -c 4 <IP_SERVIDOR>
sudo busybox traceroute -n <IP_SERVIDOR>
wget --no-check-certificate -T 5 -S -O- https://<IP_SERVIDOR>/
```

Cisco:

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
show ip nat translations
```

Validación obligatoria: VPN ON → funciona; VPN OFF → falla; VPN ON → vuelve a funcionar.

---

## Infraestructura 3

### HTTPS sin VPN
```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

Validado: `HTTP/1.0 200 OK`.

### SSH sin VPN
```bash
ssh adrian@10.21.39.130
```

Validado: no hay acceso directo.

### Establecer VPN
```bash
sudo ipsec up VPN-REMOTE-SSH
```

### Estado
```bash
sudo ipsec statusall
```

Validado: IKE SA y CHILD SA establecidos; IP virtual `10.99.99.10`.

### SSH con VPN
```bash
ssh adrian@10.21.39.130
```

Validado: acceso exitoso.
