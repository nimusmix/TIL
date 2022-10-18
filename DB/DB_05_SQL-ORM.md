# DB_05_SQL-ORM

- 전체 인원 수 조회

    ```sql
    # SQL
    SELECT rowid, COUNT(*) FROM users GROUP BY rowid;
    
    # ORM
    User.objects.count()
    len(User.objects.all())
    ```

- 나이가 어린 순으로 이름과 나이 조회

    ```sql
    # SQL
    SELECT first_name, age FROM users ORDER BY age;
    
    # ORM
    User.objects.order_by('age').values('first_name', 'age')
    ```

- 이름, 나이, 계좌 잔고를 나이가 어린 순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 조회

    ```sql
    # SQL
    SELECT first_name, age, balance FROM users ORDER BY age ASC, balance DESC;
    
    # ORM
    User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance')
    ```

- 중복 없이 모든 지역 조회

    ```sql
    # SQL
    SELECT DISTINCT country FROM users;
    
    # ORM
    User.objects.distinct().values('country')
    ```

- 나이가 30세 이상인 사람들의 이름과 나이 조회

    ```sql
    # SQL
    SELECT first_name, age WHERE age >= 30;
    
    # ORM
    User.objects.filter(age__gte=30).values('first_name', 'age')
    ```

- 나이가 30세 이상이고, 계좌 잔고가 50만원 초과인 사람들의 나이, 계좌 잔고 조회

    ```sql
    # SQL
    SELECT age, balance WHERE age >= and balance > 500000;
    
    # ORM
    User.objects.filter(age__gte=30, balance__gt=500000).values('age', 'balance')
    ```

- 이름에 '호'가 포함되는 사람의 이름 조회

    ```sql
    # SQL
    SELECT first_name FROM users WHERE first_name LIKE '%호%';
    
    # ORM
    User.objects.filter(first_name__contains='호').values('first_name')
    ```

- 핸드폰 번호가 011로 시작하는 사람들의 핸드폰 번호 조회

    ```sql
    # SQL
    SELECT phone FROM users WHERE phone LIKE '011-%';
    
    # ORM
    User.objects.filter(phone__startswith='011-').values('phone')
    ```

- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회

    ```sql
    # SQL
    SELECT name, country FROM users WHERE country NOT IN ('경기도', '강원도');
    
    # ORM
    User.objects.exclude(country__in=['경기도', '강원도']).values('first_name', 'country')
    ```

- 나이가 가장 어린 10명의 이름과 나이 조회

    ```sql
    # SQL
    SELECT first_name, age FROM users ORDER BY age LIMIT 10;
    
    # ORM
    User.objects.order_by('age').values('first_name', 'age')[:10]
    ```

- 나이가 30세이거나 성이 김씨인 사람들 조회

    ```sql
    # SQL
    SELECT * FROM users WHERE age = 30 or last_name = '김';
    
    # ORM
    from django.db.models import Q
    
    User.objects.filter(Q(age=30) | Q(last_name='김'))
    ```

- 나이가 30세 이상인 사람들의 평균 나이 조회

    ```sql
    # SQL
    SELECT AVG(age) FROM users WHERE age >= 30;
    
    # ORM
    from django.db.models import Avg
    
    User.objects.filter(age__gte=30).aggregate(Avg('age'))
    # {'age__avg': 37.659}
    User.objects.filter(age__gte=30).aggregate(avg_value=Avg('age'))
    # {'age_value': 37.659}
    ```

- 가장 높은 계좌 잔액 조회

    ```sql
    # SQL
    SELECT balance FROM users ORDER BY balance DESC LIMIT 1;
    
    # ORM
    from django.db.models import Max
    User.objects.aggregate(Max('balance'))
    # {'balance__max': 100000}
    ```

- 각 지역별로 몇 명씩 살고 있는지 조회

    ```sql
    # SQL
    SELECT country, COUNT(*) FROM users GROUP BY country;
    
    # ORM
    from django.db.models import Count
    
    User.objects.values('country').annotate(Count('country'))
    User.objects.values('country').annotate(num_of_country=Count('country'))
    ```

