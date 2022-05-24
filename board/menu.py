from board.service import BoardService


class Menu:
    def __init__(self):
        self.service = BoardService()

    def run(self):
        while True:
            m = input('1.글 쓰기 2.글 번호로 검색 3.글 작성자로 검색 4.타이틀로 검색  5. 수정 6.삭제 7.전체 출력 8.종료  \n')
            if m == '1':
                self.service.addBoard()
            elif m == '2':
                self.service.getByNum()
            elif m == '3':
                self.service.getByWriter()
            elif m == '4':
                self.service.getByTitle()
            elif m == '5':
                self.service.editBoard()
            elif m == '6':
                self.service.delBoard()
            elif m == '7':
                self.service.printAll()
            elif m == '8':
                break


if __name__ == '__main__':
    m = Menu()
    m.run()
