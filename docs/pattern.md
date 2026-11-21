# The audit trail pattern

## Where the pattern comes from

Txvni is an AI deal workspace built by Nirmeet Rao and presented on his portfolio at nirmeetrao.com. Its own description lists cited question answering, KPI extraction, risk analysis, benchmarks, IC memos, collaboration, and audit trail. The audit trail is the last item in that list, and it supports all the others. A cited answer is stronger when the system can also show when the source document arrived and who asked the question. An exported memo is stronger when its export is on record.

The same need appears in his other work. A prior authorization file, a pharmacy billing review, and a deal workspace all produce outputs that someone may later need to explain. The explanation starts with a record of what happened.

## The record

An entry holds a sequence number, the actor, the action, the target, the hash of the entry before it, and its own hash. The sequence number fixes the order. The actor and action say who did what. The target says which document or output was involved. The two hash fields link the entry to the one before it.

The own hash is computed from the sequence, actor, action, target, and previous hash together. Change any one of those fields later and the stored hash no longer matches the recomputed one.

## The four rules

1. Record at the time of the action. An entry written later from memory is a summary, not a trail. The recording step belongs inside the action itself, so uploading, asking, answering, exporting, and flagging each write their entry as they happen.
2. Never edit an entry in place. If an action was recorded wrongly, a new entry records the correction. Editing history to make it look cleaner destroys the one property the trail exists for, which is that the record can be trusted.
3. Link every entry to the one before it. A single entry with a correct hash proves little on its own. A chain proves more, because changing an early entry breaks every link that follows it, and verification finds the first break.
4. Verify, do not assume. Verification recomputes every hash in order and compares each stored previous hash with the actual previous entry. It reports either that the chain is intact or the sequence number of the first entry that fails.

## Design principles

1. The trail answers plain questions. Who uploaded this document. Who exported this memo. Was this file flagged before or after the answer was given. If the trail cannot answer questions like those in one reading, it is missing entries.
2. A failed verification is information. It does not say who changed an entry or why. It says the record as it stands cannot be trusted past the reported point, and that is worth knowing early.
3. A passing verification has limits. It shows the entries present are unchanged since they were written, under the hash rule used here. It does not prove the entries were true when written, it does not prove no entry was removed from the end, and it does not replace access control or secure storage.
4. The trail is read often and written once. Entries are written at action time and read during review. Nothing in normal use rewrites them, and the demo enforces that shape by only ever adding entries.

## What the demo shows, and what it does not show

The demo shows the pattern at miniature scale: 6 invented events, a chain that verifies, a lookup by document, and a deliberate change that verification catches at entry 3. It does not show real documents, real users, authenticated actors, trusted time, secure storage, or the Txvni product, and it claims no security or compliance result. It is a reference implementation of the pattern, written in plain Python with no external packages.

## Links

1. Portfolio: https://nirmeetrao.com
2. GitHub: https://github.com/Zaczee77
3. LinkedIn: https://www.linkedin.com/in/nirmeet-rao
