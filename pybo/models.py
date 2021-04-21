# 질문 모델 생성하기

from pybo import db

# Question 클래스는 모든 모델의 기본 클래스인 db.Model을 상속
# db는 __init__.py 파일에서 생성한 SQLAlchemy 객체
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False) #질문 제목 / nullable은 빈값을 뜻함
    content = db.Column(db.Text(), nullable=False) #질문 내용
    create_date = db.Column(db.DateTime(), nullable=False) #질문 작성일시


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set')) #질문 참조
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)