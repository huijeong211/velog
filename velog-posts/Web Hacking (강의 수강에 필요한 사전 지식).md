<p>학습일: 2026.08.12
링크:<a href="https://learn.dreamhack.io/453#2">https://learn.dreamhack.io/453#2</a>
Dream Biginner - 컴퓨터 과학 기초 - Web Hacking - 강의 수강에 필요한 사전 지식</p>
<h4 id="flask와-mysql을-활용하여-구현된-웹-서비스">Flask와 MySQL을 활용하여 구현된 웹 서비스</h4>
<pre><code>#!/usr/bin/env python3
import os
import pymysql
from flask import Flask, abort, redirect, render_template, request

PAGINATION_SIZE = 10

app = Flask(__name__)
app.secret_key = os.urandom(32)

def connect_mysql():
    conn = pymysql.connect(host='db',
                           port=3306,
                           user=os.environ['MYSQL_USER'],
                           passwd=os.environ['MYSQL_PASSWORD'],
                           db='board',
                           charset='utf8mb4')
    cursor = conn.cursor()
    return conn, cursor

@app.route('/')
def index():
    return redirect('/board')

@app.route('/board')
def board():

    page = request.args.get('page')
    page = int(page) if page and page.isdigit() and int(page) &gt; 0 else 1

    ret = []

    conn, cursor = connect_mysql()
    try:
        query = 'SELECT _id, title FROM posts ORDER BY _id DESC LIMIT %s, %s'
        cursor.execute(query, ((page - 1) * PAGINATION_SIZE, PAGINATION_SIZE))
        ret = cursor.fetchall()
    except Exception as e:
        print(e, flush=True)
        abort(400)
    finally:
        cursor.close()
        conn.close()

    return render_template('board.html', page=page, ret=ret)

@app.route('/board/&lt;post_id&gt;')
def board_post(post_id):

    if not post_id or not post_id.isdigit() or int(post_id) &lt; 1:
        abort(400)

    ret = None

    conn, cursor = connect_mysql()
    try:
        query = 'SELECT title, content FROM posts WHERE _id = %s'
        cursor.execute(query, (post_id, ))
        ret = cursor.fetchone()
    except Exception as e:
        print(e, flush=True)
        abort(400)
    finally:
        cursor.close()
        conn.close()

    if not ret:
        abort(404)

    return render_template('post.html', title=ret[0],
                           content=ret[1], post_id=post_id)

@app.route('/write_post', methods=['POST'])
def write_post():
    if 'title' not in request.form or 'content' not in request.form:
        return render_template('write_post.html')

    title = request.form['title']
    content = request.form['content']

    conn, cursor = connect_mysql()
    try:
        query = 'INSERT INTO posts (title, content) VALUES (%s, %s)'
        cursor.execute(query, (title, content))
        conn.commit()
    except Exception as e:
        print(e, flush=True)
        abort(400)
    finally:
        cursor.close()
        conn.close()

    return redirect('/board')

@app.route('/modify_post', methods=['POST'])
def modify_post():
    post_id = request.form['post_id']

    if not post_id or not post_id.isdigit() or int(post_id) &lt; 1:
        abort(400)

    if 'title' not in request.form or 'content' not in request.form:
        conn, cursor = connect_mysql()
        try:
            query = 'SELECT title, content FROM posts WHERE _id = %s'
            cursor.execute(query, (post_id, ))
            ret = cursor.fetchone()
        except Exception as e:
            print(e, flush=True)
            abort(400)
        finally:
            cursor.close()
            conn.close()

        if not ret:
            abort(404)

        return render_template('modify_post.html', title=ret[0],
                               content=ret[1], post_id=post_id)

    title = request.form['title']
    content = request.form['content']

    conn, cursor = connect_mysql()
    try:
        query = 'UPDATE posts SET title=%s, content=%s WHERE _id = %s'
        cursor.execute(query, (title, content, post_id, ))
        conn.commit()
    except Exception as e:
        print(e, flush=True)
    finally:
        cursor.close()
        conn.close()

    return redirect(f'/board/{post_id}')

