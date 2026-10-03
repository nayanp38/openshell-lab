from dataclasses import dataclass
from datetime import datetime

from dateutil import parser as date_parser
from packaging.version import Version


@dataclass(frozen=True)
class Release:
    version: Version
    released_at: datetime

    @property
    def is_stable(self) -> bool:
        return not (self.version.is_prerelease or self.version.is_devrelease)


def parse_release(line: str) -> Release:
    """Parse a line such as ``1.4.0 2026-03-14`` into a Release."""
    version_text, _, date_text = line.strip().partition(" ")
    if not version_text or not date_text.strip():
        raise ValueError(f"expected '<version> <date>', got {line!r}")
    return Release(Version(version_text), date_parser.parse(date_text.strip()))


def latest_stable(releases: list[Release]) -> Release | None:
    """Return the highest stable version, or None when there is none."""
    stable = [release for release in releases if release.is_stable]
    return max(stable, key=lambda release: release.version, default=None)


def days_between(earlier: Release, later: Release) -> int:
    """Return the whole days from one release to a later one."""
    return (later.released_at - earlier.released_at).days
