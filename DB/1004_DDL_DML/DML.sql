-- DML : 데이터 조작 언어

-- 1. users라는 테이블을 만들고 user.csv파일을 import함 
CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);


------------여기서부터 DML---------------------------------------

-- 1. Select statement. 절이 무지많아서 젤 복잡하다.
-- 이름과 나이 조회하기
SELECT first_name, age FROM users;

-- 전체 데이터 조회하기
SELECT * FROM users;

-- rowid 조회하기. 이렇게 명시를 하면 조회된다.
SELECT rowid, first_name FROM users;

-- 2-1. Sorting rows. 정렬하기
-- ORDER BY clause
-- 이름과 나이를 나이가 어린 순으로 조회하기, 오름차순은 디폴트이기 때문에 ASC안써도 됨.
SELECT first_name, age FROM users ORDER BY age ASC;
-- 내림차순
SELECT first_name, age FROM users ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로, 만약 같은 나이라면 계좌잔고가 많은 순으로.
SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC ;
-- 참고, NULL은 가장 작은 값으로 봄.

-- 2-2. Filtering data. 데이터를 필터링하여 중복제거, 조건설정 등 쿼리를 제어하기

-- 2-2-1. SELECT DISTINCT. 중복을 제거한다
SELECT country FROM users;  
SELECT DISTINCT country FROM users;
-- 지역순으로 내림차순 하여 중복없이 조회하기
SELECT DISTINCT country FROM users ORDER BY country;
-- 이름과 지역이 중복 없이 모두 조회하기
SELECT DISTINCT first_name, country FROM users;
-- 지역을 내림차순으로 이름과 지역을 중복없이 모두 조회하기
SELECT DISTINCT first_name, country FROM users ORDER BY country DESC;
-- 참고. NULL도 중복으로 간주해서 한 행만 조회됨

-- 2-2-2. WHERE claus. 특정 조건을 지정해서 조회
-- 연산자 활용가능.

SELECT first_name, age, balance FROM users WHERE age >= 30;
-- 나이가 30살 이상인 사람들의 이름, 나이 ,계좌잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance >= 500000;

-- 2-2-3. LIKE operator. 패턴 일치를 기반으로 데이터를 조회. but, 대소문자는 구분하지 않는다.
-- 두가지의 wildcards가 있다.
-- 1) %(percent) : 0개 이상의 문자가 올 수 있음을 의미. 도%, %도, %도%
-- 2) _(underscore) : 단일 문자가 있음을 의미. _하나당 딱 한글자 의미

SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';
-- 이름에 호가 들어가는 사람들의 이름과 성을 조회하라
SELECT first_name FROM users WHERE first_name LIKE '%준';

SELECT first_name, phone FROM users WHERE phone LIKE '02-%';

SELECT first_name, age FROM users WHERE age LIKE '2_';
-- 20대 조회하기

SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';
-- 중간 4자리가 51로 시작하는 사람들 조회

-- 2-2-4. IN operator
SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
SELECT first_name, country FROM users WHERE country = '경기도' OR country = '강원도';

SELECT first_name, country FROM users WHERE country NOT IN ('경기도', '강원도');

-- 2-2-5. Between operator
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age >= 20 AND age <= 30;

SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
SELECT first_name, age FROM users WHERE age < 20 OR age > 30;
-- 부정

-- 2-3. LIMIT clause. 결과에서 행 수를 제한할 수 있다.
SELECT rowid, first_name FROM users LIMIT 10;

SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
-- 계좌잔고가 가장 많은 10명 조회하라

-- 2-3-1. OFFSET keyword
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
-- 앞에 10개(LIMIT) 점프하고, 11번째부터 20번째까지(10개) 조회하라


-- 3. GROUP BY clause. COUNT와 같은 내장함수들이 있다.
SELECT country, COUNT(*) FROM users GROUP BY country;
-- 각 지역 별로 그룹핑하고, 그 그룹핑의 결과를 카운팅.

-- 3-1. Aggregate function. 집계 함수!
-- 목록 : AVG(), COUNT(), MAX(), MIN(), SUM()
SELECT COUNT(*) FROM users;
-- user 테이블의 전체 행수를 조사. 레코드가 1000개

SELECT AVG(age) FROM users WHERE age >= 30;
-- 나이가 30살 이상인 사람들의 나이 평균 조회하라

SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
-- 각 성씨가 몇 명씩 있는지 조회하라
-- 사실.. (*)이든 (name)이든 조회되는 결과는 똑같다. 또한, AS를 활용해 컬럼의 이름을 지정해 줄 수 있다.
----------------------여기까지 SELECT-------------------------
-- 2. Changing data
-- INSERT, UPDATE, DELETE. SELECT에 비해 비교적 간단하다.

-- 실습 편의를 위해 새 테이블 하나 만듦
CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- 2-1. INSERT statement
-- 행을 추가하는 것, 각 컬럼에 대한 값을 넣어줘야 한다.
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('홍길동', 23, '서울');
-- 이렇게 생략가능, but 1대1 대응 안될 시 에러
INSERT INTO classmates VALUES ('홍길동', 23, '서울'),('홍길동2', 23, '서울'),('홍길동3', 23, '서울'),('홍길동4', 23, '서울');
-- 여러 개일 땐 이렇게.

-- 2-2. UPDATE statement
 UPDATE classmates SET name='김철수한무두루미', address='제주도' WHERE rowid = 2;
--  where를 생략할시 모든 레코드가 수정된다.

-- 2-3. DELETE statement
DELETE FROM classmates WHERE rowid = 2;
-- 마찬가지로, where절 생략할 시 모든 데이터가 삭제됨
SELECT rowid, * FROM classmates;
-- 조회하면 1~n개의 레코드 중에 2번 레코드 삭제돼있음