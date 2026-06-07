# QRB — Pitch corto

> 🌐 **Idioma / Language:** **Español** · [English](summary.en.md)

**Una blockchain post-cuántica sobre Ethereum.**

## En una frase

QRB es una línea de investigación y prototipo para una capa 2 (L2) sobre Ethereum diseñada desde el origen para ser resistente a ordenadores cuánticos, con el objetivo de permitir a usuarios y aplicaciones existentes proteger sus activos digitales sin abandonar el ecosistema Ethereum.

## Por qué importa

Toda la criptografía que protege Bitcoin, Ethereum y casi cualquier blockchain hoy puede ser rota por un ordenador cuántico suficientemente grande. El consenso experto sobre su llegada se ha contraído en los últimos dos años desde "2040 o más tarde" hasta una ventana de **2028-2032** (la fecha exacta sigue siendo incierta).

Mientras tanto, actores estatales y privados ya almacenan transacciones cifradas para descifrarlas cuando esos ordenadores existan ("harvest now, decrypt later"). La regulación europea (NIS2, MiCA) y americana (NIST 2024, CNSA 2.0) ya empieza a exigir resistencia cuántica para infraestructura crítica.

## Cómo funciona

QRB es una L2 sobre Ethereum (modelo similar a Optimism o Arbitrum) que reemplaza las firmas digitales clásicas por firmas post-cuánticas estandarizadas por NIST en 2024 (CRYSTALS-Dilithium, FALCON), manteniendo compatibilidad total con la EVM.

En la práctica:

- Cualquier app de Ethereum migra a QRB **sin reescribir** sus contratos.
- Cualquier usuario mueve sus activos en segundos con MetaMask o wallet equivalente.
- Los activos quedan protegidos frente al riesgo cuántico desde el primer bloque.

## Qué diferencia a QRB

Existen otras blockchains post-cuánticas (QRL, Quranium, Cellframe, Naoris), pero **todas son L1 propias que piden al usuario abandonar Ethereum**. QRB es la primera que parte de "**aprovecho Ethereum, no lo reemplazo**".

Cinco diferenciadores concretos:

1. **Hereda la seguridad y liquidez de Ethereum** vía bridge nativo.
2. **EVM-compatible**: los devs de Solidity migran sin reescribir contratos.
3. **Account Abstraction post-cuántica desde día 1**: la complejidad criptográfica queda oculta al usuario.
4. **Estándares NIST 2024**, no protocolos legacy (XMSS, Winternitz).
5. **Diseño regulatorio-friendly**: pensado para encajar en MiCA, NIS2 y compliance institucional.

## Token QRB (modelo económico)

- **Suministro fijo**: 1.000.000.000 QRB.
- **Reparto**:
  - 15% fundador (vesting 4 años, con cliff de 12 meses)
  - 20% tesorería de la Fundación
  - 30% validadores y stakers (emisión a 10 años)
  - 25% ecosistema y subvenciones a desarrolladores
  - 10% liquidez inicial y oferta pública
- **Comisiones**: modelo EIP-1559 (base fee quemada → deflación). 15% de las priority fees a tesorería para sostener desarrollo a largo plazo.
- **Captura de valor**: cualquier token o app desplegada en QRB paga gas en QRB. Sin extraer valor de los tokens de terceros.

## Roadmap

- **Fase 0** (Q2-Q3 2026) — Whitepaper + prototipo + comunidad mínima. Coste ~0 €.
- **Fase 1** (Q4 2026 - Q3 2027) — Testnet pública financiada por *grants*. 50-150 K €.
- **Fase 2** (Q4 2027 - Q2 2028) — Mainnet beta + auditorías + token bajo MiCA. 500 K - 1,5 M €.
- **Fase 3** (H2 2028+) — Mainnet GA, gobernanza descentralizada, autosostenible vía comisiones.

## Filosofía de financiación

**Producto primero, dinero después.** QRB rechaza explícitamente el modelo ICO-pre-producto del ciclo 2017-2018:

1. Empezamos con *grants* no dilutivos: NLNet (UE), Ethereum Foundation, Optimism RetroPGF, Web3 Foundation.
2. Construimos producto demostrable y formamos comunidad.
3. Solo entonces —con producto real y métricas— se considera la emisión de token, registrada bajo whitepaper formal MiCA y con asesoramiento legal especializado.

Más lento, pero respeta tres cosas: la regulación europea, la reputación a largo plazo y la calidad del producto.

## Estado y llamada a colaborar

**Mayo 2026 — Fase 0 activa.**

Buscando activamente colaboradores:

- 1 desarrollador Rust o Go con experiencia en clientes blockchain (Geth, Reth, Erigon).
- 1 criptógrafo o doctorando con conocimiento de retículos / Dilithium.
- 1 desarrollador frontend para wallet y explorer.
- 1 *technical writer* / comunicador (ES/EN).

Cualquier contribución significativa accede a asignación de la categoría "Ecosistema" en términos a definir con la Fundación.

---

*Proyecto open source · Licencia dual MIT / Apache-2.0 · Repositorio público en GitHub.*
