from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Sequence
from sqlalchemy.orm import relationship
from app.src.database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    login = Column(String)
    password = Column(String)
    name = Column(String)
    image_path = Column(String)
    group = Column(String)

    result = relationship('Result', back_populates='user')
    student_in_course = relationship('StudentInCourse', back_populates='user')


class StudentInCourse(Base):
    __tablename__ = 'student_in_course'

    id = Column(Integer, Sequence('student_in_course_id_seq'), primary_key=True)
    student_id = Column(Integer, ForeignKey('user.id'))
    course_id = Column(Integer, ForeignKey('course.id'))

    user = relationship('User', back_populates='student_in_course')
    course = relationship('Course', back_populates='student_in_course')


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    name = Column(String)

    student_in_course = relationship('StudentInCourse', back_populates='course')
    lection = relationship('Lection', back_populates='course')
    test = relationship('Test', back_populates='course')


class Lection(Base):
    __tablename__ = 'lection'

    id = Column(Integer, Sequence('lection_id_seq'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'))
    file_path = Column(String)
    description = Column(String)
    name = Column(String)

    course = relationship('Course', back_populates='lection')


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, Sequence('test_id_seq'), primary_key=True)
    name = Column(String)
    course_id = Column(Integer, ForeignKey('course.id'))

    course = relationship('Course', back_populates='test')
    answer_to_question = relationship('AnswerToQuestion', back_populates='test')
    result = relationship('Result', back_populates='test')


class Result(Base):
    __tablename__ = 'result'

    id = Column(Integer, Sequence('result_id_seq'), primary_key=True)
    student_id = Column(Integer, ForeignKey('user.id'))
    test_id = Column(Integer, ForeignKey('test.id'))
    result = Column(Integer)

    user = relationship('User', back_populates='result')
    test = relationship('Test', back_populates='result')


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, Sequence('question_id_seq'), primary_key=True)
    question = Column(String)

    answer_to_question = relationship('AnswerToQuestion', back_populates='question')


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, Sequence('answer_id_seq'), primary_key=True)
    answer = Column(String)

    answer_to_question = relationship('AnswerToQuestion', back_populates='answer')


class AnswerToQuestion(Base):
    __tablename__ = 'answer_to_question'

    id = Column(Integer, Sequence('answer_to_question_id_seq'), primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    answer_id = Column(Integer, ForeignKey('answer.id'))
    is_correct = Column(Boolean)
    test_id = Column(Integer, ForeignKey('test.id'))

    test = relationship('Test', back_populates='answer_to_question')
    question = relationship('Question', back_populates='answer_to_question')
    answer = relationship('Answer', back_populates='answer_to_question')


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, Sequence('feedback_id_seq'), primary_key=True)
    feedback = Column(String)