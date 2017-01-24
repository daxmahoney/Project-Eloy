
from datetime import datetime

def makedate(hl7time):
    #makedate you pass the function the 14 digit number and it returns 
    #example time input 20170112000800
    #example output 2017-01-12T00:08:00Z
    newnum = str(hl7time)
    the_year = int(newnum[0:4])
    the_month = int(newnum[4:6])
    the_day = int(newnum[6:8])
    the_hour = int(newnum[8:10])
    the_minute = int(newnum[10:12])
    the_second = int(newnum[12:14])
    
    new_time = ('{:%Y-%m-%dT%H:%M:%SZ}'.format(datetime(the_year,the_month,the_day,the_hour,the_minute,the_second)))

    return new_time

def get_PID(incoming_PID_block):
    #accepts the PID string and returns the patients ID number
    #these split statements are saying if you use the pipe delimiter this information is in the position noted by the array address
        now_w_carats = incoming_PID_block.split('|')[3]
        patient_ID = now_w_carats.split('^')[0]
        
        return patient_ID

def get_OBX_event(incoming_OBX_block):
    #accepts OBX block and returns the event acronym abbreviation
        now_w_carats = incoming_OBX_block.split('|')[3]
        OBX_event = now_w_carats.split('^')[1]
    
        return OBX_event


def get_OBX_value(incoming_OBX_block):
    #accepts OBX block and returns the the value of the event
        OBX_value = incoming_OBX_block.split('|')[5]
    
        return OBX_value


def get_OBX_unit(incoming_OBX_block):
    #accepts OBX block and returns the unit of the event being measured
        OBX_unit = incoming_OBX_block.split('|')[6]
    
        return OBX_unit


def get_OBR_time(incoming_OBR_block):
    #accepts the OBBR block and returns the iso time
        iso_time_stamp = maketime(incoming_OBR_block.split('|')[6])
    
        return iso_time_stamp

def solution_stapler(observation,patient_ID,observation_time):
    #accepts the arguments and pastes the statements together to for a JSON statement
    # {"event":"SBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":154}
    event = observation.split('|')[3].split('^')[1] #1st group in the 4th pipebin
    patient_ID = str(patient_ID)
    time = observation_time
    unit = observation.split('|')[6]
    value = observation.split('|')[5]
    
    solution = '{"event":"'+event+'","patient":"'+patient_ID+'","time":"'+time+'","unit":"'+unit+'","value":'+value+'}'
    return solution
