# pip install gymnasium 

import gymnasium as gym
import time

# Step 1: Create the environment
# CartPole-v1 = Name of the game
# render_mode="human" = Show the moving cart and stick on screen so we can watch it live."
environment = gym.make("CartPole-v1", render_mode="human")

# Step 2: Start the game
observation, info = environment.reset()

start_time = time.time()   # Record start time
step = 0

# Run until 10 seconds are completed
while time.time() - start_time < 10:
    # decide Random action (left or right)
    action = environment.action_space.sample()
    
    # Take action
    observation, reward, terminated, truncated, info = environment.step(action)
    
    print(f"Step: {step}, Reward: {reward} {observation} {info}")
    
    step += 1
    
    # Small delay for smooth animation (adjust if needed)
    time.sleep(0.05)
    
    # Stop if pole falls
    if terminated or truncated:
        print(f"Game Over! Stick fell after {step} steps")
        break

# Print total time taken
total_time = time.time() - start_time
print(f"\nEpisode Finished! Ran for {total_time:.2f} seconds")

environment.close()