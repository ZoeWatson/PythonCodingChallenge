from datetime import timedelta

def incident_counter(index_array, stage_array, time_array):
    # order O(n) 
    incident_count = 0
    incident_stage = 1
    incident_details = []
    line_start = 0
    for index in index_array:
        if(incident_stage == 1):
            if((stage_array[index] == 3) and (check_time(index, time_array, index_array))):
                incident_stage = 2
                line_start = index
        elif(incident_stage == 2):
            if(stage_array[index]==2):
                incident_stage = 3
            else:
                incident_stage = 1
        elif(incident_stage == 3):
            if(stage_array[index] == 2 or stage_array[index] == 3):
                incident_stage = 3 
            elif(stage_array[index] == 0 ):
                incident_stage = 1
                incident_count = incident_count + 1
                incident_details.append([line_start, index])
            else:
                incident_stage = 1
    return incident_count, incident_details

# Helpers 
def check_time(index, time_array, index_array):
    next = index_array.index(index)+1
    if(next < len(index_array)):
        time = time_array[index_array[next]] - time_array[index]
        return time >= timedelta(minutes=5)
    else:
        return False