from unittest import TestCase
from implement_queue_using_stacks import MyQueue


class TestMyQueue(TestCase):
    def test_Queue(self):
        obj = MyQueue()
        inputs = (
            ("push", 1), ("push", 2), "peek", "pop", "empty"
        )
        outs = (None, None, 1, 1, False)
        for inp, out in zip(inputs, outs):
            if isinstance(inp, tuple):
                ret = getattr(obj, inp[0])(inp[1])
            else:
                ret = getattr(obj, inp)()
            self.assertEqual(ret, out)
