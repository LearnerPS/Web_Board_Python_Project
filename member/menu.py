from member.service import MemberService

class Menu:
    def __init__(self):
        self.service=MemberService()

    def run(self):
        while True:
            m= input('1.회원가입 2.로그인 3.내 정보 확인 / 수정  4.로그아웃 5.탈퇴 6.종료  \n')
            if m == '1':
                self.service.addMember()
            elif m == '2':
                self.service.login()
            elif m == '3':
                self.service.printMyInfo()
            elif m == '4':
                self.service.logout()
            elif m == '5':
                self.service.delMember()
            elif m == '6':
                break

if __name__ == '__main__':
    m=Menu()
    m.run()