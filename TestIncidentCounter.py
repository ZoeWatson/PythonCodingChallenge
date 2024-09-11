import unittest
from datetime import datetime
import IncidentCounter

# This File is AI generated from ChatGPT with minor modifications and additions 
class TestCheckTime(unittest.TestCase):

    def test_check_time_true(self):
        # Define a time array with intervals greater than or equal to 5 minutes
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0)]
        
        index_array = [0, 1, 2, 3]

        # Call the function for each index
        for i in range(len(time_array) - 1):
            self.assertTrue(IncidentCounter.check_time(i, time_array, index_array))

    def test_check_time_false(self):
        # Define a time array with intervals less than 5 minutes
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 3, 0),
                      datetime(2024, 6, 4, 12, 6, 0), datetime(2024, 6, 4, 12, 9, 0)]
        
        index_array = [0, 1, 2, 3]

        # Call the function for each index
        for i in range(len(time_array) - 1):
            self.assertFalse(IncidentCounter.check_time(i, time_array, index_array))

    def test_check_time_index_out_of_range(self):
        # Define a time array with only one element
        time_array = [datetime(2024, 6, 4, 12, 0, 0)]
        index_array = [0]

        # Call the function with an index out of range
        self.assertFalse(IncidentCounter.check_time(0, time_array, index_array))

