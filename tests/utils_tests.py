import unittest 

from sensesagent.utils import DictionaryUtility
from sensesagent import log

class DictionaryUtilityTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_can_convert_simple_dict_to_object(self):
        
        d = { "name": "Jason", "surname": "Viloria"}
        
        r = DictionaryUtility.to_object(d)
        
        self.assertEqual(r.name, d.get("name"))
        self.assertEqual(r.surname, d.get("surname"))


    def test_can_convert_dict_of_dicts_to_object(self):
        
        d = {  
               "personal_info" : {"name": "Jason", "surname": "Viloria"}, 
               "address": { "city": "malaga", "country": "spain"}
            } 
        
        r = DictionaryUtility.to_object(d)
        
        self.assertEqual(r.personal_info.name, d["personal_info"]["name"])
        



        
if __name__ == "__main__":
    
    unittest.main()
    
    
