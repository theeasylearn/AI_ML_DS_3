'''
    pip install swig
    pip install "gymnasium[box2d]
'''
import gymnasium as gym
import time

# Create the Lunar Lander environment
env = gym.make("LunarLander-v3", render_mode="human")

observation, info = env.reset()

start_time = time.time()
step = 0
total_reward = 0

print("🚀 Lunar Lander is starting... Try to land safely!")

while time.time() - start_time < 15:   # Run for 15 seconds
    # Random actions for now (Later we will use AI)
    action = env.action_space.sample()
    
    observation, reward, terminated, truncated, info = env.step(action)
    
    total_reward += reward
    step += 1
    
    print(f"Step: {step} | Reward: {reward:.2f} | Total Reward: {total_reward:.2f}")
    
    time.sleep(0.02)
    
    if terminated or truncated:
        if reward > 100:
            print("🎉 Successful Landing!")
        else:
            print("💥 Crash Landing!")
        break

print(f"\nEpisode Finished! Total Reward: {total_reward:.1f} | Steps: {step}")
env.close()