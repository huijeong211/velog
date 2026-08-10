<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.09</li>
<li>문제명: 64se64</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/872">https://dreamhack.io/wargame/challenges/872</a></li>
<li>핵심 키워드: Base64, Encoding/Decoding, Python Scripting</li>
</ul>
<hr />
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>문제에서 제시된 암호문(또는 파일)을 확인했을 때, 반복적인 인코딩 형태나 Base64 패턴을 띨 가능성을 확인했다.</p>
<ul>
<li><strong>Base64의 특징:</strong><ul>
<li>64개의 ASCII 문자를 사용 (A-Z, a-z, 0-9, +, /)</li>
<li>패딩 문자 <code>=</code> 사용</li>
<li>3바이트(24비트) 데이터를 6비트씩 4개로 나누어 표현함</li>
</ul>
</li>
</ul>
<hr />
<h2 id="3-문제-해결-과정-파이썬-스크립트">3. 문제 해결 과정 (파이썬 스크립트)</h2>
<ol>
<li>문제에 들어가서 해당 html의 페이지 소스를 확인하였다.<pre><code class="language-python">&lt;!doctype html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;title&gt;Welcome&lt;/title&gt;
&lt;/head&gt;
</code></pre>
</li>
</ol>

  <h1>Welcome! 👋</h1>
  <form method="POST">
    <input name="64se64_encoding" type="hidden" value="IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwphc2M9WzY4LCA3MiwgMTIzLCA5OCwgMTAxLCA0OCwgNTIsIDU0LCA5OCwgNTUsIDUzLCA1MCwgNTAsIDk3LCA5NywgNTAsIDEwMSwgNTAsIDU2LCAxMDIsIDUwLCA1NSwgNTQsIDEwMSwgNDgsIDk5LCA1NywgNDksIDQ4LCA1MywgNTAsIDQ5LCAxMDIsIDUwLCA1MSwgOTcsIDQ4LCA1MywgNTYsIDU1LCA0OCwgNDgsIDUzLCA5NywgNTYsIDUxLCA1NSwgNTUsIDUxLCA1NSwgNDgsIDk3LCA0OSwgNDksIDEwMSwgNTMsIDEwMSwgNTIsIDEwMCwgOTksIDQ5LCA1MywgMTAyLCA5OCwgNTAsIDk3LCA5OCwgMTI1XQphcnI9WzAgZm9yIGkgaW4gcmFuZ2UoNjgpXQpmb3IgaSBpbiByYW5nZSgwLDY4KToKICAgIGFycltpXT1jaHIoYXNjW2ldKQpmbGFnPScnLmpvaW4oYXJyKQpwcmludChmbGFnKQ==" />
  </form>


```

<p>해당 코드에서 64se64_encoding에 해당하는 value를 찾았다.</p>
<ol start="2">
<li><p>손으로 일일이 디코딩하는 것은 불가능하므로, <a href="https://www.base64decode.org/ko/">https://www.base64decode.org/ko/</a> 해당 도구를 이용하여 디코딩 하였다</p>
<pre><code class="language-python">#!/usr/bin/env python3
asc=[68, 72, 123, 98, 101, 48, 52, 54, 98, 55, 53, 50, 50, 97, 97, 50, 101, 50, 56, 102, 50, 55, 54, 101, 48, 99, 57, 49, 48, 53, 50, 49, 102, 50, 51, 97, 48, 53, 56, 55, 48, 48, 53, 97, 56, 51, 55, 55, 51, 55, 48, 97, 49, 49, 101, 53, 101, 52, 100, 99, 49, 53, 102, 98, 50, 97, 98, 125]
arr=[0 for i in range(68)]
for i in range(0,68):
 arr[i]=chr(asc[i])
flag=''.join(arr)
print(flag)</code></pre>
</li>
<li><p>나온 해당 값을 vscode에서 실행시키고, 문제의 정답을 찾았다.</p>
</li>
</ol>
<hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<p>디코딩을 통해 얻은 파이썬 코드의 동작 원리는 다음과 같다.</p>
<ol>
<li><strong>ASCII 코드 배열 (<code>asc</code>):</strong> <ul>
<li>총 68개의 정수로 이루어진 리스트로, 각 숫자는 문자(Char)의 ASCII 코드값을 의미한다.</li>
<li>첫 부분인 <code>[68, 72, 123]</code>은 각각 <code>'D'</code>, <code>'H'</code>, <code>'{'</code>에 대응되어 플래그 포맷인 <code>DH{</code>로 시작함을 알 수 있다.</li>
</ul>
</li>
<li><strong>문자열 복원 (<code>chr()</code> 및 <code>join()</code>):</strong><ul>
<li><code>chr()</code> 함수를 통해 ASCII 정수값을 문자로 변환한 뒤, <code>arr</code> 리스트에 저장한다.</li>
<li><code>''.join(arr)</code>를 수행하여 파편화된 문자들을 하나의 완전한 FLAG 문자열로 결합한다.</li>
</ul>
</li>
</ol>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>웹 소스코드 추적 능력:</strong> 문제 페이지의 겉면만 보는 것이 아니라, HTML 소스코드 내 숨겨진 <code>input type=&quot;hidden&quot;</code> 태그의 데이터를 확인하는 접근 방식을 익혔다.</li>
<li><strong>Base64 및 ASCII 인코딩 구조 이해:</strong> 인코딩된 데이터를 Base64로 1차 해독하고, 내부의 ASCII 코드 배열을 파이썬 스크립트로 2차 해독하는 과정을 거치며 데이터 변환의 밑바닥 흐름을 직접 체득했다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/383b81c5-274b-4aa4-926a-b2351b235a82/image.jpg" /><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/d5daf81d-28a7-4af2-a9ca-67d2a47731e0/image.jpg" />
<img alt="" src="https://velog.velcdn.com/images/huijeong211/post/95b676b3-d7e9-45cf-aa53-a4be8f722e7f/image.jpg" /></p>