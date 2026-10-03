# Running-configs

Este directorio debe contener las configuraciones finales utilizadas en cada infraestructura.

## Requisito

Los archivos deben exportarse directamente desde los dispositivos reales del laboratorio. No deben inventarse configuraciones.

## Antes de publicar

Eliminar o sustituir:
- PSK
- contraseñas
- claves privadas
- `psksecret ENC ...`
- tokens o secretos

Usar:

```text
<PSK_DEL_LAB>
<PASSWORD_DEL_USUARIO_VPN>
```

## Nombres recomendados

```text
infraestructura-1/
  fortigate-1-sanitized.conf
  fortigate-2-sanitized.conf
  isp-r1-running-config.txt

infraestructura-2/
  fortigate-sanitized.conf
  cisco-running-config.txt
  isp-running-config.txt

infraestructura-3/
  fortigate-sanitized.conf
  cisco-r2-running-config.txt
  isp-running-config.txt
  strongswan-ipsec.conf.example
```
