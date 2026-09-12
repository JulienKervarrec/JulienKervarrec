# Prototype de classification de commits pour expérimentation Guild

from dataclasses import dataclass
from typing import Any, Dict, Iterable, List


@dataclass(frozen=True)
class Decision:
    sha: str
    accepted: bool
    reasons: tuple[str, ...]


REQUIRED_FIELDS = ("sha", "author", "visibility", "branch", "files")


def classify_commit(commit: Dict[str, Any], expected_author: str, expected_branch: str = "main") -> Decision:
    """Classifie un commit selon des critères explicites et reproductibles.

    Ce modèle expérimental ne prétend pas reproduire Guild : il rend visibles
    les hypothèses utilisées pour comparer un historique GitHub.
    """
    sha = str(commit.get("sha", ""))
    reasons: List[str] = []
    missing = [field for field in REQUIRED_FIELDS if field not in commit]
    if missing:
        reasons.append("champs manquants: " + ", ".join(missing))
    if commit.get("visibility") != "public":
        reasons.append("commit non public")
    if commit.get("author") != expected_author:
        reasons.append("auteur différent")
    if commit.get("branch") != expected_branch:
        reasons.append("branche différente")
    if not commit.get("files"):
        reasons.append("aucun fichier modifié")
    if commit.get("is_merge", False):
        reasons.append("commit de merge")
    return Decision(sha, not reasons, tuple(reasons))


def classify_history(commits: Iterable[Dict[str, Any]], expected_author: str, expected_branch: str = "main") -> List[Decision]:
    return [classify_commit(commit, expected_author, expected_branch) for commit in commits]


def accepted_shas(commits: Iterable[Dict[str, Any]], expected_author: str, expected_branch: str = "main") -> List[str]:
    return [decision.sha for decision in classify_history(commits, expected_author, expected_branch) if decision.accepted]
