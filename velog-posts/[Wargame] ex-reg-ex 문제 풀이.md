<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.26</li>
<li>문제명: ex-reg-ex</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/834">https://dreamhack.io/wargame/challenges/834</a></li>
<li>핵심 키워드: Regular Expression (정규표현식), Python re module, Input Validation</li>
</ul>
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제공된 문제 파일을 Visual Studio Code로 열어보았다.</p>
<p><strong>문제 파일</strong></p>
<pre><code>#!/usr/bin/python3
from flask import Flask, request, render_template
import re

app = Flask(__name__)

try:
    FLAG = open(&quot;./flag.txt&quot;, &quot;r&quot;).read()       # flag is here!
except:
    FLAG = &quot;[**FLAG**]&quot;

@app.route(&quot;/&quot;, methods = [&quot;GET&quot;, &quot;POST&quot;])
def index():
    input_val = &quot;&quot;
    if request.method == &quot;POST&quot;:
        input_val = request.form.get(&quot;input_val&quot;, &quot;&quot;)
        m = re.match(r'dr\w{5,7}e\d+am@[a-z]{3,7}\.\w+', input_val)
        if m:
            return render_template(&quot;index.html&quot;, pre_txt=input_val, flag=FLAG)
    return render_template(&quot;index.html&quot;, pre_txt=input_val, flag='?')

app.run(host=&quot;0.0.0.0&quot;, port=8000)
</code></pre><p>제공된 app.py 소스 코드를 분석해보면, 사용자가 POST 요청으로 input_val 값을 보내면 파이썬의 re.match() 함수를 통해 특정 정규표현식 패턴과 일치하는지 검사한다.</p>
<pre><code>m = re.match(r'dr\w{5,7}e\d+am@[a-z]{3,7}\.\w+', input_val)
if m:
    return render_template(&quot;index.html&quot;, pre_txt=input_val, flag=FLAG)</code></pre><p> 입력받은 input_val이 r'dr\w{5,7}e\d+am@[a-z]{3,7}.\w+' 정규식 패턴을 통과하면 flag.txt의 내용을 화면에 출력해 준다.</p>
<hr />
<h2 id="3-문제-해결-과정-정규표현식-해석">3. 문제 해결 과정 (정규표현식 해석)</h2>
<p><a href="https://regexr.com/">https://regexr.com/</a> 과 같은 툴을 이용해 패턴을 조각내어 분석했다. 정규표현식은 왼쪽부터 오른쪽으로 순서대로 조건을 덧붙여 읽으면 된다.</p>
<p>dr: 알파벳 소문자 dr로 시작해야 한다.</p>
<p><code>\w{5,7}</code>: <code>\w</code>는 Word 문자(알파벳 대소문자, 숫자, 언더스코어 _)를 의미한다. {5,7}은 이 문자가 5개에서 7개 사이로 와야 함을 뜻한다. (예: aaaaa)</p>
<p><code>e</code>: 알파벳 소문자 e가 와야 한다.</p>
<p><code>\d+</code>: <code>\d</code>는 숫자(0-9)를 의미하며, +는 1개 이상을 뜻한다. (예: 1 또는 123)</p>
<p><code>am@</code>: 문자열 am@가 와야 한다.</p>
<p><code>[a-z]{3,7}</code>: [a-z]는 알파벳 소문자만 허용함을 의미한다. {3,7}이므로 3개에서 7개 사이여야 한다. (예: abc)</p>
<p><code>\.</code>: .은 정규식에서 '모든 문자'를 뜻하는 특수기호인데, 앞에 역슬래시(<code>\</code>)를 붙였으므로 실제 마침표(.) 문자 자체를 의미한다.</p>
<p><code>\w</code>+: 다시 [A-Z a-z 0-9 _ ] 문자가 1개 이상 와야 한다. (예: 0)</p>
<p>즉: <a href="mailto:draaaaae1am@abc.0">draaaaae1am@abc.0</a> 이 된다. 이 문자열을 생성한 가상 머신에 제출하면 DH{e64a267ab73ae3cea7ff1255b5f08f3e5761defbfa6b99f71cbda74b7a717db3} 값을 얻을 수 있다.</p>
<hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<p>소스코드(app.py)의 주요 동작 원리는 다음과 같다. Python의 Flask 프레임워크를 기반으로 동작하는 웹 서버 코드이다.</p>
<ol>
<li><strong>플래그 파일 로드 (try - except):</strong><pre><code>try:
 FLAG = open(&quot;./flag.txt&quot;, &quot;r&quot;).read()       # flag is here!
