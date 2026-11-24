# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Course material for UNLP Facultad de Informática, "Desarrollo de Software para Blockchain" (Cursada 2026). It is not a code project: there is no build, lint, or test tooling, and no solution code yet. It is a git repo (branch `main`, remote `origin` = github.com/joaquinsantacruz/DSB). All source content is in Spanish.

- `Teorias/`: lecture slides (Bitcoin basics, Ethereum, Solidity/EVM, Web3, Brownie, Rust, Solana/Anchor, ERC-20/ERC-721, patterns, oracles, bridges).
- `Ejercicios/`: the five graded assignments.
- `Videos/`: lecture transcripts plus `links.md`, which maps each video title (same as the transcript filename) to its YouTube URL. Clase 01 ("sin sonido") and the videos marked "no tiene subs" (Web3, Brownie P1, Rust P1/P2) have no transcript. The five `EVM (… Parte) | Taller Avanzado…` transcripts are an external EVM deep-dive workshop (Germán Küber), not course lectures.

The number prefixes in `Teorias/`, `Videos/`, and `links.md` do not agree with each other (`Teorias/03- Rust.md` vs `links.md` "03- Web3"), so match topics by name, not by number.

## Reading the files

Every file is Markdown produced by markitdown. The slides and assignments were PDFs converted to HTML with pdf2htmlEX; the HTML originals are gone, so their images survive only as `![](data:image/png;base64...)` placeholders and any content that lived in a diagram or screenshot is lost. Do not infer what a placeholder showed.

Each transcript in `Videos/` is a single line with no newlines, so line-based reads return the whole file at once. Search with context instead:

```bash
rg -o '.{0,300}storage.{0,300}' Videos/
```

Filenames contain spaces, accents, and `|`, so always quote paths.

`Teorias/05- Clase Solidity-EVM.md` and `Teorias/Clase03-Solidity-EVM-20251013.md` contain the same text. Read just one.

## Assignments and how they connect

| # | Stack | Task |
|---|-------|------|
| 1 | Python + pybitcointools | Bitcoin Testnet wallet: generate addresses, restore from seed, send satoshis, check balances |
| 2 | Solidity | Seven independent contracts: contact book, counter, personal wallet, priority task list, voting, user registry + message wall, escrow with arbiter |
| 3 | Python + Web3.py | Scripts that read, write, and listen to events on **each of the seven Assignment 2 contracts** (same numbering) |
| 4 | Solidity + Brownie | Sealed-bid commit-reveal auction (ERC-721 lot optional). Delivery requires network-parametrized deploy scripts, a public testnet deploy verified on its explorer, Brownie tests with ≥80% coverage, and a README |
| 5 | Rust + Anchor (Solana) | Proposal voting system. State must live in **PDAs, not global collections**. TS tests optional |

Assignment 3 depends on the contracts deployed in Assignment 2, so the events Assignment 3 listens to must be emitted by the Assignment 2 contracts. Assignment 5 says it reuses "the previous activity's statement", but its spec (voting) matches Assignment 2's voting contract, not Assignment 4's auction; follow the spec it states. Read the full assignment text before writing any solution; the table above is only a summary.
