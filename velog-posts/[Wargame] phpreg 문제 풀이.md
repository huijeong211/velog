<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.30</li>
<li>문제명: phpreg</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/873">https://dreamhack.io/wargame/challenges/873</a></li>
<li>핵심 키워드: PHP preg_replace, Regex Filter Bypass, OS Command Injection</li>
</ul>
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제공된 문제 파일 step2.php를 확인해보면, 사용자로부터 $input_name과 $input_pw를 받아 PHP의 preg_replace 함수를 통해 필터링을 수행한다.</p>
<p><strong>문제 파일 일부</strong></p>
<pre><code>// pw filtering
if (preg_match(&quot;/[a-zA-Z]/&quot;, $input_pw)) {
    echo &quot;alphabet in the pw :(&quot;;
}
else {
    $name = preg_replace(&quot;/nyang/i&quot;, &quot;&quot;, $input_name);
    $pw = preg_replace(&quot;/\d*\@\d{2,3}(31)+[^0-8\&quot;]\!/&quot;, &quot;d4y0r50ng&quot;, $input_pw); 

    if ($name === &quot;dnyang0310&quot; &amp;&amp; $pw === &quot;d4y0r50ng+1+13&quot;) {
        echo '&lt;h4&gt;Step 2 : Almost done...&lt;/h4&gt;...';
        // Command Injection 폼 출력 로직 (생략)
    }
}
</code></pre><p>처음에는 정규표현식 /nyang/i를 패턴 nyang을 대소문자 구분 없이 찾으라는 의미라고 읽고 id에 nyang를 입력했다.
비밀번호도 <code>/\d*\@\d{2,3}(31)+[^0-8\&quot;]\!/</code>를 해석해서 0@11319! 를 비밀번호 자리에 넣어봤더니 에러가 나왔다. 분석을 통해 입력값이 최종적으로 어떤 문자열로 치환되어야 하는지, 그리고 금지된 알파벳 조건을 어떻게 우회할 수 있는지 확인했다.</p>
<hr />
<h2 id="3-문제-해결-과정-웹-실습">3. 문제 해결 과정 (웹 실습)</h2>
<p>조건을 통과하기 위해 두 가지 입력값을 고려했다.</p>
<p><strong>1. $input_name 페이로드 제작 (단순 치환 우회)</strong>
목표값은 dnyang0310인데, 서버는 nyang이라는 문자열을 찾아 삭제(&quot;&quot;)해 버린다.
이를 우회하기 위해 지워질 부분을 예상하고 겹쳐 적었다.</p>
<ul>
<li><p>입력값: dnynyangang0310</p>
</li>
<li><p>동작: 중간의 nyang이 정규식에 의해 삭제되고, 남은 dny와 ang0310이 결합하여 최종적으로 dnyang0310이 완성된다.</p>
</li>
</ul>
<p><strong>2. $input_pw 페이로드 제작 (알파벳 필터링 우회)</strong>
서버는 preg_match(&quot;/[a-zA-Z]/&quot;, $input_pw)를 통해 입력값에 알파벳이 단 한 글자라도 들어가면 차단한다. 그런데 우리가 최종적으로 만들어야 하는 목표값은 d4y0r50ng+1+13으로 알파벳이 포함되어 있다.
여기서 핵심은 &quot;알파벳(d4y0r50ng)은 내가 입력하는 게 아니라, 서버가 정규식 매칭 후 알아서 치환해 준다&quot;는 점이다.
따라서 알파벳이 전혀 없는 정규식 매칭 문자열을 만들고, 그 뒤에 +1+13을 덧붙이면 된다.</p>
<ul>
<li><p>입력값: 1@123319!+1+13</p>
</li>
<li><p>동작: 입력값에는 알파벳이 없으므로 필터링을 통과한다. 이후 앞부분 1@123319!가 정규식에 매칭되어 d4y0r50ng로 치환되고, 뒤의 +1+13과 합쳐져 최종적으로 d4y0r50ng+1+13이 완성된다.</p>
</li>
</ul>
<p><strong>3. Command Injection (플래그 획득)</strong>
Step 1을 통과하면 cmd 폼이 열린다. 소스코드상에 플래그 파일의 정확한 위치가 명시되어 있지 않았기 때문에, 리눅스 명령어를 통해 디렉터리 구조를 확인해야 했다.</p>
<p>1) ls -al : 현재 디렉터리 확인</p>
<p>2) ls ../ : 상위 디렉터리 확인 -&gt; dream 이라는 수상한 디렉터리 발견</p>
<p>3) ls ../dream : 내부 확인 -&gt; flag.txt 또는 유사한 이름의 파일 확인</p>
<p>4) 최종적으로 cat ../dream/fla*.txt (와일드카드 사용) 명령어를 입력하여 플래그(DH{ad866c64dabaf30136e22d3de2980d24c4da617b9d706f81d10a1bc97d0ab6f6})를 획득했다.</p>
<hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<table>
<thead>
<tr>
<th>로직(코드)</th>
<th>역할 및 취약점 분석</th>
</tr>
</thead>
<tbody><tr>
<td><code>if (preg_match(&quot;/[a-zA-Z]/&quot;, $input_pw))</code></td>
<td><code>사용자의 입력값($input_pw)에 알파벳 대/소문자가 존재하는지 검사한다. 존재하면 예외 처리로 빠져버린다. 방화벽(WAF)의 입력값 검증 역할을 한다.</code></td>
</tr>
<tr>
<td><code>$name = preg_replace(&quot;/nyang/i&quot;, &quot;&quot;, $input_name);</code></td>
<td><code>/i 플래그로 인해 대소문자 구분 없이 nyang을 찾아 빈 문자열로 지운다. 단 1회(또는 발견된 모든 패턴을 1회씩만) 지우기 때문에 중첩된 문자열(nynyangang)에 대한 재검증 로직이 없어 우회가 가능하다.</code></td>
</tr>
<tr>
<td><code>$pw = preg_replace(&quot;/\d*\@\d{2,3}(31)+[^0-8\&quot;]\!/&quot;, &quot;d4y0r50ng&quot;, $input_pw);</code></td>
<td><code>특정 패턴을 강제로 d4y0r50ng으로 바꾼다. 정규식 구성은 숫자 0개 이상(\d*), @ 기호(\@), 숫자 2~3개(\d{2,3}), 31 1번 이상 반복((31)+), 0~8 및 &quot;가 아닌 문자 1개([^0-8\&quot;]), 느낌표(\!)로 이루어져 있다.</code></td>
</tr>
<tr>
<td><code>$cmd = $_POST[&quot;cmd&quot;]</code></td>
<td><code>Step 2 폼에서 넘겨받은 cmd 값을 저장한다. 코드에는 생략되었으나 내부적으로 system($cmd)나 shell_exec($cmd)를 호출했을 것이다. 사용자 입력을 필터링 없이 셸로 바로 넘겼기 때문에 OS Command Injection 취약점이 발생했다.</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>단순 치환(Replace) 기반 필터링의 한계:</strong> 이번 문제의 ID 검증 로직처럼 WAF나 서버 애플리케이션에서 특정 악성 키워드(예: admin, script 등)를 한 번만 지우는 로직은 매우 위험하다. 공격자가 adadminmin처럼 필터링 단어를 겹쳐 쓰면 삭제 후 완전한 공격 페이로드가 재조립되는 우회 기법이 가능함을 확인했다. 인프라 보안 관점에서 입력값을 검증할 때는 단순 삭제가 아니라 반복 검사(Recursive)를 하거나 아예 요청 자체를 차단(Block)하는 방식이 안전하다.</li>
<li><strong>OS Command Injection의 위험성:</strong> 웹 애플리케이션에서 사용자 입력값을 시스템 명령어로 직접 넘기는 구조가 얼마나 치명적인지 실감했다. 서버를 구축할 때는 유저 입력값이 셸 명령어 인터프리터로 넘어가지 않도록 철저한 이스케이프 처리가 필요하며, 컨테이너 환경에서는 실행 권한을 최소화하는 조치(Principle of Least Privilege)가 반드시 동반되어야 한다.</li>
</ul>