@app.route('/delete_post', methods=['POST'])
def delete_post():

    post_id = request.form['post_id']
    if not post_id or not post_id.isdigit() or int(post_id) &lt; 1:
        abort(400)

    if 'answer' not in request.form:
        return render_template('delete_post.html', post_id=post_id)

    if request.form['answer'] == 'y':
        conn, cursor = connect_mysql()
        try:
            query = 'DELETE FROM posts WHERE _id = %s'
            cursor.execute(query, (post_id, ))
            conn.commit()
        except Exception as e:
            print(e, flush=True)
        finally:
            cursor.close()
            conn.close()

        return redirect('/board')

    return redirect(f'/board/{post_id}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
</code></pre><p>이 웹 소스를 읽고 이해할 수 있는 수준이 되어야한다.</p>
<p>웹 기초 지식에 관련된 내용(1-10)
위 소스 코드와 관련된 질문(11-14)</p>
<ol>
<li>웹 브라우저와 웹 서버가 통신하는 프로토콜의 약자를 설명할 수 있다</li>
</ol>
<ul>
<li>HTTP (HyperText Transfer Protocol): 웹상에서 클라이언트(브라우저)와 서버 간에 문서 및 데이터를 주고받기 위한 표준 통신 규약(프로토콜)</li>
</ul>
<ol start="2">
<li>웹 사이트 주소에 포함된 &quot;https&quot; 중 &quot;s&quot;가 어떤 의미를 나타내는지 설명할 수 있다</li>
</ol>
<ul>
<li>Secure (안전함): HTTP 통신에 SSL/TLS 암호화 프로토콜을 적용한 것, 서버와 클라이언트 사이의 통신 내용을 암호화하여 도청이나 데이터 변조를 방지</li>
</ul>
<ol start="3">
<li>웹 브라우저와 서버가 이용자의 로그인 상태를 어떤 방법으로 유지하는지 설명할 수 있다.</li>
</ol>
<ul>
<li>쿠키(Cookie)와 세션(Session): 서버가 로그인에 성공한 이용자에게 식별자(Session ID)를 부여하고 이를 쿠키 형태로 브라우저에 저장, 이후 브라우저가 요청할 때마다 해당 쿠키를 함께 전송함으로써 로그인 상태를 지속적으로 확인하고 유지</li>
</ul>
<ol start="4">
<li>요청을 성공적으로 처리했을때, 웹 서버가 어떤 HTTP 상태 코드를 반환해야 하는지 설명할 수 있다.</li>
</ol>
<ul>
<li>200 OK: 요청이 성공적으로 처리
참고: 게시글 작성/수정/삭제 후 다른 페이지로 이동할 때 사용하는 302 Found 리다이렉트 코드도 성공적인 처리 흐름에 포함</li>
</ul>
<ol start="5">
<li>클라이언트의 요청에 오류가 있어서 요청을 처리하지 못했을 때, 웹 서버가 어떤 HTTP 상태 코드를 반환해야 하는지 설명할 수 있다.</li>
</ol>
<ul>
<li>4xx (Client Error):
400 Bad Request: 잘못된 요청 (파라미터 누락, 유효하지 않은 포맷 등)
404 Not Found: 요청한 리소스(페이지, 게시글)가 존재하지 않음</li>
</ul>
<ol start="6">
<li>웹 서버 측에서 발생한 오류로 인해 요청을 처리하지 못했을때, 웹 서버가 어떤 HTTP 상태 코드를 반환해야 하는지 설명할 수 있다.</li>
</ol>
<ul>
<li>5xx (Server Error):
500 Internal Server Error: 서버 내부 로직 오류 또는 DB 접속 실패 등 예상치 못한 에러가 발생했을 때 반환</li>
</ul>
<ol start="7">
<li>클라이언트와 서버 간의 데이터 전송 시, 인코딩과 암호화 간의 주요한 차이점을 설명할 수 있다.</li>
</ol>
<ul>
<li>인코딩 (Encoding): 데이터를 시스템 간 안전하게 전송하거나 처리하기 위해 포맷을 변환하는 과정. 비밀키 없이 누구나 디코딩하여 원본을 복원할 수 있다. (예: Base64, URL Encoding)
암호화 (Encryption): 인가되지 않은 사람이 데이터를 볼 수 없도록 비밀키(Key)를 사용해 데이터를 난독화하는 과정. 적절한 키 없이는 원본 복구가 불가능. (예: AES, RSA)</li>
</ul>
<ol start="8">
<li>웹 애플리케이션에서 사용자의 입력을 검증하는 이유와 그 중요성을 설명할 수 있다.</li>
</ol>
<ul>
<li>보안 취약점 방지: 입력 검증을 거치지 않으면 SQL Injection, XSS(크로스 사이트 스크립팅), Command Injection 등의 공격에 무방비로 노출.
시스템 안정성 확보: 코드 내 post_id.isdigit()과 같이 숫자인지 검증함으로써 유효하지 않은 입력값으로 인한 DB 에러나 서버 다운을 예방.</li>
</ul>
<ol start="9">
<li>HTTP 메소드에는 어떠한 종류가 있는지 나열할 수 있다.</li>
</ol>
<ul>
<li>GET, POST, PUT, DELETE, PATCH, OPTIONS, HEAD, CONNECT, TRACE 등</li>
</ul>
<ol start="10">
<li>GET 메소드와 POST 메소드의 차이가 무엇인지 설명할 수 있다.</li>
</ol>
<ul>
<li>GET: 데이터를 조회/요청할 때 사용합니다. 데이터가 URL 쿼리 스트링(?key=value)으로 전달되며 크기에 제한이 있고 브라우저 히스토리에 남는다.
POST: 데이터를 생성/수정/삭제 등 변경할 때 사용합니다. 데이터가 HTTP Request Body에 담겨 전달되며, URL에 노출되지 않고 대용량 데이터 전송에 적합</li>
</ul>
<ol start="11">
<li>위의 웹 서비스에 어떤 엔드포인트들이 존재하고, 각 엔드포인트가 수행하는 주요 기능에 대해 설명할 수 있다.</li>
</ol>
<table>
<thead>
<tr>
<th>엔드포인트</th>
<th>HTTP 메소드</th>
<th>주요 기능 설명</th>
</tr>
</thead>
<tbody><tr>
<td>/</td>
<td>GET,메인 인덱스 경로.</td>
<td>/board로 리다이렉트(이동)</td>
</tr>
<tr>
<td>/board</td>
<td>GET</td>
<td>게시글 목록을 조회. page 파라미터를 받아 페이징(10개씩) 처리</td>
</tr>
<tr>
<td>/board/</td>
<td>GET</td>
<td>특정 post_id에 해당하는 게시글의 상세 내용을 조회</td>
</tr>
<tr>
<td>/write_post</td>
<td>POST</td>
<td>새로운 게시글(제목, 내용)을 등록. 입력값이 없으면 작성 폼 화면</td>
</tr>
<tr>
<td>/modify_post</td>
<td>POST</td>
<td>기존 게시글의 제목과 내용을 수정합. 값 전달 유무에 따라 수정 폼을 출력하거나 DB를 업데이트.</td>
</tr>
<tr>
<td>/delete_post</td>
<td>POST</td>
<td>게시글 삭제를 처리. 삭제 확인(answer='y')을 받아 해당 게시글을 DB에서 삭제</td>
</tr>
</tbody></table>
<ol start="12">
<li>각 기능을 수행하기 위해 사용되는 SQL 쿼리를 이해하고 설명할 수 있다.
(1) 게시글 목록 조회 (GET /board)<pre><code>SELECT _id, title FROM posts ORDER BY _id DESC LIMIT %s, %s</code></pre>최근 작성된 글 순서대로 페이징 범위(LIMIT)에 맞게 게시글 ID와 제목을 가져온다.</li>
</ol>
<p>(2) 게시글 상세 조회 (GET /board/, POST /modify_post)</p>
<pre><code>SELECT title, content FROM posts WHERE _id = %s</code></pre><p>특정 _id에 해당하는 게시글의 제목과 내용을 가져온다</p>
<p>(3) 게시글 작성 (POST /write_post)</p>
<pre><code>INSERT INTO posts (title, content) VALUES (%s, %s)</code></pre><p>사용자가 입력한 제목과 내용을 posts 테이블에 신규 등록</p>
<p>(4) 게시글 수정 (POST /modify_post)</p>
<pre><code>UPDATE posts SET title=%s, content=%s WHERE _id = %s</code></pre><p>특정 _id 게시글의 제목과 내용을 전달받은 새 값으로 변경</p>
<p>(5) 게시글 삭제 (POST /delete_post)</p>
<pre><code>DELETE FROM posts WHERE _id = %s</code></pre><p>특정 _id에 해당하는 게시글 레코드를 테이블에서 완전 삭제</p>
<ol start="13">
<li><p>이용자가 POST /write_post 엔드포인트를 통해 게시글을 생성하는 경우, 브라우저, 웹 서비스, 그리고 데이터베이스 간의 상호작용 과정을 상세히 설명할 수 있다.</p>
<p>(1) [브라우저 ➔ 웹 서비스] 이용자가 글 작성 페이지에서 제목과 내용을 입력하고 제출 버튼을 누르면, 브라우저는 POST /write_post 요청을 보내며 Form Data(Body)에 title과 content를 담아 전달합니다.</p>
<p>(2) [웹 서비스] Flask 서버는 write_post() 함수에서 요청 데이터 내 title과 content 필드가 존재하는지 파라미터를 검증합니다.</p>
<p>(3) [웹 서비스 ➔ DB] connect_mysql()을 호출하여 MySQL 커넥션을 생성하고, Prepared Statement 형태의 쿼리(INSERT INTO posts ...)에 전달받은 값들을 바인딩하여 쿼리를 실행합니다.</p>
<p>(4) [DB ➔ 웹 서비스] DB는 쿼리를 실행하여 posts 테이블에 새 레코드를 저장하고, 웹 서비스가 conn.commit()을 수행하여 변경 사항을 최종 반영(저장)합니다.</p>
<p>(5) [웹 서비스 ➔ 브라우저] 처리가 정상 완료되면, 웹 서비스는 브라우저에게 /board로 이동하라는 302 Redirect 응답을 전송합니다.</p>
<p>(6) [브라우저] 응답을 받은 브라우저는 즉시 GET /board 요청을 새롭게 전송하여 갱신된 게시글 목록 화면을 렌더링합니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/3e92e732-8037-48ec-98b1-af78722d13bf/image.jpg" /></p>
</li>
</ol>