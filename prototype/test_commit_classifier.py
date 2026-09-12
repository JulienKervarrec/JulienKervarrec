import unittest

from commit_classifier import accepted_shas, classify_commit


class CommitClassifierTests(unittest.TestCase):
    def test_accepts_public_authored_main_commit_with_file(self):
        commit = {"sha": "base-001", "author": "JulienKervarrec", "visibility": "public", "branch": "main", "files": ["docs/base.md"], "domain": "Base"}
        self.assertEqual(accepted_shas([commit], "JulienKervarrec"), ["base-001"])

    def test_covers_four_domain_fixtures(self):
        commits = [{"sha": domain.lower()+"-001", "author": "JulienKervarrec", "visibility": "public", "branch": "main", "files": ["docs/notes.md"], "domain": domain} for domain in ("Base", "Hyperliquid", "ZK", "FHE")]
        self.assertEqual(len(accepted_shas(commits, "JulienKervarrec")), 4)

    def test_explains_rejection_reasons(self):
        decision = classify_commit({"sha": "bad-001", "author": "other", "visibility": "private", "branch": "feature", "files": [], "is_merge": True}, "JulienKervarrec")
        self.assertFalse(decision.accepted)
        self.assertIn("commit non public", decision.reasons)
        self.assertIn("auteur différent", decision.reasons)
        self.assertIn("commit de merge", decision.reasons)


if __name__ == "__main__":
    unittest.main()
