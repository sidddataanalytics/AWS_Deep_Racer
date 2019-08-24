import math
def reward_function(params):
    '''
     '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])
    direction_stearing=params['steering_angle']
    speed = params['speed']
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    ABS_STEERING_THRESHOLD = 15
    TOTAL_NUM_STEPS = 85
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    
    #Set the reward reward_function
    reward = 1
    if progress == 100:
        reward = reward + 100
    
    #calculate the current & next waypoints
    prev_point = waypoints[closest_waypoints[0]]
    next_point = waypoints[closest_waypoints[1]]
    
    #calculate the direction_stearing in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2((next_point[1] - prev_point[1]), (next_point[0] - prev_point[0])) 
    
    #convert to degrees
    track_direction = math.degrees(track_direction)
    
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    
    # Penalize the reward if the difference is too large
    DIRECTION_THRESHOLD = 12.0
    SPEED_THRESHOLD = 2.25 
    
    reward_calculator=1
    
    if direction_diff > DIRECTION_THRESHOLD:
        reward_calculator=1-(direction_diff/50)
        if reward_calculator<0 or reward_calculator>1:
            reward_calculator = 0
        reward *= reward_calculator
        
        
    if not all_wheels_on_track:
		# Penalize if the car goes off track
       reward = reward - 1.0
    elif speed < SPEED_THRESHOLD:
		# Penalize if the car goes too slow
        reward = reward - 2.0
    else:
		# High reward if the car stays on track and goes fast
        reward = reward + 2.0
    
    return float(reward)
