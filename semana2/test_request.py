import unittest
import make_request

class TestRequest(unittest.TestCase):

	def test_type(self):
		new_p = make_request.Request(new_plant='spider_plant')
		self.assertIsInstance(new_p.repeat_plant_name(),str)

if __name__ == "__main__":
	unittest.main()