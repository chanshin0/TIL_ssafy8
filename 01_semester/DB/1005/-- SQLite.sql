-- SQLite
-- RDB JOIN하는 법 연습

-- TABLE user
CREATE TABLE user(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT 
);

INSERT INTO user (name) VALUES ('치킨!');
INSERT INTO user (name) VALUES ('삼겹살');
INSERT INTO user (name) VALUES ('돈까스');

-- TABLE article
CREATE TABLE article (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  content TEXT,
  user_id INTEGER NOT NULL,
 
  -- 왜래 키 등록
  -- user_id를 왜래 키로 등록한다.
  -- user에 있는 pk인 id를 참조로 등록한다.
  -- user에 없는 값을 넣으면 에러를 발생시킨다.
  FOREIGN KEY(user_id) REFERENCES user(id)
);

INSERT INTO article (title, content, user_id) VALUES ('test1', 'test1', 1);
INSERT INTO article (title, content, user_id) VALUES ('test2', 'test2', 2);
INSERT INTO article (title, content, user_id) VALUES ('test3', 'test3', 3);
-- INSERT INTO article (title, content, user_id) VALUES ('test4', 'test4', 4);

-- INNER JOIN
-- article에 있는 user_id로부터
-- user의 정보를 합쳐서 가져올 것
-- 값이 중복되는 경우 명시를 해야한다(ex. article.title)
-- id가 누구의 id인지 모르기 때문에 에러를 뱉는다.content

--articles = Article.objects.all()
-- for article in articles
--  print article 
SELECT user.name, article.title, article.content FROM article INNER JOIN user ON article.user_id = user.id;

-- articles = Article.objects.get(pk=1)
-- Django에서 article.user.name, article.user.id
-- ORM을 통해 query를 몰라도 사용 가능
-- query문이 어떻게 동작하는지 알고 쓰면 더 좋다.
SELECT user.name, article.title, article.content FROM article INNER JOIN user ON article.user_id = user.id WHERE article.id == 1;