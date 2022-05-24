from member.menu import Menu as mMenu
from board.menu import Menu as bMenu


class SMenu:
    def __init__(self):
        self.m_menu = mMenu()
        self.b_menu = bMenu()

    def run(self):
        while True:
            m = input('1.회원관리  2.게시판 3. 종료\n')
            if m == '1':
                self.m_menu.run()
            elif m == '2':
                self.b_menu.run()
            elif m == '3':
                break
