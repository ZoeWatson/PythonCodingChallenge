import pandas as pd 

def get_data_from_file(log_name):
    # Note: panda auto closes opened files after it reads 
    try:
         csv_data = pd.read_csv(log_name, sep='\t')
         print(csv_data)
    except:
        raise ValueError("file read error: "+ log_name + " could not be read")
    return parse_csv_data(csv_data)

def generate_index_array(stage_array):
    # order O(n) 
    index_array = []
    index = 0
    for stage in stage_array:
        stage_number = sanitize_data(stage)
        if((stage_number >= 0) and 
           ((len(index_array) <= 0 ) or (stage_array[index-1] != stage_number))):
            index_array.append(index)
        index = index + 1
    return index_array

# Helpers
def parse_csv_data(csv_data):
    stage_array = csv_data[csv_data.columns[1]]
    time_array = csv_data[csv_data.columns[0]]
    time_array = pd.to_datetime(time_array)
    return stage_array, time_array

def sanitize_data(data):
    # Trust by verify
    if (data == 1) or (data == 2) or (data == 3) or (data == 0):
        return data
    else:
        return -999 