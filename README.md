# Audit trail pattern

A reference pattern and a small runnable demo for keeping a trustworthy record of what happened inside an AI workspace. The pattern comes from work Nirmeet Rao has shipped: Txvni, his AI deal workspace for private equity, hedge fund, and family office teams, which ingests documents and spreadsheets for cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail.

## The problem

An AI workspace lets people upload documents, ask questions, get cited answers, and export memos. When a number in an exported memo is later questioned, someone has to answer a plain question: who did what, to which document, and in what order. If the system kept no record, or kept a record that anyone could quietly edit, that question has no trustworthy answer.

An audit trail is the record that answers it. It is not a feature for its own sake. It is what makes the other features defensible when a team, a client, or a reviewer asks how a result was produced.

## What the pattern does

1. Every meaningful action is recorded as one entry, with a sequence number, the actor, the action, and the target document.
2. Entries are added in order and are never edited in place. A correction is a new entry, not a rewrite of an old one.
3. Every entry carries a short hash of its own contents together with the hash of the entry before it, forming a chain.
4. The chain can be verified at any time. If an old entry was changed, its hash no longer matches and verification reports the first entry where the chain breaks.
5. Entries can be listed for one document, so the full history of a single file can be read without scanning the whole trail.

## The demo in this repository

The demo folder contains a small reference demo in plain Python with no external packages. It records 6 invented events: uploads, a question, a cited answer, an export, and a review flag. The chain verifies as intact. The demo then changes one old entry on purpose and verifies again, and verification fails at entry 3, which is exactly where the change was made. A lookup lists 3 entries for the memo and 2 entries for the pricing sheet.

The docs folder describes the pattern in full: what an entry contains, why entries are never edited, how the hash chain works, and what verification can and cannot prove.

## What this is not

This demo is not the Txvni product. It models the audit trail idea Txvni lists among its features, at miniature scale, with invented sample data. No real documents, deals, users, or outcomes appear here, and no security, compliance, or outcome number is claimed. A real system would add the steps this demo does not model, such as authenticated actors, trusted timestamps, storage that prevents deletion, access rules for who may read the trail, and retention rules. None of those are modeled here, and a hash chain alone is not a compliance system.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