except:
 FLAG = &quot;[**FLAG**]&quot;</code></pre></li>
</ol>
<ul>
<li>서버가 켜질 때 같은 디렉터리에 있는 flag.txt 파일을 읽어와 FLAG 변수에 저장한다. 파일이 없으면 예외 처리된다.</li>
</ul>
<ol start="2">
<li><strong>라우팅 및 데이터 수신 (@app.route, request.method):</strong></li>
</ol>
<pre><code>@app.route(&quot;/&quot;, methods = [&quot;GET&quot;, &quot;POST&quot;])
def index():
    input_val = &quot;&quot;
    if request.method == &quot;POST&quot;:
        input_val = request.form.get(&quot;input_val&quot;, &quot;&quot;)</code></pre><ul>
<li>클라이언트가 / 경로로 POST 요청을 보내면, 폼(form) 데이터 중 input_val 파라미터 값을 가져온다.</li>
</ul>
<ol start="3">
<li><p><strong>정규표현식 매칭 및 플래그 출력 (re.match):</strong></p>
<pre><code>m = re.match(r'dr\w{5,7}e\d+am@[a-z]{3,7}\.\w+', input_val)
     if m:
         return render_template(&quot;index.html&quot;, pre_txt=input_val, flag=FLAG)
 return render_template(&quot;index.html&quot;, pre_txt=input_val, flag='?')</code></pre><ul>
<li>파이썬의 re 모듈을 사용해 입력받은 input_val이 타겟 정규표현식 패턴과 일치(match)하는지 검사한다.</li>
<li>결과: 조건을 통과하면 숨겨둔 FLAG 변수를 포함해 index.html을 렌더링(출력)하고, 실패하면 플래그 부분에 ?를 띄운다.</li>
</ul>
</li>
</ol>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>정규표현식(Regex)의 작동 원리 체득</strong> 처음엔 외계어 같았던 특수기호(\w, \d, +, {})들이 각각 어떤 데이터 타입을 필터링하고 길이를 제한하는지 직접 분해하고 조립하며 원리를 이해했다.</li>
<li><strong>보안 필터링과 WAF(Web Application Firewall)의 이해:</strong> 이번 문제는 정규표현식을 '통과'하는 문자열을 찾는 것이었지만, 반대로 생각하면 인프라 엔지니어가 악의적인 입력을 차단(Block)하기 위해 이런 식별 규칙을 사용한다는 것을 깨달았다. WAF의 핵심 룰셋이나 서버 접근 로그(Access Log)에서 공격 시도를 추출할 때 정규표현식이 필수적으로 쓰인다는 점을 상기하게 되었다.</li>
</ul>
<p>찾아보니, 정규표현식을 잘못 작성할 경우(예: 백트래킹이 심하게 발생하는 패턴) 해커가 악의적인 문자열을 던져 서버의 CPU를 100%로 마비시키는 ReDoS 공격이 가능하다는 것을 알게 되었다. 인프라를 운영할 때, 개발자가 작성한 정규식이 서버 성능에 악영향을 주지 않는지 검증하는 것도 엔지니어의 중요한 역할임을 배웠다. 단순한 문법 학습을 넘어, 안전하고 효율적인 필터링 설계의 중요성을 체감했다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/37d9b082-ddff-4307-8df2-acf3c092513a/image.jpg" /></p>