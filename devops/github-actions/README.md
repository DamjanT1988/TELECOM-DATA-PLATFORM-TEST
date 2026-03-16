# GitHub Actions Notes

Primary workflow lives in `../../.github/workflows/ci.yml`.

It performs:
- dependency install
- backend test execution
- docker image build
- compose startup and API health probe
