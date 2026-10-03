import pytest

from release_notes import days_between, latest_stable, parse_release


def test_parse_release_reads_version_and_date():
    release = parse_release("1.4.0 2026-03-14")
    assert str(release.version) == "1.4.0"
    assert (release.released_at.year, release.released_at.month, release.released_at.day) == (2026, 3, 14)


def test_parse_release_accepts_written_dates():
    release = parse_release("2.0.0 March 1, 2026")
    assert release.released_at.month == 3


def test_parse_release_rejects_a_line_without_a_date():
    with pytest.raises(ValueError):
        parse_release("1.4.0")


def test_latest_stable_orders_by_version_not_text():
    releases = [parse_release(line) for line in ["1.9.0 2026-01-01", "1.10.0 2026-02-01", "2.0.0rc1 2026-03-01"]]
    latest = latest_stable(releases)
    assert latest is not None
    assert str(latest.version) == "1.10.0"


def test_latest_stable_is_none_without_stable_releases():
    assert latest_stable([parse_release("2.0.0rc1 2026-03-01")]) is None


def test_days_between_releases():
    first = parse_release("1.9.0 2026-01-01")
    second = parse_release("1.10.0 2026-02-01")
    assert days_between(first, second) == 31
