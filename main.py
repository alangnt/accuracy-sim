GRAVITY = 9.81
INITIAL_VELOCITY = 20
INITIAL_POSITION = 0
SIMULATION_DURATION = 4

DT = 1

# at peak -> v = 0
# h = h₀ + v₀·t − ½·g·t²

def calculate_max_height_at_current_time(current_time):
  return INITIAL_POSITION + (INITIAL_VELOCITY * current_time) - (0.5 * GRAVITY * current_time**2)

def main():
  duration = 0
  
  time_to_peak = INITIAL_VELOCITY / GRAVITY
  
  print(f"Time to reach the peak: {time_to_peak:.2f}s")
  
  while duration <= SIMULATION_DURATION:
    max_height_at_current_time = calculate_max_height_at_current_time(duration)
    print(f"Max height at {duration}s: {max_height_at_current_time:.2f}m")
    duration += DT
  
main()