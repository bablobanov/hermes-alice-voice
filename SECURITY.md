# Security

This experimental 0.3.x input bridge is intended for one operator using a private
Alice skill. It is not a public authentication service. Only the current 0.3.x
line is in scope for fixes; there is no guaranteed response time or security SLA.

The webhook URL is a bearer credential. Yandex request signatures are not
verified; request-body account/skill IDs can be forged by someone with the bearer.
Requests run with the configured Hermes session's existing permissions. Keep
normal gateway authorization, tool approvals, HTTPS, proxy limits, and log hygiene.
See README.md for the complete boundaries and delivery limitations.

Do not publish an exploitable issue or any secrets. If available, use this
repository's GitHub Security → Report a vulnerability private reporting feature.
Otherwise privately contact the maintainer through their GitHub profile; do not
assume private reporting is enabled. Share a minimal synthetic reproducer,
affected version, and impact, never your actual bearer URL or payload identifiers.

If a bearer is disclosed, rotate ALICE_WEBHOOK_SECRET in Hermes .env, update the
private skill webhook, and restart the gateway. Disable the plugin while investigating.
