# Git

> Bootstrap 2026-11-09. Uzak depo: **GitHub** (CI: `.github/workflows/check.yml`).
> Varsayılan branch: `main`. Tek geliştiricili ekip.

## Branching
- `feature/<spec-no>-<short-name>` — **no branch without a spec.** Also for CHANGE-lane mini-specs.
- Refactors: `refactor/<spec-no>-<short-name>` (mini-spec with Changed behavior = none).
- Fixes: `fix/<report-id>-<short-name>` (bug fixes carry a report, not a spec number);
  incidents: `incident/<date>-<short-name>`; trivial changes: `trivial/<short-name>` (see below).

## Commits
- Conventional Commits, İngilizce, plan referanslı: `feat(leave): weekday-only leave days [plan 0001/3]`.
  Review fixes name their fix round instead of the step:
  `fix(leave): weekend boundary [plan 0001/fix-2]` — the reviewer counts rounds from these
  (R-06 after round 3).
- Agent commits follow the same standard: the agent writes the message, the human approves.

## Forbidden
- Direct commits to the default branch. **Tek istisna:** bootstrap'in ilk commit'i
  (`chore: bootstrap ANEW workspace`), çünkü o anda başka branch yok.
- Force push, history rewriting on shared branches. Undo = `git revert` (see recovery R-11).

## Trivial changes
<!-- Set at bootstrap. Applies only to requests the change-request triage rubric
     (workflows/change-request.md) classifies as TRIVIAL: no acceptance criterion changes, no shared code. -->
- Policy: **(1) PR + bağımsız inceleme (`/review`), spec yok.**
- Always: one narrow commit, `scripts/check` green. A second file or a new test means re-triage.
- Dikkat: durum değerleri (`Onaylandi` …) hem ekran metni hem veridir — "yazım düzeltmesi" değil,
  davranış değişikliğidir (`docs/domain.md`).

## Pull requests
- PR template checklist completed; `scripts/check` green in CI; squash-merge.
- İnsan onayı yerine **bağımsız inceleme** yeterlidir (tek geliştirici): `/review` ile salt okunur
  alt ajan ya da ayrı oturum (invariant kural 3). İnceleme raporu PR'a bağlanır.