class TestIncidentCounter(unittest.TestCase):

    def test_incident_counter_no_incident(self):
        # Define index_array, stage_array, and time_array without any incident
        index_array = [0, 2, 3]
        stage_array = [1, 2, 3, 2, 3]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0),
                      datetime(2024, 6, 4, 12, 20, 0)]
        
        # Call the function
        incident_count, incident_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        
        # Verify no incidents detected
        self.assertEqual(incident_count, 0)
        self.assertEqual(incident_details, [])

    def test_incident_counter_single_incident(self):
        # Define index_array, stage_array, and time_array with a single incident
        index_array = [0, 1, 2]
        stage_array = [3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 11, 0)]
        
        # Call the function
        incident_count, incident_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        
        # Verify one incident detected
        self.assertEqual(incident_count, 1)
        self.assertEqual(incident_details, [[0, 2]])

    def test_incident_counter_single_incident_less_than_a_sec(self):
        # Define index_array, stage_array, and time_array with a single incident
        index_array = [0, 1, 2]
        stage_array = [3, 2, 0]
        # this tests what happens if there is less than a second between incidents. 
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 5, 0)]
        
        # Call the function
        incident_count, incident_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        
        # Verify one incident detected
        self.assertEqual(incident_count, 1)
        self.assertEqual(incident_details, [[0, 2]])

    def test_incident_counter_multiple_incidents(self):
        # Define index_array, stage_array, and time_array with multiple incidents
        index_array = [0, 1, 3, 4, 5, 6, 7, 8]
        stage_array = [3, 2, 2, 0, 3, 2, 0, 1, 2]
        
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 6, 0),
                      datetime(2024, 6, 4, 12, 11, 0), datetime(2024, 6, 4, 12, 17, 0),
                      datetime(2024, 6, 4, 12, 22, 0), datetime(2024, 6, 4, 12, 28, 0),
                      datetime(2024, 6, 4, 12, 30, 0), datetime(2024, 6, 4, 12, 35, 0),
                      datetime(2024, 6, 4, 12, 40, 0)]
        
        # Call the function
        incident_count, incident_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        
        # Verify multiple incidents detected
        self.assertEqual(incident_count, 2)
        self.assertEqual(incident_details, [[0, 3], [4, 6]])

    # the following tests each focus on testing a specific stage of the incident cycle
    '''The fault sequence is indicated by four operations that occur in sequence: 
        1.	Stage 3 for five minutes or more
        2.	Stage 2, 
        3.	Any number of cycles between stage 2 and 3 for any duration
        4.	Stage 0 '''
    def test_error_stage_1(self):
        index_array = [0, 1, 2]
        stage_array = [3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 1),
                      datetime(2024, 6, 4, 12, 10, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

        index_array = [0, 1, 2]
        stage_array = [3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 4, 59),
                      datetime(2024, 6, 4, 12, 10, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

        index_array = [0, 1, 2]
        stage_array = [3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 3, 0),
                      datetime(2024, 6, 4, 12, 10, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

        index_array = [0, 1, 2]
        stage_array = [1, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

    def test_error_stage_2(self):
        index_array = [0, 1, 2]
        stage_array = [3, 1, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

        index_array = [0, 1, 2, 3]
        stage_array = [3, 0, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

    def test_error_stage_3(self):
        index_array = [0, 1, 2, 3]
        stage_array = [3, 2, 3, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

        index_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        stage_array = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0),
                      datetime(2024, 6, 4, 12, 15, 1), datetime(2024, 6, 4, 12, 15, 2),
                      datetime(2024, 6, 4, 12, 15, 3), datetime(2024, 6, 4, 12, 15, 4),
                      datetime(2024, 6, 4, 12, 15, 5), datetime(2024, 6, 4, 12, 15, 6),
                      datetime(2024, 6, 4, 12, 15, 7), datetime(2024, 6, 4, 12, 15, 8),
                      datetime(2024, 6, 4, 12, 15, 9), datetime(2024, 6, 4, 12, 15, 10),
                      datetime(2024, 6, 4, 12, 15, 11)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

        index_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        stage_array = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0),
                      datetime(2024, 6, 4, 12, 15, 1), datetime(2024, 6, 4, 12, 15, 2),
                      datetime(2024, 6, 4, 12, 15, 3), datetime(2024, 6, 4, 12, 15, 4),
                      datetime(2024, 6, 4, 12, 15, 5), datetime(2024, 6, 4, 12, 15, 6),
                      datetime(2024, 6, 4, 12, 15, 7), datetime(2024, 6, 4, 12, 15, 8),
                      datetime(2024, 6, 4, 12, 15, 9), datetime(2024, 6, 4, 12, 15, 10),
                      datetime(2024, 6, 4, 12, 15, 11)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

        index_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        stage_array = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 0, 1]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0),
                      datetime(2024, 6, 4, 12, 15, 1), datetime(2024, 6, 4, 12, 15, 2),
                      datetime(2024, 6, 4, 12, 15, 3), datetime(2024, 6, 4, 12, 15, 4),
                      datetime(2024, 6, 4, 12, 15, 5), datetime(2024, 6, 4, 12, 15, 6),
                      datetime(2024, 6, 4, 12, 15, 7), datetime(2024, 6, 4, 12, 15, 8),
                      datetime(2024, 6, 4, 12, 15, 9), datetime(2024, 6, 4, 12, 15, 10),
                      datetime(2024, 6, 4, 12, 15, 11)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

    def test_error_stage_4(self):
        index_array = [0, 1, 2, 3]
        stage_array = [3, 2, 0, 2]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0), datetime(2024, 6, 4, 12, 15, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

        index_array = [0, 1, 2]
        stage_array = [3, 2, 1]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

        index_array = [0, 1, 2, 3, 4, 5]
        stage_array = [3, 2, 1, 3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0),datetime(2024, 6, 4, 12, 10, 1),
                      datetime(2024, 6, 4, 12, 30, 1), datetime(2024, 6, 4, 12, 30, 2)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

        index_array = [0, 1, 2, 3, 4, 5]
        stage_array = [3, 2, 2, 3, 2, 0]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0),
                      datetime(2024, 6, 4, 12, 10, 0),datetime(2024, 6, 4, 12, 10, 1),
                      datetime(2024, 6, 4, 12, 30, 1), datetime(2024, 6, 4, 12, 30, 2)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 1)

        index_array = [0, 1]
        stage_array = [3, 2]
        time_array = [datetime(2024, 6, 4, 12, 0, 0), datetime(2024, 6, 4, 12, 5, 0)]
        error_count, error_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
        self.assertEqual(error_count, 0)

if __name__ == '__main__':
    unittest.main()
