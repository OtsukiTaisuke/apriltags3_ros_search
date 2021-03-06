import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


#%matplotlib inline
class BAgent(object):
    def __init__(self, epsilon):
        self.epsilon = epsilon
        self.reward_log = []
        self.Q = {}
    def __del__(self):
        epis = [x+1 for x in range(len(self.reward_log))]
        data = pd.DataFrame(colums = ['episode', 'reward'])
        data.append(pd.DataFrame({'episode':x, 'reward':self.reward_log}))
        data.to_csv('reward_log.csv')

        self.fig.save("reward_log.png")


    def policy(self, state, actions,Q):
        if np.random.rand() < self.epsilon:
            return np.random.randint(len(actions))
        else:
            if state in Q and sum(Q[state]) != 0:
                return np.argmax(Q[state])
            else:
                return np.random.randint(len(actions))

    def init_log(self):
        self.reward_log = []
        self.fig, self.ax = plt.subplots(1,1)
        plt.title("Reward History")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
    def log(self, reward):
        self.reward_log.append(reward)
    def show_reward_log(self, interval=1, episode = -1):
        if len(self.reward_log) > 0 and episode > 1 :#and e%interval ==0:
            x = range(len(self.reward_log))#episode
            y = self.reward_log
            #plt.scatter(x, y)
            #line ,  = self.ax.plot(x,y)
            plt.plot(x,y)
            self.fig.canvas.draw()
            #plt.draw()
            #plt.show(block= False)
            #plt.pause(0.1) #second
            #line.remove()


    """
    def reset_learn(self,env):
        self.actions = list(range(env.action_space))
        self.value = defaultdict(lambda: [0]*len(self.actions))
        #model = Model(self.actions)
        rewards = []
    """

    def instant_learn(self,env,episode_num, episode_count=1000, gamma=0.9, learning_rate = 0.1,\
            observer = -1, report_inverval= 100):
            a = self.policy(s)
            n_state, reward, done, info = env.step(a)

            gain = reward + gamma * max(self.value[n_state])
            self.value[s][a] += learning_rate * (gain - estimated)
            """
            if observer > 0 :
                model.update(s)
                ...
            """
            s = n_state
            if episode_num != 0 and episode_num % report_inverval ==0:
                recent = np.array(rewards[- report_inverval:])
                print ("At episode {}, reward is {}".format(e, recent.mean()))



    def learn(self, env, episode_count=1000, gamma=0.9, learning_rate = 0.1,\
            observer = -1, report_inverval= 100):
        self.actions = list(range(env.action_space))
        self.value = defaultdict(lambda: [0]*len(self.actions))
        #model = Model(self.actions)
        rewards = []

        for e in range(episode_count):
            s = env.reset()
            done = False
            goal_reward = 0
            while not done:
                a = self.policy(s)
                n_state, reward, done, info = env.step(a)

                gain = reward + gamma * max(self.value[n_state])
                self.value[s][a] += learning_rate * (gain - estimated)
                """
                if observer > 0 :
                    model.update(s)
                    ...
                """
                s = n_state
            else:
                goal_reward = reward
        rewards.append()
        if e != 0 and e % report_inverval ==0:
            recent = np.array(rewards[- report_inverval:])
            print ("At episode {}, reward is {}".format(e, recent.mean()))



