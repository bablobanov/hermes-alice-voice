# Contributing

Keep this MVP voice-input-only and patch-free. Changes go through pull requests;
do not change Hermes core, add deployment-specific policy, or imply that an ACK
proves delivery. Discuss larger features in an issue before implementing them.

Run `python -B -m unittest discover -s plugins/alice-voice -v` from the root.
Add a regression test for behavior changes. Use synthetic IDs and ephemeral test
secrets only; never paste real request bodies, bearer URLs, credentials, or logs.
The optional SDK probe and exact stock hashes are documented in README.md.
Report skips separately from passes, and fixture checks separately from live tests.

Keep the English and Russian READMEs in sync. Review security implications and
compatibility claims, update CHANGELOG.md, and keep dependencies minimal.
By contributing, you agree to license your contribution under the MIT license.
