import pymysql
from board.vo import Board


# 번호 id / 이름 pwd

# Dao
class BoardDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='', db='encore_db', charset='utf8')

    def disconn(self):
        self.conn.close()

    # 추가 메서드
    def insert(self, a: Board):  # a는 Addr객체
        # 1. db 커넥션 수립
        self.connect()

        # 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
        cursor = self.conn.cursor()

        # 3. 실행할 sql문 정의
        sql = 'insert into Board(writer, w_date, title,content) values(%s, now(), %s, %s)'

        # 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
        d = (a.writer, a.title, a.content)

        # 5. sql 실행(실행할 sql, %s매칭한 튜플)
        cursor.execute(sql, d)

        # 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
        self.conn.commit()

        # db 커넥션 끊음
        self.disconn()

        # 검색 메서드

    def select(self, num: int):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select*from Board where num=%s'
            d = (num,)
            cursor.execute(sql, d)  # sql 실행
            row = cursor.fetchone()  # fetchone() : 현재 커서 위치의 한 줄 추출
            if row:
                return Board(row[0], row[1], row[2], row[3], row[4])

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 작성자로 가져오기
    def selectByWriter(self, writer: str):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select*from board where writer like %s'
            d = (writer,)
            cursor.execute(sql, d)  # sql 실행
            res = [Board(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
            # for row in cursor:
            #     res.append(Board(row[0], row[1], row[2], row[3], row[4]))
            return res

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 글 제목으로 가져오기
    def selectByTitle(self, title: str):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select*from board where title like %s'
            d = (title,)
            cursor.execute(sql, d)  # sql 실행
            res = [Board(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
            # for row in cursor:
            #     res.append(Board(row[0], row[1], row[2], row[3]))
            return res

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 삭제(name)
    def delete(self, num: int):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'delete from board where num = %s'
            d = (num,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('삭제가 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def update(self, a: Board):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'update board set title=%s, content=%s where num = %s'

            d = (a.title, a.content, a.num,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('수정이 완료 되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def selectAll(self):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성글
            sql = 'select*from board'
            cursor.execute(sql)
            res = [Board(row[0], row[1], row[2], row[3], row[4]) for row in cursor]
            return res

        except Exception as e:
            print(e)

        finally:
            self.disconn()
