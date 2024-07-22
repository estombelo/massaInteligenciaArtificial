import random

from Agent0 import Agent
from Environment0 import Environment
from TrivialVacuumEnvironment0 import TrivialVacuumEnvironment


def test_environment():
    v = Environment()
    v.is_done()
    v.step()
    v.run()


def test_agent():
    def constant_prog(percept):
        return percept

    agent = Agent(constant_prog)
    result = agent.program(5)
    assert result == 5


test_environment()
test_agent()


def test_inseriragentenoambiente():
    v = Environment()
    agent = Agent()
    agent2 = Agent()

    o = v.is_done()
    print("    Sem agente is_done={}".format(o))

    v.add_thing(agent, "area1")
    v.add_thing(agent2, "area1")

    o = v.is_done()
    print("    Com agente inserido is_done={}".format(o))

    # v.step() # Erro: falta implementar método percept()
    # v.run() # Erro: falta implementar método percept()
    allthings = v.list_things_at("area1")
    print(f"Lista de coisas dentro do ambiente:{allthings}")


test_inseriragentenoambiente()


def RandomAgentProgram(actions):
    return lambda percept: random.choice(actions)


def test_trivialvacuumenvironment():
    v = TrivialVacuumEnvironment()

    list = ['Right', 'Left', 'Suck', 'NoOp']
    program = RandomAgentProgram(list)

    agent = Agent(program)

    v.add_thing(agent, location=(0,0))

    print('\n')
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    v.step()
    print("Desempenho: {}".format(agent.performance))
    print(f"    status mundo:  {v.status}")

    # v.run(10)


test_trivialvacuumenvironment()
