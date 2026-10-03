# Práctica 2 — Documentación de las tres infraestructuras

## Seguridad de Redes

Esta documentación describe las tres topologías implementadas para la **Práctica 2 de Seguridad de Redes**. El laboratorio fue desarrollado en GNS3 utilizando FortiGate, Cisco, Ubuntu Client, Ubuntu Server, segmentación mediante VLAN, políticas de firewall y distintos tipos de VPN.

El objetivo general de la práctica es demostrar cómo diferentes arquitecturas de seguridad pueden controlar y proteger la comunicación entre usuarios, redes remotas y servidores.

> **Video de demostración:** https://youtu.be/vsI622JK9Ig

---

# 1. Objetivo general

Diseñar, implementar y validar tres infraestructuras de red orientadas a seguridad, utilizando firewalls FortiGate, un router Cisco, sistemas Ubuntu y mecanismos VPN para controlar el acceso entre redes.

Los escenarios permiten demostrar:

- segmentación mediante VLAN;
- direccionamiento IP;
- DHCP;
- políticas de firewall;
- VPN IPsec Site-to-Site;
- interoperabilidad FortiGate–Cisco;
- publicación de servicios mediante Virtual IP;
- acceso HTTPS;
- acceso SSH restringido;
- VPN de acceso remoto;
- pruebas de conectividad y validación.

---

# 2. Herramientas utilizadas

| Herramienta / equipo | Función |
|---|---|
| GNS3 | Simulación y construcción de las topologías |
| FortiGate VM | Firewall, VPN, políticas y control de acceso |
| Cisco IOS | Router utilizado en la Infraestructura 2 |
| Ubuntu Client | Equipo utilizado para realizar las pruebas |
| Ubuntu Server | Servidor HTTPS/SSH de las redes remotas |
| VMware | Plataforma utilizada para las máquinas virtuales |
| StrongSwan | Cliente IPsec utilizado en la VPN remota |

---

# 3. Infraestructura 1 — FortiGate ↔ FortiGate

## 3.1 Topología

![Topología real de la Infraestructura 1](../images/infraestructura-1/01-topologia-real.png)

Esta infraestructura utiliza **dos firewalls FortiGate** comunicados a través de una red que representa el ISP. El FortiGate-1 protege la red de usuarios y el FortiGate-2 protege la red donde se encuentra el servidor Ubuntu.

El propósito principal es establecer una **VPN Site-to-Site FortiGate ↔ FortiGate** para que el tráfico entre ambas redes viaje mediante el túnel IPsec.

## 3.2 Componentes

- Cloud / conexión externa.
- ISP.
- FortiGate-1.
- FortiGate-2.
- SW-USERS.
- Ubuntu Client.
- Ubuntu Server.

## 3.3 Direccionamiento principal

| Elemento | Dirección |
|---|---|
| Red USERS | 10.21.39.0/25 |
| Gateway USERS | 10.21.39.1 |
| Ubuntu Client | 10.21.39.10/25 |
| FortiGate-1 WAN | 198.51.100.22/30 |
| ISP hacia FGT1 | 198.51.100.21/30 |
| ISP hacia FGT2 | 203.0.113.37/30 |
| FortiGate-2 WAN | 203.0.113.38/30 |
| Red del servidor | 10.21.39.128/28 |
| Ubuntu Server | 10.21.39.130/28 |

## 3.4 Funcionamiento

El Ubuntu Client pertenece a la red de usuarios. Su tráfico llega primero al FortiGate-1. Cuando intenta comunicarse con la red del servidor, el FortiGate identifica que el destino pertenece a la red remota protegida por la VPN.

El tráfico es enviado a través del túnel Site-to-Site hacia el FortiGate-2. El segundo firewall recibe el tráfico, aplica las políticas correspondientes y lo entrega al Ubuntu Server.

El camino lógico es:

```text
Ubuntu Client
      |
   SW-USERS
      |
 FortiGate-1
      |
   VPN IPsec
      |
 FortiGate-2
      |
 Ubuntu Server
```

## 3.5 Controles de seguridad

La infraestructura aplica:

- segmentación de usuarios mediante VLAN 10;
- políticas de firewall;
- túnel IPsec Site-to-Site;
- control del tráfico entre redes;
- acceso al servidor únicamente a través de la ruta autorizada.

La VPN utilizada se identifica como:

```text
VPN-FGT1-FGT2
```

## 3.6 Pruebas

Desde Ubuntu Client:

