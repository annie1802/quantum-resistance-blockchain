# QRB — Quantum-Resistance Blockchain

> _"All of the internet from the past 40 years will become an open book, and there is nothing you can do to save the past."_
>
> — **Gilles Brassard**, co-inventor of quantum cryptography (BB84, 1984), Turing Award 2026

**QRB is the first Layer 2 blockchain on Ethereum designed from day one to be resistant to quantum-computer attacks** — covering both **authentication** (post-quantum signatures via ML-DSA-65, NIST FIPS 204) and **confidentiality** (post-quantum privacy layer built on STARKs, Phase 3+ vision).

![Status](https://img.shields.io/badge/status-Phase%200-0b3d91)
![License](https://img.shields.io/badge/license-MIT-green)
![Whitepaper](https://img.shields.io/badge/whitepaper-v0.2-orange)
![Made with](https://img.shields.io/badge/made%20with-Python%20%2B%20Dilithium-blueviolet)

---

## Why now

In **April 2026**, an independent researcher used a publicly accessible cloud quantum computer to break a real elliptic-curve cryptography key, winning Project Eleven's _Q-Day Prize_. Google now estimates that breaking Bitcoin's ECDSA-256 requires **fewer than 500,000 physical qubits** — down from 20 million in 2019. Caltech researchers showed it could potentially be done with just **10,000 qubits** using atomic-architecture systems. Current commercial quantum computers already have 1,000-2,000 qubits.

Vitalik Buterin (Ethereum founder): _"Crypto has until 2028 to avoid quantum collapse."_

Google has moved its internal post-quantum migration deadline to **2029**, six years ahead of the NIST 2035 standard.

In January 2026, Jefferies removed 10% of its Bitcoin allocation from model portfolios citing quantum risk explicitly.

The biggest cryptographic robbery in history is no longer hypothetical. **It has begun.**

---

## What QRB does differently

| Project | PQ auth | PQ privacy | EVM | Account Abstraction | QKD-ready |
|---|:-:|:-:|:-:|:-:|:-:|
| Bitcoin / Ethereum L1 | ❌ | ❌ | ✅ Ethereum | partial | ❌ |
| QRL / Zond | ✅ | ❌ | partial | ❌ | ❌ |
| Quranium | ✅ | ❌ | partial | ❌ | ❌ |
| Aleo | ❌ (SNARK) | ✅ but NOT PQ-safe | ❌ | ❌ | ❌ |
| Aztec | ❌ (SNARK) | ✅ but NOT PQ-safe | partial | ✅ | ❌ |
| Monero | ❌ | ✅ but NOT PQ-safe | ❌ | ❌ | ❌ |
| **QRB** | **✅ ML-DSA-65** | **✅ STARKs + lattice** | **✅** | **✅** | **✅ (planned)** |

**QRB is the only known project combining all five capabilities.**

The privacy chains in the market today (Aleo, Aztec, Monero) build on SNARKs or non-PQ commitments — meaning their privacy is **broken at long horizons** under harvest-now-decrypt-later. QRB is the first project to call this out explicitly and to design the privacy layer on top of STARKs (hash-based, natively post-quantum).

---

## Repository contents

```
quantum-resistance-blockchain/
├── whitepaper/
│   ├── whitepaper-v0.2.md         Source markdown (full whitepaper, Spanish)
│   ├── whitepaper-v0.2.pdf        24-page PDF rendering for distribution
│   └── _build_pdf.js              Reproducible PDF build script (Node + Chrome)
├── prototype/
│   ├── qrb/                       Python package with the prototype
│   ├── qrb_cli.py                 Command-line interface
│   ├── tests/                     End-to-end tests
│   └── README.md                  Prototype setup and usage
├── marketing/
│   └── launch-kit.md              Public launch materials
├── resumen.md                     ~700-word pitch (Spanish)
├── README.md                      This file
└── LICENSE                        MIT
```

---

## Quick start — run the prototype

The prototype is a minimal Python blockchain that demonstrates ML-DSA-65 signatures, account-based state, signed blocks and persistence. It runs on your laptop, single node, no networking.

**Requirements**: Python 3.10+

```bash
cd prototype
python -m venv .venv

# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt
python tests/test_basic.py
```

You should see 5 tests pass.

Then play with the CLI:

```bash
python qrb_cli.py wallet create --name founder
python qrb_cli.py wallet create --name alice
python qrb_cli.py chain init --founder founder --supply 1000000000
python qrb_cli.py wallet list
# copy alice's address from the listing
python qrb_cli.py tx send --from founder --to <alice-address> --amount 1000
python qrb_cli.py chain mine --proposer founder
python qrb_cli.py wallet balance --name alice
python qrb_cli.py chain block --index 1
```

The blocks and state are persisted as JSON in `.qrb-data/` — open the files to inspect the ML-DSA-65 signatures (~3.3 KB each) and see how they compose into a chain.

See [`prototype/README.md`](prototype/README.md) for full prototype documentation.

---

## Roadmap

| Phase | Period | Milestones | Funding |
|-------|--------|-----------|---------|
| **0 — Validation** | Q2-Q3 2026 | Whitepaper · Python prototype with Dilithium signatures · Public repo · Initial community | Self-funded |
| **1 — Public testnet** | Q4 2026 - Q3 2027 | Grants (NLNet, Ethereum Foundation, Optimism RetroPGF) · Devnet · Public testnet · SDK · 5-10 dApp demos · Ethereum bridge | €100-250K (grants) |
| **2 — Mainnet beta** | Q4 2027 - Q2 2028 | Audits · Production bridge · MiCA-registered token · DEX listings · 50+ contracts | €500K-2M (seed + token) |
| **3 — GA + Privacy layer** | H2 2028 - 2030 | Sequencer decentralization · STARK confidentiality · Stealth addresses · QKD institutional pilots · Optimistic → ZK rollup migration | Self-sustaining via fees |

Read the full economic and technical model in [`whitepaper/whitepaper-v0.2.pdf`](whitepaper/whitepaper-v0.2.pdf).

---

## Funding philosophy

**Product first, money second.** QRB explicitly rejects the ICO-pre-product model.

1. Non-dilutive grants first: NLNet, Ethereum Foundation, Optimism RetroPGF, Web3 Foundation, Horizon Europe.
2. Then demonstrable product + community.
3. **Only then** — token issuance registered under MiCA with proper legal counsel and a notified whitepaper.

🚫 No ICO before product. 🚫 No vaporware. 🚫 No promises without code.

---

## Looking for collaborators

QRB is actively recruiting for Phase 0 and early Phase 1:

- **1 Rust / Go developer** with blockchain client experience (Geth, Reth, Erigon).
- **1 cryptographer or PhD student** with lattice / Dilithium / STARK expertise.
- **1 frontend developer** for wallet and block explorer.
- **1 technical writer / communicator** (Spanish/English).

Significant contributors receive an allocation from the **Ecosystem & Grants** category (25% of total supply, terms negotiated with the QRB Foundation upon constitution).

Interested? Open an issue, send a pull request, or DM [@QRB_PQ on X](https://x.com/QRB_PQ).

---

## How to cite

If you reference QRB in academic work, please cite:

> QRB Project. _Quantum-Resistance Blockchain: a post-quantum L2 on Ethereum_. Whitepaper v0.2. May 2026. https://github.com/Fiyiware/quantum-resistance-blockchain

---

## License

Released under the [MIT License](LICENSE) for maximum compatibility with the open-source ecosystem.

---

## Acknowledgments

- **Charles Bennett and Gilles Brassard** for inventing quantum cryptography in 1984 and receiving the 2026 Turing Award.
- **The NIST PQC team** for standardizing ML-DSA, FN-DSA, SLH-DSA and ML-KEM (FIPS 203-206).
- **Peter Shor** for proving in 1994 what the world is only now waking up to.
- **Vitalik Buterin and the Ethereum Foundation** for the open L2 ecosystem this project builds on.
- **StarkWare and the broader STARK research community** for showing that post-quantum-secure ZK proofs are practical today.
- **Project Eleven** for the Q-Day Prize that put quantum risk on the public agenda.

---

🛡️ **Help build the cryptographic infrastructure the world will need in the next decade.**
