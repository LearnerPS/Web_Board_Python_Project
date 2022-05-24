from member.vo import Member
from member.dao_db import MemberDao


class MemberService:
    loginId = ''

    def __init__(self):
        self.dao = MemberDao()

    # 추가
    def addMember(self):
        print('=== 추가 ===')
        id1 = input('id :')
        if self.dao.select(id1) is None:
            pwd = input('pwd :')
            name = input('name :')
            email = input('email :')
            self.dao.insert(Member(id=id1, pwd=pwd, name=name, email=email))
        else:
            print('해당 아이디는 존재합니다.')

    def getById(self):
        print('=== 아이디 검색===')
        id1 = int(input('search id : '))
        a: Member = self.dao.select(id1)
        if a is None:
            print('없는 번호')
        else:
            print(a)

    # 검색
    def seAddr(self):
        print('=== 이름으로 검색 ===')
        name = input('name :')
        res = self.dao.selectByName('%' + name + '%')
        if res is None:
            print('예외발생.')
        elif len(res) == 0:
            print('검색결과없음')
        else:
            for i in res:
                print(i)

    # 삭제
    def delMember(self):
        print('=== 삭제 ===')
        if MemberService.loginId == '':
            print('로그인 먼저 하시오')
            return
        else:
            a = self.dao.select(MemberService.loginId)
            pwd = input('pwd :')
            if pwd == a.pwd:
                MemberService.loginId = ''
                self.dao.delete(a.id)


    # 전체출력
    def printAll(self):
        data = self.dao.selectAll()
        for i in data:
            print(i)

    def login(self):
        if MemberService.loginId != '':
            print('이미 로그인중')
            return
        id1 = input('아이디 :')
        a = self.dao.select(id1)

        if a is None:
            print('없는 아이디입니다')
            return
        else:
            pwd = input('패스워드 :')
            if pwd == a.pwd:
                MemberService.loginId = id1  # 로그인 상태로 만들어줌
                print('로그인 성공')
            else:
                print('패스워드(이름) 불일치')

    def printMyInfo(self):
        if MemberService.loginId == '':
            print('로그인 먼저 하시오')
            return
        else:
            a = self.dao.select(MemberService.loginId)
            print(a)
            print('=== 수정 ===')
            # id = input('id :')
            # a: Member = self.dao.select(num)
            # if a is None:
            #     print('가입되지 않았습니다.')
            # else:
                # a.name=input('name : ')
                # a.tel=input('tel : ')
                # a.addr=input('addr : ')
                # self.dao.update(a)
            s = ['pwd', 'name', 'email']
            data = [input('new ' + s[i] + ':') for i in range(len(s))]
            for idx, i in enumerate(data):
                if i != '':
                    # 객체 클래스 변수 수정
                    a.__setattr__(s[idx], i)

            self.dao.update(a)

    def logout(self):
        if MemberService.loginId == '':
            print('로그인 먼저 하시오')
            return
        MemberService.loginId = ''
        print('로그아웃 완료!')
