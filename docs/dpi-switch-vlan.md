# DPI, Switch, VLAN y seguridad básica

Este documento se agregó para evitar observaciones de documentación incompleta sobre controles de inspección y segmentación de capa 2.

## 1. DPI / inspección profunda

La documentación de DPI debe demostrar **dónde se aplica la inspección y qué tráfico protege**, no solo mencionar que existe.

### Evidencias que deben mostrarse

En FortiGate:

1. Abrir `Policy & Objects → Firewall Policy`.
2. Abrir la política donde se aplica la inspección.
3. Mostrar los perfiles de seguridad activos.
4. Si se utiliza inspección SSL/SSH, mostrar el perfil aplicado.
5. Si se utiliza IPS, mostrar el perfil correspondiente.
6. Mostrar logs/eventos que prueben que el tráfico fue inspeccionado.

> **Importante:** el nombre exacto del perfil DPI/IPS debe tomarse de la configuración real del laboratorio. No se documenta un nombre inventado.

### Qué explicar en el informe

La inspección profunda permite que FortiGate analice el contenido del tráfico permitido por una política, además de revisar únicamente IP, puerto y protocolo. Esto permite aplicar controles de seguridad adicionales sobre las sesiones que atraviesan el firewall.

### Capturas recomendadas

Guardar en:

```text
images/controles/
01-dpi-policy.png
02-dpi-security-profile.png
03-dpi-log.png
```

---

## 2. Switch y VLAN 10

La VLAN 10 se utiliza para separar lógicamente la red de usuarios.

Red documentada:

```text
VLAN 10 USERS
Red: 10.21.39.0/25
Cliente observado: 10.21.39.10/25
```

El switch debe documentarse indicando claramente:

- puerto conectado al usuario;
- puerto conectado al dispositivo de capa 3/FortiGate;
- modo Access o 802.1Q según corresponda;
- VLAN asignada;
- propósito de la VLAN.

### Comprobaciones

En el cliente:

```bash
ip addr
ip route
```

En FortiGate se puede comprobar la presencia del cliente mediante:

```text
get system arp
```

Durante la validación de la Infraestructura 1 se observó:

```text
10.21.39.10    VLAN10-USERS
```

### Seguridad básica del switch

La documentación debe indicar los controles realmente utilizados. Dependiendo del dispositivo/switch del laboratorio pueden incluir:

- puertos no utilizados deshabilitados;
- separación de tráfico mediante VLAN;
- puertos de usuario configurados únicamente para su VLAN;
- trunk limitado a las VLAN necesarias;
- evitar VLANs innecesarias.

> Si se utiliza el switch Ethernet integrado de GNS3, deben documentarse los modos de puerto configurados en la interfaz gráfica del nodo. No se debe afirmar que existe Port Security de Cisco si el switch usado no implementa esa función.

### Capturas recomendadas

```text
images/controles/
04-switch-vlan10.png
05-switch-port-user.png
06-switch-uplink.png
```

---

## 3. Evidencia mínima para la entrega

Para evitar la observación “DPI no documentado / Switch y VLAN no documentados”, la entrega final debe contener:

- captura de la política donde se aplica DPI/perfiles de seguridad;
- captura del perfil utilizado;
- captura o log de inspección;
- captura del switch mostrando VLAN 10;
- identificación del puerto de usuario;
- identificación del uplink;
- explicación breve del propósito de VLAN 10;
- prueba de que el cliente obtiene una IP de esa VLAN.
