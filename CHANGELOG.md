# Changelog

## 0.3.0

- Minimal public release of private Alice voice input using stock Hermes gateway injection.
- Fixed existing Telegram DM destination in the default profile; Telegram-only results.
- Listener starts on the Telegram connect factory, never import or CLI registration;
  unload closes it. Core estop blocks new task injection.
- Asynchronous scheduling ACK, 32-entry in-memory retry cache, local control reminders.
- No completion callbacks, result reader, SDK patches, or Alice TTS.
- 15 local unit tests and an optional hash-verified current-stock SDK/HTTP probe
  with seven synthetic child checks. Public CI covers Python 3.11–3.13 unit tests.

The operator-reported successful real chain is not a blanket live-case verification.
