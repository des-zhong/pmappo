import numpy as np
import gym


class EnvCore(object):
    """
    # 环境中的智能体
    """

    def __init__(self):
        self.env = gym.make('BipedalWalker-v3')
        self.agent_num = 2
        self.obs_dim = 24
        self.action_dim = 2

    def reset(self):
        """
        # self.agent_num设定为2个智能体时，返回值为一个list，每个list里面为一个shape = (self.obs_dim, )的观测数据
        # When self.agent_num is set to 2 agents, the return value is a list, each list contains a shape = (self.obs_dim, ) observation data
        """
        start_state = self.env.reset()
        sub_agent_obs = []
        for i in range(self.agent_num):
            sub_obs = start_state
            sub_agent_obs.append(sub_obs)
        return sub_agent_obs

    def step(self, actions):
        """
        # self.agent_num设定为2个智能体时，actions的输入为一个2纬的list，每个list里面为一个shape = (self.action_dim, )的动作数据
        # 默认参数情况下，输入为一个list，里面含有两个元素，因为动作维度为5，所里每个元素shape = (5, )
        # When self.agent_num is set to 2 agents, the input of actions is a 2-dimensional list, each list contains a shape = (self.action_dim, ) action data
        # The default parameter situation is to input a list with two elements, because the action dimension is 5, so each element shape = (5, )
        """
        next_state, reward, done, _ = self.env.step(np.concatenate(actions))
        sub_agent_obs = []
        sub_agent_reward = []
        sub_agent_done = []
        sub_agent_info = []
        for i in range(self.agent_num):
            sub_agent_obs.append(next_state)
            sub_agent_reward.append([reward])
            sub_agent_done.append(done)
            sub_agent_info.append({})

        return [sub_agent_obs, sub_agent_reward, sub_agent_done, sub_agent_info]

    def render(self, mode):
        self.env.render(mode)
