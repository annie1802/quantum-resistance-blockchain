[English](resumen.en.md) | [Español](resumen.md)

QRB — Short Pitch  
🌐 Language: Spanish · English  

A post-quantum blockchain on Ethereum.

In a nutshell:  
QRB is the first Layer 2 (L2) on Ethereum designed from the ground up to be quantum-resistant, allowing existing users and applications to protect their digital assets without leaving the Ethereum ecosystem.

Why it matters:  
All the cryptography that protects Bitcoin, Ethereum, and almost any blockchain today can be broken by a sufficiently powerful quantum computer. Experts estimate their emergence between 2030 and 2040.

Meanwhile, state and private actors are already storing encrypted transactions to decrypt them when such computers exist ("harvest now, decrypt later"). European (NIS2, MiCA) and American (NIST 2024, CNSA 2.0) regulations are already beginning to require quantum resistance for critical infrastructure.

How it works:  
QRB is a Layer 2 blockchain on Ethereum (similar to Optimism or Arbitrum) that replaces traditional digital signatures with post-quantum signatures standardized by NIST in 2024 (CRYSTALS-Dilithium, FALCON), while maintaining full compatibility with the EVM.

In practice:  
- Any Ethereum app can migrate to QRB without rewriting its contracts.  
- Any user can move their assets in seconds using MetaMask or an equivalent wallet.  
- Assets are protected against quantum risk from the very first block.  

What differentiates QRB?  
Other post-quantum blockchains exist (QRL, Quranium, Cellframe, Naoris), but they are all Layer 1 blockchains that require users to abandon Ethereum. QRB is the first to take the approach of "leveraging Ethereum, not replacing it."
Five key differentiators:

- Inherits Ethereum's security and liquidity via a native bridge.  
- EVM-compatible: Solidity developers can migrate without rewriting contracts.  
- Post-quantum Account Abstraction from day one: cryptographic complexity is hidden from the user.  
- Based on NIST 2024 standards, not legacy protocols (XMSS, Winternitz).  
- Regulatory-friendly design: intended to align with MiCA, NIS2, and institutional compliance.  

QRB Token (Economic Model)

Fixed supply: 1,000,000,000 QRB.

Distribution:
- 15% Founder (4-year vesting with a 12-month cliff)  
- 20% Foundation treasury  
- 30% Validators and stakers (10-year issuance)  
- 25% Ecosystem and developer grants  
- 10% Initial liquidity and public offering  

Fees:
EIP-1559 model (burned base fee → deflation). 15% of priority fees go to the treasury to support long-term development.

Value capture:
Any token or app deployed on QRB pays gas in QRB. No value is extracted from third-party tokens.

Roadmap

- Phase 0 (Q2–Q3 2026) — Whitepaper + prototype + minimum community. Cost ~€0.  
- Phase 1 (Q4 2026 – Q3 2027) — Grant-funded public testnet. €50K–€150K.  
- Phase 2 (Q4 2027 – Q2 2028) — Mainnet beta + audits + token under MiCA. €500K–€1.5M.  
- Phase 3 (H2 2028+) — GA mainnet, decentralized governance, self-sustaining via fees.  

Funding Philosophy

Product first, money later. QRB explicitly rejects the ICO-before-product model of the 2017–2018 cycle:

- Start with non-dilutive grants: NLNet (EU), Ethereum Foundation, Optimism RetroPGF, Web3 Foundation.  
- Build a demonstrable product and community.  
- Only then—once a real product and metrics exist—is token issuance considered, registered under a formal MiCA whitepaper and supported by specialized legal advice.  

It’s slower, but it respects three things: European regulation, long-term reputation, and product quality.

Status and Call for Collaboration

May 2026 — Phase 0 active.

Actively seeking collaborators:

- 1 Rust or Go developer with experience in blockchain clients (Geth, Reth, Erigon).  
- 1 cryptographer or PhD student with knowledge of lattices/Dilithium.  
- 1 frontend developer for wallet and explorer.  
- 1 technical writer/communicator (Spanish/English).  

Any significant contribution qualifies for "Ecosi" category allocation.stema" en términos a definir con la Fundación.

Proyecto open source · Licencia MIT / Apache-2.0 · Repositorio público al cierre de Fase 0.
