import requests
import json

class ZeroJudge:
    PYTHON = 'PYTHON'
    CPP = 'CPP'
    C = 'C'
    JAVA = 'JAVA'
    
    def __init__(self, jessionid:str) -> None:
        self.test_url = 'https://zerojudge.tw/Testjudge'
        self.problem_url = 'https://zerojudge.tw/ShowProblem'
        self.solution_url = 'https://zerojudge.tw/Solution.json'    
        self.jessionid = jessionid

    def obtain_test_data(self, problemid:str):
        ...

    def test(self, code:str, language:str, problemid:str ,contestid:int = 0):
        ...

    def solve(self, code:str, language:str, problemid:str , action:str = 'SubmitCode', contestid:int = 0):
        ...

    def consult_code(self, solutionid:int, identify:int, data:str = 'Code' ):
        ...
    
    def consult_result(self, solutionid:int, identify:int, data:str = 'ServerOutputs'):
        ...
    
    