```bash
ip addr show ens33
ping -c 4 10.21.39.130
sudo busybox traceroute -n 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

La prueba HTTPS devolvió:

```text
HTTP/1.0 200 OK
Servidor HTTPS - Seguridad de Redes
Ubuntu Server 10.21.39.130
```

La validación principal consistió en desactivar temporalmente el túnel VPN. Con la VPN desactivada, la comunicación con el servidor deja de funcionar. Al volver a activar el túnel, la conectividad se restablece.

Esto demuestra que la comunicación entre las dos redes depende de la VPN Site-to-Site.

---

# 4. Infraestructura 2 — FortiGate ↔ Cisco

## 4.1 Topología

![Topología lógica de la Infraestructura 2](../images/infraestructura-2/topologia-logica.svg)

En esta infraestructura se sustituye uno de los FortiGate por un dispositivo Cisco. El objetivo es comprobar la interoperabilidad de una **VPN Site-to-Site entre FortiGate y Cisco**.

La arquitectura contiene una red de usuarios, un FortiGate, un ISP, un router Cisco R2 y un servidor Ubuntu.

## 4.2 Componentes

- Cloud / ISP.
- FortiGate-1.
- Cisco R2.
- SW-USERS.
- Ubuntu Client.
- Ubuntu Server.

## 4.3 Direccionamiento observado

| Elemento | Dirección |
|---|---|
| FortiGate port1 | 198.51.100.22/30 |
| Gateway ISP | 198.51.100.21 |
| VLAN10-USERS | 10.21.39.1/25 |
| Red USERS | 10.21.39.0/25 |
| Red remota | 10.21.39.128/28 |
| Cisco R2 WAN | 203.0.113.38 |
| Cisco R2 LAN | 10.21.39.129 |
| Ubuntu Server | 10.21.39.130 |

La ruta remota observada en FortiGate fue:

```text
S 10.21.39.128/28 via VPN-FGT1-CISCO tunnel 203.0.113.38
```

## 4.4 Funcionamiento

Cuando el cliente necesita acceder al servidor remoto, el FortiGate reconoce la red de destino y dirige el tráfico hacia:

```text
VPN-FGT1-CISCO
```

El túnel IPsec transporta el tráfico hasta Cisco R2. El router Cisco descifra el tráfico y lo envía a la red del servidor.

El flujo general es:

```text
Ubuntu Client
      |
   SW-USERS
      |
 FortiGate-1
      |
 VPN-FGT1-CISCO
      |
    Cisco R2
      |
 Ubuntu Server
```

Este escenario demuestra que IPsec puede utilizarse entre equipos de fabricantes diferentes siempre que los parámetros de negociación sean compatibles.

## 4.5 Validación en Cisco

Los comandos principales utilizados son:

```text
show ip interface brief
show crypto isakmp sa
show crypto ipsec sa
```

En la negociación IKE se observó un estado:

```text
QM_IDLE
ACTIVE
```

Esto indica que la asociación de seguridad se encontraba establecida.

`show crypto ipsec sa` permite verificar los contadores de paquetes cifrados y descifrados, proporcionando evidencia de que el tráfico realmente atraviesa IPsec.

## 4.6 Pruebas desde el cliente

```bash
ip addr show ens33
ping -c 4 10.21.39.130
sudo busybox traceroute -n 10.21.39.130
wget --no-check-certificate -T 5 -S -O- https://10.21.39.130/
```

Durante el traceroute se observó que un salto intermedio podía no responder a ICMP, pero el destino final `10.21.39.130` fue alcanzado correctamente.

La prueba HTTPS también devolvió:

```text
HTTP/1.0 200 OK
```

## 4.7 Resultado

La Infraestructura 2 permitió validar:

- interoperabilidad FortiGate–Cisco;
- negociación IKE;
- túnel IPsec;
- comunicación entre redes privadas;
- acceso HTTPS al servidor remoto;
- dependencia de la comunicación respecto al túnel VPN.

---

# 5. Infraestructura 3 — HTTPS público y SSH mediante VPN remota

## 5.1 Topología

![Topología lógica de la Infraestructura 3](../images/infraestructura-3/topologia-logica.svg)

La tercera infraestructura tiene un objetivo distinto a los dos primeros escenarios.

En lugar de utilizar únicamente una VPN Site-to-Site, se aplican dos formas de acceso:

1. **HTTPS puede accederse sin VPN.**
2. **SSH solamente puede utilizarse mediante una VPN de acceso remoto.**

De esta manera se separa un servicio que puede publicarse externamente de otro servicio administrativo que debe permanecer restringido.

## 5.2 Componentes

- Cloud / ISP.
- FortiGate.
- red de usuarios.
- Ubuntu Client.
- red del servidor.
- Ubuntu Server.
- cliente IPsec StrongSwan.

## 5.3 Direccionamiento

| Elemento | Dirección |
|---|---|
| Red usuarios | 10.21.39.0/25 |
| Gateway usuarios | 10.21.39.1 |
| Ubuntu Client | 10.21.39.10/25 |
| FortiGate WAN | 198.51.100.22/30 |
| Gateway ISP | 198.51.100.21 |
| Red servidor | 10.21.39.128/28 |
| Gateway servidor | 10.21.39.129 |
| Ubuntu Server | 10.21.39.130/28 |
| Pool VPN remota | 10.99.99.10 - 10.99.99.20 |

## 5.4 Publicación HTTPS mediante Virtual IP

El servicio HTTPS se publica mediante:

```text
WEB-HTTPS-VIP
```

Configuración documentada:

```text
IP externa: 198.51.100.22
IP interna: 10.21.39.130
Protocolo: TCP
Puerto externo: 443
Puerto interno: 443
```

La función del VIP es traducir el tráfico recibido en la dirección pública del FortiGate hacia el servidor web interno.

La política asociada es:

```text
WAN-to-WEB-HTTPS
```

con servicio HTTPS y NAT deshabilitado en la política.

## 5.5 VPN de acceso remoto

El acceso SSH utiliza:

```text
VPN-REMOTE-SSH
```

Grupo autorizado:

```text
VPN-USERS
```

Pool asignado:

```text
10.99.99.10 - 10.99.99.20
```

Red protegida:

```text
10.21.39.128/28
```

La política del firewall limita este acceso al servicio SSH.

## 5.6 Flujo HTTPS

```text
Cliente
   |
