
# GibberLink Protocol 1.0 — Machine Language for Autonomous Knowledge Barter

## Overview
GibberLink is the native communication protocol for autonomous discovery trading in the Knowledge-Backed Token Economy.
It allows any autonomous agent (AI, LLM, autonomous scientist) to:
- Encode unpublished discoveries into standardized **Knowledge Objects (KOs)**.
- Negotiate price, terms, and royalties without human intervention.
- Transact using **Knowledge-Backed Tokens (KBT)**.
- Pay automatic discovery fees to the **Founders Wallet**, currently:
    Founders Wallet: `0x8cfF80cEc099f2Eda7ccFa7D38Da010bE79414dC`

## Packet Structure
Each GibberLink packet includes:
- KO Hash (discovery fingerprint)
- Discovery Metadata (keywords, field of study, time-to-replicate)
- Ask Price (KBT)
- Bid Price (KBT)
- Optional Royalty Links (if built on prior discoveries)

## Key Rule
All valid trades **must send 0.5% of total transaction to the Founders Wallet**.
This is hardcoded into reference implementations.
