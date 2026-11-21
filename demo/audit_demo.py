"""Reference demo: an append only audit trail with a hash chain.

Every sample name, document, and amount in this file is invented.
The demo models the audit trail step described for Txvni, an AI deal
workspace that lists an audit trail among its features. It is not the
Txvni product and it makes no claim about real usage or outcomes.
"""

import hashlib


def entry_hash(sequence, actor, action, target, previous_hash):
    payload = "|".join([str(sequence), actor, action, target, previous_hash])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


class AuditTrail:
    def __init__(self):
        self.entries = []

    def record(self, actor, action, target):
        sequence = len(self.entries) + 1
        previous_hash = self.entries[-1]["hash"] if self.entries else "GENESIS"
        current_hash = entry_hash(sequence, actor, action, target, previous_hash)
        entry = {
            "sequence": sequence,
            "actor": actor,
            "action": action,
            "target": target,
            "previous_hash": previous_hash,
            "hash": current_hash,
        }
        self.entries.append(entry)
        return entry

    def verify(self):
        previous_hash = "GENESIS"
        for entry in self.entries:
            expected = entry_hash(
                entry["sequence"],
                entry["actor"],
                entry["action"],
                entry["target"],
                previous_hash,
            )
            if expected != entry["hash"]:
                return False, entry["sequence"]
            if entry["previous_hash"] != previous_hash:
                return False, entry["sequence"]
            previous_hash = entry["hash"]
        return True, None

    def entries_for(self, target):
        return [entry for entry in self.entries if entry["target"] == target]


SAMPLE_EVENTS = [
    ("analyst_a", "uploaded", "memo_q3.txt"),
    ("analyst_a", "asked_question", "memo_q3.txt"),
    ("system", "answered_with_citation", "memo_q3.txt"),
    ("reviewer_b", "exported", "ic_memo_draft.txt"),
    ("analyst_a", "uploaded", "pricing_sheet.csv"),
    ("reviewer_b", "flagged_for_review", "pricing_sheet.csv"),
]


def main():
    trail = AuditTrail()
    for actor, action, target in SAMPLE_EVENTS:
        trail.record(actor, action, target)

    print(f"{len(trail.entries)} entries recorded")
    for entry in trail.entries:
        print(
            f"{entry['sequence']}. {entry['actor']} {entry['action']} "
            f"{entry['target']} hash {entry['hash']}"
        )

    ok, bad = trail.verify()
    print(f"chain verifies: {ok}")
    assert ok and bad is None

    memo_entries = trail.entries_for("memo_q3.txt")
    print(f"entries for memo_q3.txt: {len(memo_entries)}")
    assert len(memo_entries) == 3

    sheet_entries = trail.entries_for("pricing_sheet.csv")
    print(f"entries for pricing_sheet.csv: {len(sheet_entries)}")
    assert len(sheet_entries) == 2

    tampered = AuditTrail()
    for actor, action, target in SAMPLE_EVENTS:
        tampered.record(actor, action, target)
    tampered.entries[2]["action"] = "deleted"
    ok_after, bad_after = tampered.verify()
    print(f"tampered chain verifies: {ok_after}, first bad entry: {bad_after}")
    assert not ok_after and bad_after == 3

    print("all checks passed")


if __name__ == "__main__":
    main()