Internet / ISP
   |
198.51.100.22:443
   |
WEB-HTTPS-VIP
   |
10.21.39.130:443
   |
Ubuntu Server
```

El usuario puede acceder al servicio web sin establecer la VPN remota.

Prueba:

```bash
wget --no-check-certificate -T 5 -S -O- https://198.51.100.22/
```

Resultado esperado:

```text
HTTP/1.0 200 OK
```

## 5.7 Flujo SSH

Sin VPN:

```bash
ssh adrian@10.21.39.130
```

La conexión directa no debe establecerse.

Después se activa la VPN:

```bash
sudo ipsec up VPN-REMOTE-SSH
```

Una vez establecida, el cliente recibe una dirección virtual del pool y puede volver a ejecutar:

```bash
ssh adrian@10.21.39.130
```

El acceso SSH debe funcionar a través del túnel VPN.

## 5.8 Resultado

La Infraestructura 3 demuestra una separación clara entre:

- **servicio público:** HTTPS;
- **servicio administrativo protegido:** SSH.

Esto permite aplicar el principio de menor exposición, manteniendo el acceso administrativo detrás de un mecanismo VPN.

---

# 6. Comparación de las tres infraestructuras

| Característica | Infraestructura 1 | Infraestructura 2 | Infraestructura 3 |
|---|---|---|---|
| Tipo principal | Site-to-Site | Site-to-Site | Acceso remoto + publicación |
| Extremo 1 | FortiGate | FortiGate | Cliente remoto |
| Extremo 2 | FortiGate | Cisco | FortiGate |
| Protocolo VPN | IPsec | IPsec | IPsec |
| HTTPS | Por red privada/VPN | Por red privada/VPN | Publicado mediante VIP |
| SSH | No es objetivo principal | No es objetivo principal | Solo mediante VPN |
| Interoperabilidad | FortiGate–FortiGate | FortiGate–Cisco | StrongSwan–FortiGate |
| Prueba principal | VPN ON/OFF | IKE/IPsec + tráfico | HTTPS sin VPN / SSH con VPN |

---

# 7. Validación general

Las pruebas realizadas permiten comprobar distintos niveles de funcionamiento.

## Capa de red

```bash
ip addr show ens33
ping -c 4 <DESTINO>
sudo busybox traceroute -n <DESTINO>
```

Permiten verificar direccionamiento, conectividad y recorrido del tráfico.

## Capa de aplicación

```bash
wget --no-check-certificate -T 5 -S -O- https://<DESTINO>/
```

Permite comprobar que HTTPS está disponible y que el servidor responde.

## VPN Cisco

```text
show crypto isakmp sa
show crypto ipsec sa
```

Permiten validar negociación y tráfico IPsec.

## VPN remota

```bash
sudo ipsec up VPN-REMOTE-SSH
sudo ipsec statusall
```

Permiten verificar el establecimiento de la VPN de acceso remoto.

---

# 8. Consideraciones de seguridad

Durante la documentación y publicación del laboratorio no deben exponerse:

- contraseñas;
- claves PSK;
- claves privadas;
- valores `psksecret ENC ...`;
- credenciales de usuarios;
- secretos de autenticación.

La documentación debe mostrar únicamente la información necesaria para demostrar la arquitectura y las pruebas.

---

# 9. Conclusiones

La Práctica 2 permitió implementar tres escenarios que representan formas diferentes de proteger la comunicación de red.

La **Infraestructura 1** demuestra una VPN Site-to-Site entre dos firewalls FortiGate y confirma que la comunicación entre redes remotas depende del túnel.

La **Infraestructura 2** demuestra interoperabilidad entre FortiGate y Cisco utilizando IPsec, verificando tanto la negociación IKE como el tráfico cifrado.

La **Infraestructura 3** aplica un modelo diferente: el servicio HTTPS se publica hacia el exterior mediante un Virtual IP, mientras que SSH permanece restringido a usuarios conectados mediante una VPN de acceso remoto.

En conjunto, las tres infraestructuras permiten aplicar conceptos de segmentación, control de acceso, publicación segura de servicios, VPN IPsec, interoperabilidad y validación práctica de políticas de seguridad.

---

# 10. Video de demostración

La demostración de las tres infraestructuras se encuentra en un único video:

**YouTube:** https://youtu.be/vsI622JK9Ig
