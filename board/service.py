from board.vo import Board
from board.dao_db import BoardDao
from member.service import MemberService


class BoardService:

    def __init__(self):
        self.dao = BoardDao()

    # 글쓰기
    def addBoard(self):
        print('=== 글 쓰기 ===')
        if MemberService.loginId == '':
            print('로그인 먼저 하시오')
            return
        else:
            writer = MemberService.loginId
            title = input('title :')
            content = input('content :')
            self.dao.insert(Board(writer=writer, title=title, content=content))

    def getByNum(self):
        print('=== 번호로 검색===')
        num = int(input('search num : '))
        a: Board = self.dao.select(num)
        if a is None:
            print('없는 게시물 번호')
        else:
            print(a)

    # 검색
    def getByWriter(self):
        print('=== 작성자로 검색 ===')
        writer = input('writer :')
        res = self.dao.selectByWriter('%' + writer + '%')
        if res is None:
            print('예외발생.')
        elif len(res) == 0:
            print('검색결과없음')
        else:
            for i in res:
                print(i)

    # 검색
    def getByTitle(self):
        print('=== 글 제목으로 검색 ===')
        title = input('title :')
        res = self.dao.selectByTitle('%' + title + '%')
        if res is None:
            print('예외발생.')
        elif len(res) == 0:
            print('검색결과없음')
        else:
            for i in res:
                print(i)

    # 수정
    def editBoard(self):
        print('=== 글 수정 ===')
        if MemberService.loginId=='':
            print('로그인 먼저 하시오')
            return
        else:
            num = input('num :')
            a: Board = self.dao.select(num)
            if a is None:
                print('해당 번호의 게시글이 없습니다.')
            else:
                # a.name=input('name : ')
                # a.tel=input('tel : ')
                # a.addr=input('addr : ')
                # self.dao.update(a)
                s = ['title', 'content']
                data = [input('new ' + s[i] + ':') for i in range(len(s))]
                for idx, i in enumerate(data):
                    if i != '':
                        # 객체 클래스 변수 수정
                        a.__setattr__(s[idx], i)

                self.dao.update(a)

    # 삭제
    def delBoard(self):
        print('=== 글 삭제 ===')
        if MemberService.loginId=='':
            print('로그인 먼저 하시오')
            return
        else:
            num = input('num :')
            self.dao.delete(num)

    # 전체출력
    def printAll(self):
        data = self.dao.selectAll()
        for i in data:
            print(i)


