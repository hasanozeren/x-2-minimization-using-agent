import gym
import gym.spaces
import random
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

a=[]
b=[]
class x2env(gym.Env):
    def __init__(self):
        self.observation_space = gym.spaces.Box(low=-1000,high=1000,shape=(1,),dtype=int)
        self.action_space = gym.spaces.Discrete(2)
        self.cStep=0
        self.maxStep=1000000
        self.x=random.randint(-1000,1000)
    def reset(self):
        self.cStep=0
        self.x=random.randint(-1000,1000)
        return self.x 
    def step(self,action):
        done=False
        i=0
        if(len(a)>=2):
           if(b[i]>0):
               action=1
               i+=1
           elif(b[i]<0):
                 action=0
                 i+=1
           else:
               action=None
        if action==0:
              self.x+=1
        elif action==1:
              self.x-=1
        else:
            self.x=self.x
        self.cStep+=1
        if self.cStep >self.maxStep:
            raise Exception("Ajan hatalı hareket ediyor")
        reward= -(self.x**2)
        a.append(reward)
        b.append(self.x)

        return self.x ,reward, done, {}
    

env=x2env()
env = DummyVecEnv([lambda: env])
model = PPO('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=2000)
obs = env.reset()
total_reward=[]
for i in range(2000):
    action, _=model.predict(obs)
    obs ,reward, done, info= env.step(action)
    total_reward.append(reward)
    if done:
        break


c=max(a)
index=a.index(c)
print("x^2 fonksiyonun minimizasyonun sonucu",b[index])



