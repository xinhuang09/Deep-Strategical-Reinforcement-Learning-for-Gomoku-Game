import numpy as np
import gym, glob, tictactoe_env
import tensorflow
import rl

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory

#Use keras to build a deep learning network, and choose relu as our activation function
def Model(input_shape, output_neurons):
    model = Sequential()
    model.add(Flatten(input_shape=(1,) + input_shape))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dense(output_neurons))
    model.add(Activation('linear'))
    print(model.summary())
    return model

def get_path(weights_name):
    path = None
    for f in glob.glob(weights_name):
        if(f != ""):
            path = f
            break
    return path

def main():
    name = "tic_tac_toe_dqn_agent.h5f"
    ENV_NAME = 'tictactoe-v0'
    env = gym.make(ENV_NAME)
    network = Model(env.get_obs_space().shape, env.get_action_space().n)
    #Configure Agent
    memory = SequentialMemory(limit = 50000, window_length = 1)
    #We use epsilon-greedy as our policy
    policy = EpsGreedyQPolicy()
    #Choose DQN model as our agent
    dqn_model = DQNAgent(model = network, memory = memory, policy = policy, nb_actions = env.get_action_space().n, nb_steps_warmup = 10, gamma = 0.3)
    dqn_model.compile(Adam(lr=1e-3), metrics=['accuracy', 'mae'])
    # First Agent Training
    for i in range (0, 10):
        env.reset_all()
        path2 = get_path(name)
        if (path2 != None):
            dqn_model.load_weights(path2)
        dqn_model.fit(env, nb_steps = 10000, visualize=True, verbose=2)
        #Save model
        dqn_model.save_weights(name, overwrite=True)

if __name__ == '__main__':
    main()
