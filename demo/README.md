# Demo: audit trail

A small reference demo of the audit trail idea behind Txvni: every action is recorded as one entry with a sequence number, an actor, an action, and a target, each entry carries a hash linked to the entry before it, and the chain can be verified to catch a later change to an old entry.

## How to run it

From the repository root, or from this folder:

```
python3 demo/audit_demo.py
```

Plain Python, no external packages, no network calls.

## What it does

1. It records 6 invented events: two uploads, one question, one cited answer, one export, and one review flag.
2. It prints each entry with its sequence number and hash, then verifies the chain and reports that it is intact.
3. It lists the entries for one document at a time: 3 entries for the memo and 2 entries for the pricing sheet.
4. It copies the trail, changes the action recorded in entry 3, and verifies again. Verification fails and reports entry 3 as the first bad entry, which is where the change was made.

## What it printed when it was tested

6 entries recorded, chain verifies true, 3 entries for the memo, 2 entries for the pricing sheet, the tampered chain verifies false with first bad entry 3, and all checks passed.

## What the sample data is

Every actor name, document name, and event in `audit_demo.py` is invented sample data written only to exercise the pattern. Nothing here is a real document, a real deal, a real user, or a real system log. A real system would record real actions by authenticated users in secure storage. None of that is modeled here.

## Files

1. `audit_demo.py`: the demo. The sample events, the entry recording, the hash chain, the verification, the lookup by document, and the built in assertions.
2. `README.md`: this file.
