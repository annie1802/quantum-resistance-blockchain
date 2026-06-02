# QRB — Short pitch

> 🌐 **Language / Idioma:** **English** · [Español](resumen.md)

**A post-quantum blockchain on Ethereum.**

## In one sentence

QRB is the first Layer 2 (L2) on Ethereum designed from the ground up to resist quantum computers, letting existing users and applications protect their digital assets without leaving the Ethereum ecosystem.

## Why it matters

All of the cryptography protecting Bitcoin, Ethereum and almost every blockchain today can be broken by a large enough quantum computer. Experts estimate its arrival between 2030 and 2040.

Meanwhile, state and private actors are already storing encrypted transactions to decrypt them once such computers exist ("harvest now, decrypt later"). European (NIS2, MiCA) and US (NIST 2024, CNSA 2.0) regulation is already starting to require quantum resistance for critical infrastructure.

## How it works

QRB is an L2 on Ethereum (a model similar to Optimism or Arbitrum) that replaces classical digital signatures with post-quantum signatures standardized by NIST in 2024 (CRYSTALS-Dilithium, FALCON), while keeping full EVM compatibility.

In practice:

- Any Ethereum app migrates to QRB **without rewriting** its contracts.
- Any user moves their assets in seconds with MetaMask or an equivalent wallet.
- Assets are protected against quantum risk from the very first block.

## What sets QRB apart

Other post-quantum blockchains exist (QRL, Quranium, Cellframe, Naoris), but **they are all dedicated L1s that ask the user to leave Ethereum**. QRB is the first to start from "**I leverage Ethereum, I don't replace it**".

Five concrete differentiators:

1. **Inherits Ethereum's security and liquidity** via a native bridge.
2. **EVM-compatible**: Solidity devs migrate without rewriting contracts.
3. **Post-quantum Account Abstraction from day 1**: the cryptographic complexity is hidden from the user.
4. **NIST 2024 standards**, not legacy protocols (XMSS, Winternitz).
5. **Regulation-friendly design**: built to fit MiCA, NIS2 and institutional compliance.

## QRB token (economic model)

- **Fixed supply**: 1,000,000,000 QRB.
- **Distribution**:
  - 15% founder (4-year vesting, 12-month cliff)
  - 20% Foundation treasury
  - 30% validators and stakers (10-year emission)
  - 25% ecosystem and developer grants
  - 10% initial liquidity and public offering
- **Fees**: EIP-1559 model (base fee burned → deflation). 15% of priority fees to the treasury to sustain long-term development.
- **Value capture**: any token or app deployed on QRB pays gas in QRB. No value extracted from third-party tokens.

## Roadmap

- **Phase 0** (Q2–Q3 2026) — Whitepaper + prototype + minimal community. Cost ~€0.
- **Phase 1** (Q4 2026 – Q3 2027) — Grant-funded public testnet. €50–150K.
- **Phase 2** (Q4 2027 – Q2 2028) — Mainnet beta + audits + token under MiCA. €500K–1.5M.
- **Phase 3** (H2 2028+) — Mainnet GA, decentralized governance, self-sustaining via fees.

## Funding philosophy

**Product first, money second.** QRB explicitly rejects the ICO-before-product model of the 2017–2018 cycle:

1. We start with non-dilutive grants: NLNet (EU), Ethereum Foundation, Optimism RetroPGF, Web3 Foundation.
2. We build a demonstrable product and form a community.
3. Only then — with a real product and metrics — do we consider a token issuance, registered under a formal MiCA whitepaper with specialized legal counsel.

Slower, but it respects three things: European regulation, long-term reputation and product quality.

## Status and call to collaborate

**May 2026 — Phase 0 active.**

Actively seeking collaborators:

- 1 Rust or Go developer with blockchain client experience (Geth, Reth, Erigon).
- 1 cryptographer or PhD student with lattice / Dilithium knowledge.
- 1 frontend developer for wallet and explorer.
- 1 technical writer / communicator (ES/EN).

Any significant contribution gets an allocation from the "Ecosystem" category, on terms to be defined with the Foundation.

---

*Open source · MIT / Apache-2.0 license · Public repository.*
