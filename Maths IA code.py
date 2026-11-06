import time
from SimConnect import SimConnect, AircraftRequests, AircraftEvents
pitch_data = []
speed_data = []
def pitch(ae, aq, sm, airspeed, pitch_up, target_elev, atetude, target_speed, pitch_data):
  while atetude < 1.57079:
    if airspeed == target_speed:
      pitch_up(target_elev)
      print("elevator position set")
      pitch_data.append(atetude)
    else:
      pass

def speed(airspeed, target_speed, throttle, speed_data):
  if airspeed != target_speed:
    if airspeed < target_speed:
      throttle(16384)
    elif airspeed > target_speed:
      throttle(0)
  else:
    pass
  speed_data.append(airspeed)

def main():
  print("connecting")
  sm = SimConnect()
  
  aq = AircraftRequests(sm, _time=0)
  ae = AircraftEvents(sm)
  print("connected")
  try:
    while True:
      airspeed = aq.get("AIRSPEED_INDECATED")
      pitch_up = ae.find("AXIS_ELEVATOR_SET")
      target_elev = 12288
      pitch_up(target_elev)
      print(f"elevator posission sent as {target_elev}")
      throttle = ae.find("THROTTLE_SET")
      target_throttle = 16384
      throttle(target_throttle)
      print(f"throttle set to {target_throttle} (100%)")
      
      
