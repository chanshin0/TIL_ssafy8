-- DDL : 데이터 정의 언어

-- 1. CREATE TABLE. 테이블 생성
--  데이터 타입과 제약조건(contraits)를 설정한다.
CREATE TABLE contacts(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- 2. ALTER TABLE 역할 네가지
-- 테이블 수정, 컬럼수정, 컬럼 추가, 컬럼 삭제,
ALTER TABLE contacts RENAME TO new_contacts;

ALTER TABLE new_contacts RENAME COLUMN name To last_name;

ALTER TABLE new_contacts ADD COLUMN adress TEXT NOT NULL DEFAULT 'no adress';
-- 만약, 테이블에 데이터가 저장되어있는 상태에서 컬럼을 추가할 경우 기존 데이터는 새 컬럼에 데이터가 없고 NOT NULL 제약을 넣어놨기 때문에 에러가 난다. 이를 방지하기위해 DEFAULT를 설정하고, 기존 데이터의 새 컬럼에는 'no adress'가 담긴다.

ALTER TABLE new_contacts DROP COLUMN adress;


-- 3. DROP TABLE.  테이블 삭제
-- 단, 실행취소가 불가능하기 때문에 주의.
DROP TABLE new_contacts;

-- 위 세가지가 'DDL'!