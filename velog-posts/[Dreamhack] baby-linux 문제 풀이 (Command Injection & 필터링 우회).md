<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.11</li>
<li>문제명: baby-linux</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/837">https://dreamhack.io/wargame/challenges/837</a></li>
<li>핵심 키워드: Command Injection, Blacklist Filtering Bypass, Flask, Subprocess</li>
</ul>
<hr />
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제시된 문제는 사용자 입력값을 받아 서버 측 리눅스 셸에서 명령어를 실행하는 웹 서비스이다.</p>
<p><strong>문제 코드 분석(app.py)</strong></p>
<pre><code class="language-python">#!/usr/bin/env python3
import subprocess
from flask import Flask, request, render_template

APP = Flask(__name__)

@APP.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        cmd = f'echo $({user_input})'
        if 'flag' in cmd:
            return render_template('index.html', result='No!')

        try:
            output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
            return render_template('index.html', result=output.decode('utf-8'))
        except subprocess.TimeoutExpired:
            return render_template('index.html', result='Timeout')
        except subprocess.CalledProcessError:
            return render_template('index.html', result='Error')

    return render_template('index.html')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8000)</code></pre>
<ul>
<li><p>입력 방식: 사용자가 입력한 user_input이 echo $({user_input}) 형태로 조립되어 명령어 실행 치환(Command Substitution) 구문 $() 안으로 들어간다.</p>
</li>
<li><p>필터링 조건: if 'flag' in cmd: 구문을 통해 cmd 문자열 내에 flag라는 단어가 포함되면 No!를 반환하며 차단(Blacklist)한다.</p>
</li>
</ul>
<hr />
<h2 id="3-문제-해결-과정">3. 문제 해결 과정</h2>
<ol>
<li><p>flag.txt 파일의 내용을 출력해야 하지만, flag 키워드가 들어간 문자열을 그대로 전송하면 if 'flag' in cmd 조건문에 의해 차단된다. 이를 우회하기 위해 와일드카드 문자(?)를 활용하여 flag 문자열 검증을 회피하는 전략을 세웠다.</p>
</li>
<li><p>절대/상대 경로와 와일드카드(?)를 조합하여 다음과 같이 입력을 제출하였다.</p>
</li>
</ol>
<pre><code>cat ./dream/hack/hello/f?ag.txt</code></pre><p>이 구문은 문자열에 flag가 직접 들어가지 않으므로 검증 로직을 무사히 통과하며, 셸 내에서 와일드카드 f?ag.txt가 flag.txt로 정상 매칭되어 실행된다.</p>
<ol start="3">
<li>입력 제출 후 cat 명령어의 실행 결과가 정상적으로 출력되어 DH{...} 플래그를 획득하였다.</li>
</ol>
<ul>
<li>실제 서버에서 실행된 명령어</li>
</ul>
<pre><code>echo $(cat ./dream/hack/hello/f?ag.txt)</code></pre><hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<p> <strong>Wildcard (?)를 통한 Blacklist Bypass::</strong></p>
<ul>
<li>물음표(?)는 임의의 한 문자를 대체하는 리눅스 셸 와일드카드이다.</li>
<li>f?ag.txt는 파일 시스템상에서 flag.txt를 가리키지만, 파이썬 코드의 문자열 차단 조건인 'flag' in cmd에는 걸리지 않아 필터링을 완벽히 우회한다.</li>
</ul>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>블랙리스트 기반 필터링의 한계:</strong> 특정 단어(flag)만을 차단하는 방식은 와일드카드(?, *),경로 표현식, 변수 분할 등 셸의 다양한 특수 문자를 이용한 우회 기법에 취약하다는 점을 확인했다.</li>
<li><strong>시큐어 코딩의 중요성:</strong> ubprocess.check_output 사용 시 셸을 매개로 명령어를 실행(/bin/sh -c)하는 구조를 피하고, 입력값 검증 시 강력한 화이트리스트 방식을 적용해야 함을 배웠다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/42a624f6-8ca1-4141-9402-b504be55dd1b/image.jpg" />
<img alt="" src="https://velog.velcdn.com/images/huijeong211/post/c2c8365b-ec96-40dc-aecb-60a37accfb27/image.jpg" />
<img alt="" src="https://velog.velcdn.com/images/huijeong211/post/52239a6d-2f17-49e0-a859-58ad6c5835db/image.jpg" />
<img alt="" src="https://velog.velcdn.com/images/huijeong211/post/83f68ab9-6dc5-4409-8f78-28858aace19a/image.jpg" /></p>