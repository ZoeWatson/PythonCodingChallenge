import GUI 
import IncidentCounter
import logSanitizer

def main():
    GUI.gui_init(parse_event_log)

# Helpers 
def parse_event_log(results_display):
    # get the event log data from user selected file 
    try:
        log_name = GUI.open_file()
    except:
        print("failed to open file")
        return
    # handles the data of the parse_event_log, a way to sperate GUI from Controller/Data 
    try:
        incident_count, incident_details, time_array = parse_event_log_data(log_name)
    except:
        print("failed to parse data")
        return

    # display the results  
    GUI.display_results(incident_count, incident_details, time_array, results_display, log_name)

def parse_event_log_data(log_name):
    # get the event log data from user selected file 
    try:
        stage_array, time_array = logSanitizer.get_data_from_file(log_name)
    except:
        # it would be nice to have a user error message here detailing why the data is invalid.
        raise ValueError("failed to get data from user selected file")
    
    # create an array of the valid indexi of the stage_array 
        # this allows non-stage-changing events to be ignored.
    index_array = logSanitizer.generate_index_array(stage_array)

    # count the incidents in the event log
    incident_count, incident_details = IncidentCounter.incident_counter(
            index_array, stage_array, time_array)
    return incident_count, incident_details, time_array 
