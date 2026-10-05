"""Voice-input-only control phrases; no result reader."""
import unittest
import test_bridge as fixtures


class VoiceInputTests(unittest.TestCase):
    path: str
    setUp = fixtures.BridgeTests.setUp
    bridge = fixtures.BridgeTests.bridge

    def test_control_phrases_never_inject_or_claim_readiness(self):
        bridge = self.bridge()
        for phrase in ('Ответ готов?', 'Дальше', ' ОТВЕТ ГОТОВ! ', 'дальше.'):
            with self.subTest(phrase=phrase):
                status, data = bridge.handle(self.path, fixtures.envelope(phrase))
                self.assertEqual(status, 200)
                self.assertEqual(data['response']['text'], 'Ответ будет в Telegram')
        self.assertEqual(bridge.ctx.calls, [])

    def test_control_phrases_remain_local_when_paused(self):
        bridge = self.bridge(paused=lambda: True)
        self.assertEqual(bridge.handle(self.path, fixtures.envelope('Ответ готов?')),
                         (200, {'version': '1.0', 'response': {
                             'text': 'Ответ будет в Telegram', 'end_session': False}}))
        self.assertEqual(bridge.ctx.calls, [])

    def test_control_requires_authenticated_envelope(self):
        bridge = self.bridge()
        self.assertEqual(bridge.handle('/alice/wrong', fixtures.envelope('Дальше'))[0], 403)
        data = fixtures.envelope('Ответ готов?')
        del data['session']['user']
        self.assertEqual(bridge.handle(self.path, data)[0], 403)
        self.assertEqual(bridge.ctx.calls, [])

    def test_task_ack_has_no_completion_state(self):
        bridge = self.bridge()
        self.assertEqual(bridge.handle(self.path, fixtures.envelope())[1]['response']['text'], fixtures.ACK)
        self.assertFalse(hasattr(bridge, 'results'))
        self.assertFalse(hasattr(bridge, '_completed'))
        self.assertFalse(hasattr(bridge, '_read_result'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
