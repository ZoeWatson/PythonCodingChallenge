import unittest
import main

class TestMain(unittest.TestCase):
    # Basic Tests
    def test_basic_simple_incident(self):
        incident_count, incident_details, time_array = main.parse_event_log_data(
            'TestFiles\\basic_simple_incident.csv')
        self.assertEqual(incident_count, 1)
        self.assertEqual(incident_details, [[0,2]])

    def test_basic_simple_incidents_2(self):
        incident_count, incident_details, time_array  = main.parse_event_log_data(
            "TestFiles\\basic_simple_incidents_2.csv")
        self.assertEqual(incident_count, 2)
        self.assertEqual(incident_details, [[0,2], [3, 5]])

    def test_basic_simple_incidents_2_with_gap(self):
        incident_count, incident_details, time_array  = main.parse_event_log_data(
            "TestFiles\\basic_simple_incidents_2_with_gap.csv")
        self.assertEqual(incident_count, 2)
        self.assertEqual(incident_details, [[0,2], [11, 13]])

    def test_basic_simple_no_incident(self):
        incident_count, incident_details, time_array = main.parse_event_log_data(
            'TestFiles\\basic_simple_no_incident.csv')
        self.assertEqual(incident_count, 0)
        self.assertEqual(incident_details, [])   

    # Non Stage Changing Tests
    def test_stage1_non_stage_changing_event (self):
        incident_count, incident_details, time_array  = main.parse_event_log_data(
            "TestFiles\\stage1_non_stage_changing_event_incident.csv")
        self.assertEqual(incident_count, 1)
        self.assertEqual(incident_details, [[2,6]])  

    def test_stage2_non_stage_changing_event (self):
        incident_count, incident_details, time_array  = main.parse_event_log_data(
            "TestFiles\\stage2_non_stage_changing_event_incident.csv")
        self.assertEqual(incident_count, 1)
        self.assertEqual(incident_details, [[2,6]]) 

    def test_large_data_set(self):
        incident_count, incident_details, time_array  = main.parse_event_log_data(
            "TestFiles\\large_event_log.txt")
        self.assertEqual(incident_count, 10)

if __name__ == '__main__':
    unittest.main()