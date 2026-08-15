<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.15</li>
<li>문제명: Exercise: Welcome-Beginners</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/812">https://dreamhack.io/wargame/challenges/812</a></li>
<li>핵심 키워드: C Language</li>
</ul>
<hr />
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제공된 C 언어 소스코드(chall.c)를 분석하여 프로그램의 실행 흐름과 플래그 출력 조건을 확인하였다.</p>
<p><strong>C 언어 기초 동작 분석:</strong></p>
<p>open(), read() 함수를 통해 서버 내 ./flag 파일의 내용을 읽어 메모리에 저장한다.</p>
<p>scanf(&quot;%9s&quot;, inp_str)를 사용하여 사용자로부터 문자열 입력을 받는다.</p>
<p>strcmp() 함수를 사용하여 입력받은 문자열과 기존 지정된 문자열(&quot;Dreamhack&quot;)을 비교한다.</p>
<p>문자열이 일치할 경우 메모리에 저장되어 있던 플래그를 화면에 출력한다.</p>
<hr />
<h2 id="3-문제-해결-과정-파이썬-스크립트">3. 문제 해결 과정 (파이썬 스크립트)</h2>
<p>문제에서 제공된 chall.c 소스코드:</p>
<pre><code class="language-//">// Compile Option: gcc chall.c -o chall -fno-stack-protector

#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;unistd.h&gt;
#include &lt;string.h&gt;

#define FLAG_SIZE 0x45

void init() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

int main(void) {
    int fd;
    char *flag;

    init();

    // read flag
    flag = (char *)malloc(FLAG_SIZE);
    fd = open(&quot;./flag&quot;, O_RDONLY);
    read(fd, flag, FLAG_SIZE);

    char cmp_str[10] = &quot;Dreamhack&quot;;
    char inp_str[10];   
    printf(&quot;Enter \&quot;Dreamhack\&quot; : &quot;);
    scanf(&quot;%9s&quot;, inp_str);

    if(strcmp(cmp_str, inp_str) == 0){
        puts(&quot;Welcome Beginners!&quot;);
        // print flag
        puts(flag);
    }

    return 0;
}</code></pre>
<ol>
<li><p>코드를 확인해보니 프로그램이 요구하는 문자열 Dreamhack을 그대로 입력하면 if(strcmp(cmp_str, inp_str) == 0) 조건문이 참이 되어 플래그가 출력되는 것을 파악할 수 있었다.</p>
</li>
<li><p>드림핵 문제 페이지에서 생성을 통해 얻은 접속 정보(nc host.dreamhack.games -port-)를 터미널에 입력하여 문제 서버에 접속하였다.</p>
</li>
<li><p>Enter &quot;Dreamhack&quot; : 안내 문구가 출력되었을 때 Dreamhack을 입력하여 플래그를 획득하였다.</p>
</li>
</ol>
<p><strong>리눅스 터미널에 입력한 값 및 결과</strong></p>
<pre><code>  user@user-VirtualBox:~$ nc host3.dreamhack.games port
Enter &quot;Dreamhack&quot; : Dreamhack
Welcome Beginners!
DH{d6398f06b35117877a855ade8d2015fc3b142c3ca6686ce3198e372b9ef8a644}</code></pre><hr />
<h2 id="4-문제-풀이-및-코드-분석-line-by-line">4. 문제 풀이 및 코드 분석 (Line-by-Line)</h2>
<p>소스코드의 주요 동작 원리는 다음과 같다.</p>
<ol>
<li><p><strong>플래그 로드 (open &amp; read):</strong> </p>
<ul>
<li>open(&quot;./flag&quot;, O_RDONLY)로 플래그 파일을 읽기 전용으로 열고, read() 함수를 사용하여 동적 할당된 flag 버퍼에 저장한다.</li>
</ul>
</li>
<li><p><strong>입력 및 비교 (scanf &amp; strcmp):</strong></p>
<ul>
<li>cmp_str에 &quot;Dreamhack&quot; 문자열을 미리 지정해 두고, scanf(&quot;%9s&quot;, inp_str)로 사용자 입력을 받는다.</li>
<li>strcmp(cmp_str, inp_str) 함수는 두 문자열이 일치할 때 0을 반환하므로, 정확히 Dreamhack을 입력해야 조건문 내부로 진입한다.</li>
</ul>
</li>
<li><p><strong>플래그 출력 (puts):</strong> </p>
<ul>
<li>조건식이 참이 되면 puts(flag)가 실행되어 메모리에 로드되어 있던 플래그 문자열이 표준 출력으로 렌더링된다.</li>
</ul>
</li>
</ol>
<hr />
<h2 id="5-배운-점-및-회고">5. 배운 점 및 회고</h2>
<ul>
<li><strong>C 언어 문자열 비교 함수 이해:</strong> strcmp() 함수의 동작 방식과 반환값(0일 때 일치)을 복습하고, 단순한 조건 비교 알고리즘의 구조를 파악했다.</li>
<li><strong>시스템 워게임 문제 해결 흐름 체득:</strong> 로컬 환경에서의 컴파일 및 셸 실행 방식과 원격 서버(nc) 접속을 통한 플래그 획득 과정의 차이를 이해하고 직접 적용해 보았다.</li>
</ul>
<p><img alt="업로드중.." src="blob:https://velog.io/1f26c835-7245-45af-85f7-fc1475346a83" /></p>