- 각 지역별로 몇 명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회

    ```sql
    # SQL
    SELECT country, COUNT(*), AVG(balance) FROM users GROUP BY country;
    
    # ORM
    User.objects.values('country').annotate(Count('country'), avg_balance=Avg('balance'))
    ```

- 각 게시글의 댓글 개수와 2000-01-01보다 나중에 작성된 댓글의 개수를 조회

    ```sql
    # ORM
    Article.objects.annotate(
      num_of_comment=Count('comment'),
      pub_date=Count('Comment', filter=Q(comment__created_at__lte='2000-01-01'))
    )
    ```

    

## (SQL) DDL-DML

- **DDL** (Data Definituon Language)

    - RDB 구조를 정의하기 위한 명령어

    - `CREATE`, `ALTER`, `DROP`

    - `CREATE`

        ```sql
        CREATE TABLE table_name (
          -- column_name data_type constraints
          name TEXT NOT NULL,
          age INTEGER NOT NULL,
          email TEXT NOT NULL UNIQUE
        )
        ```

    - `ALTER`

        ```sql
        -- 1. Rename a table
        ALTER TABLE table_name RENAME TO new_table_name;
        
        -- 2. Rename a column
        ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;
        
        -- 3. Add a new column to a table
        ALTER TABLE table_name ADD COLUMN new_column TEXT NOT NULL DEFAULT 'default';
        
        -- 4. Delete a column
        -- 컬럼이 다른 부분에서 참조되는 경우, PRIMARY KEY인 경우, UNIQUE 제약 조건이 있는 경우는 삭제 불가!
        ALTER TABLE table_name DROP COLUMN column_name;
        ```

    - `DROP`

        - 한 번에 하나의 테이블만 삭제할 수 있음.
        - 여러 테이블을 삭제하려면 여러 DROP TABLE 문을 실행해야 함.
        - DROP TABLE 문은 실행 취소하거나 복구할 수 없음!

        ```sql
        DROP TABLE table_name;
        ```

- **DML** (Data Manipulation Language)

    - 데이터를 조작하기 위한 명령어
    - `INSERT`, `SELECT`, `UPDATE`, `DELETE`

    - `INSERT`

        ```sql
        INSERT INTO table_name (column1, column2) VALUES (value1, value2)
        
        -- 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을 지정해야 함.
        INSERT INTO classmates
        VALUES
          ('김철수', 30, '경기'),
          ('이영미', 31, '강원'),
          ('박진성', 26, '전라');
        ```

    - `SELECT`

        - SELECT 문 절 순서 : `WHERE` - `GROUP BY` - `ORDER BY` - `LIMIT`

        ```sql
        -- ORDER BY (sorting rows)
        SELECT fisrt_name, age, balnce FROM users ORDER BY age ASC, balance DESC;
        
        -- DISTINNCT (filtering data)
        SELECT DISTINCT country FROM users;
        SELECT DISTINCT first_name, country FROM users;
        SELECT DISTINCT country FROM users ORDER BY country DESC;
        
        -- WHERE (filtering data)
        SELECT first_name FROM users WHERE first_name LIKE '%호%';
        SELECT phone FROM users WHERE phone LIKE '%-51__-%';
        SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
        
        -- LIMIT (filtering data)
        SELECT rowid, first_name FROM users LIMIT 10;
        SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
        SELECT fisrt_name, balance FROM users ORDER BY balance DESC LIMIT 10;
        
        -- GROUP BY (filtering data)
        SELECT AVG(age) FROM users WHERE age >= 30;
        SELECT country, COUNT(*) FROM users GROUP BY country;
        SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;
        ```

    - `UPDATE`

        ```sql
        UPDATE table_name
        SET column_1 = new_value_1,
            column_2 = new_value_2
        WHERE
            search_condition;
            
        UPDATE classmates
        SET name = '김철수한무두루미',
            address = '제주도'
        WHERE rowid = 2;
        ```

    - `DELETE`

        ```sql
        DELETE FROM classmates WHERE rowid = 5;
        DELETE FROM classmates WHERE name LIKE '%영%';
        ```

        