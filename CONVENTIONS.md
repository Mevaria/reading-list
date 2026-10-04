# Conventions

These rules apply to every change in this repository, whether made by a person or by the pipeline.

## Code
- Python, snake_case for functions and variables.
- Routes return JSON for the API and HTML only for the index page.
- Every new route or behaviour change comes with a test in `tests/`.

## Git
- Branch names follow `<type>/<short-description>`, for example `feat/delete-book`.
- Commit messages follow Conventional Commits: `<type>[optional scope]: <description>`.
- Keep commit messages to one line unless a body is necessary.
- No attribution trailers such as `Co-authored-by`.
- README updates are committed separately as `docs:` commits.

## Review checklist
- All tests pass.
- No security findings at or above the blocking severity.
- Input from requests is validated before use.
- No secrets, tokens or credentials in the code.
- The change stays within the scope of the request.
