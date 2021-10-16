import requests
from requests import exceptions

JSESSIONID = ""
CODE = """"""

class Solve:
    def __init__(self, jsessionid) -> None:
        self.solution_url = "https://zerojudge.tw/Solution.api"
        self.jsessionid = jsessionid

    def code_reader(self, code_path:str) -> str:
        code = open(code_path, 'r')
        code_content = code.read()
        code.close()
        return code_content
    
    def data_generator(self, language:str, code:str, problemid:str, action:str, contestid:str):
        return {
            'action': action,
            'language': language,
            'code': self.code_reader(code_path= code),
            'contestid': contestid,
            'problemid': problemid
        }

    def send(self, language:str, code:str, problemid:str ,action:str = 'SubmitCode', contestid:int = 0):
        post_data = self.data_generator(
                                        language= language,
                                        code= code,
                                        problemid= problemid,
                                        action= action,
                                        contestid= contestid
                                    )
        post_header = {'cookie': self.jsessionid}
        post_request = requests.post(self.solution_url, headers= post_header, data= post_data)
        return post_request
    
if __name__ == '__main__':
    if not JSESSIONID: JSESSIONID = input('[Input your JESSIONID]: ')
    Solver = Solve(JSESSIONID)
    while (True):
        Problem_ID = input('[Problem ID]: ')
        Language = input('[Language](PYTOHN, CPP, C, JAVA): ')
        Code = input('[Code File Path]: ')

        print('The parameters below have preset values. If there is no need to change, just enter and skip!')

        _Contestid = input('[Contest ID (default:0)]: ')
        Contestid = _Contestid or '0' 

        _Action = input('[Action (default:SubmitCode)]: ')
        Action = _Action or 'SubmitCode'

        try: 
            Solver.send(Language, Code, Problem_ID, Action, Contestid)
            print('*Sending Solving Code Succesfully!!*')
        except Exception as e:
            print(f'exception-{e}')