# Controlar tu PC (Windows) desde el móvil

Guía para conectarte a tu ordenador Windows desde el móvil y mandarle comandos
de forma segura, usando **Tailscale + OpenSSH**.

> ⚠️ Importante: esta configuración se hace **una sola vez**, físicamente en el
> PC. Una vez hecha, podrás conectarte desde el móvil estés donde estés
> (siempre que el PC esté encendido y con internet).

---

## Resumen de cómo queda

| Lo que quieres hacer | Herramienta | ¿Depende del PC? |
|---|---|---|
| Programar este proyecto día a día | Claude Code on the web | No |
| Mandar comandos a tu PC desde el móvil | Tailscale + SSH | Sí (debe estar encendido) |

---

## Parte 1 — Activar SSH en Windows (en el PC)

1. Abre **Configuración** → **Sistema** → **Características opcionales**.
2. Pulsa **Agregar una característica**.
3. Busca **Servidor de OpenSSH** y pulsa **Instalar**.
4. Abre **PowerShell como Administrador** y ejecuta:

   ```powershell
   # Iniciar el servicio SSH
   Start-Service sshd

   # Que arranque solo al encender el PC
   Set-Service -Name sshd -StartupType 'Automatic'

   # Comprobar que está corriendo
   Get-Service sshd
   ```

5. (Opcional) Mira tu nombre de usuario de Windows, lo necesitarás para conectarte:

   ```powershell
   whoami
   ```

---

## Parte 2 — Instalar Tailscale (en el PC y en el móvil)

Tailscale crea una red privada entre tus dispositivos, sin abrir puertos ni
exponer tu PC a internet. Es gratis para uso personal.

### En el PC (Windows)
1. Descarga Tailscale desde https://tailscale.com/download/windows
2. Instálalo y **inicia sesión** (puedes usar tu cuenta de Google).
3. Una vez conectado, anota la **dirección Tailscale** del PC. La ves en el
   panel de Tailscale o ejecutando en PowerShell:

   ```powershell
   tailscale ip -4
   ```

   Será algo tipo `100.x.x.x`.

### En el móvil
1. Instala la app **Tailscale** (Google Play / App Store).
2. **Inicia sesión con la MISMA cuenta** que usaste en el PC.
3. Activa la VPN cuando te lo pida. Listo: el móvil y el PC ya se "ven".

---

## Parte 3 — Conectarte desde el móvil

Necesitas una app de terminal SSH en el móvil. Recomendadas:

- **Android:** Termux o JuiceSSH
- **iPhone:** Termius o Blink Shell

Para conectarte, usa:

```bash
ssh TU_USUARIO_WINDOWS@100.x.x.x
```

- `TU_USUARIO_WINDOWS` = lo que devolvió `whoami` (sin la parte del dominio).
- `100.x.x.x` = la IP de Tailscale de tu PC.

La primera vez te pedirá confirmar la huella y luego tu contraseña de Windows.
¡Ya estás dentro! Cualquier comando que escribas se ejecuta en tu PC.

---

## Parte 4 (opcional pero recomendada) — Entrar sin contraseña con clave SSH

Más cómodo y más seguro que escribir la contraseña cada vez.

1. En el **móvil** (en la terminal), genera una clave:

   ```bash
   ssh-keygen -t ed25519
   ```

   Pulsa Enter a todo (puedes dejar la passphrase vacía).

2. Copia tu clave pública. Muéstrala con:

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

3. En el **PC (PowerShell)**, pega esa clave en el archivo de claves
   autorizadas (cambia `LA_CLAVE_PUBLICA` por lo que copiaste):

   ```powershell
   Add-Content -Path "$env:USERPROFILE\.ssh\authorized_keys" -Value "LA_CLAVE_PUBLICA"
   ```

   Si la carpeta `.ssh` no existe, créala antes con:

   ```powershell
   mkdir "$env:USERPROFILE\.ssh"
   ```

A partir de ahora, `ssh TU_USUARIO@100.x.x.x` entra directo, sin contraseña.

---

## Flujo de trabajo recomendado

- **Para tocar este proyecto:** sigue usando Claude Code on the web desde el
  móvil. Yo hago los cambios y los subo a GitHub. Para tener la copia local
  actualizada en tu PC: `git pull`.
- **Para mandar comandos / ejecutar cosas en tu PC:** conéctate por SSH como
  arriba.

---

## Consejos de seguridad

- No expongas el puerto SSH directamente a internet: con Tailscale **no hace
  falta**, y es mucho más seguro.
- Usa una contraseña fuerte en tu cuenta de Windows.
- Si pierdes el móvil, entra en el panel de Tailscale desde otro dispositivo y
  **revoca** ese dispositivo.

---

## Si algo falla

- **No conecta el SSH:** comprueba que el servicio `sshd` está corriendo
  (`Get-Service sshd`) y que ambos dispositivos aparecen "conectados" en
  Tailscale.
- **Pide contraseña aunque pusiste clave:** revisa que la clave pública esté
  bien pegada en `authorized_keys` y sin saltos de línea extra.
- **El PC se duerme:** en Windows, Configuración → Sistema → Inicio/apagado,
  pon la suspensión en "Nunca" si quieres acceso 24/7.
