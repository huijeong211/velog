<p>학습일: 2026.08.13
링크:<a href="https://learn.dreamhack.io/450#2">https://learn.dreamhack.io/450#2</a>
Dream Biginner - 드림핵의 주요 학습 카테고리 소개 - System Hacking - 강의 수강에 필요한 사전 지식</p>
<h4 id="c-언어로-작성된-간단한-소스코드">C 언어로 작성된 간단한 소스코드</h4>
<pre><code>#include &lt;stdio.h&gt;

void fun (int x, int y)
{
    int z;    
    char buf[100];

    z = x;
    read (0, buf, y);

    printf (&quot;x is %d\n&quot;, x);
    //printf (“z is %d\n”, z);
}

int main (int argc, char* argv[])
{
    int a, b;
    a = 30;
    b = 300;

    fun (a,b);
}</code></pre><ol>
<li>위 코드가 실행 되었을 때, 프로그램이 어떻게 동작할지 예상할 수 있다.</li>
</ol>
<ul>
<li>main()에서 a=30, b=300을 설정하고 fun(30,300)을 호출함.
 fun()에서는 z=x를 수행한 후 read()를 통해 최대 300바이트를 buf에 입력하고 x를 출력함.
 buf는 100바이트이므로 100바이트를 초과하는 입력에서 Stack Buffer Overflow가 발생할 수 있음.</li>
</ul>
<ol start="2">
<li>함수 호출 규약(Calling Convention)이 무엇인지 설명할 수 있다</li>
</ol>
<ul>
<li>Calling Convention은 함수 호출 시 인자 전달, 반환값 전달, 레지스터 보존, Stack 관리 등의 방법을 정의한 규칙임.</li>
</ul>
<ol start="3">
<li>스택 프레임(Stack Frame)이 무엇인지 설명할 수 있다.</li>
</ol>
<ul>
<li>Stack Frame은 함수 실행에 필요한 지역 변수, 저장된 레지스터, 반환 주소 등의 정보를 포함하는 Stack 영역임.</li>
</ul>
<ol start="4">
<li>Register가 무엇인지 설명할 수 있으며, C 코드가 진행됨에 따라 레지스터 값들이 어떻게 변할지 유추할 수 있다.</li>
</ol>
<ul>
<li>Register는 CPU 내부의 고속 저장공간임.
 64-bit System V ABI에서는 함수의 첫 번째와 두 번째 정수 인자가
 각각 RDI와 RSI 등을 통해 전달됨.</li>
</ul>
<ol start="5">
<li>시작 지점부터 종료 시점까지 main()의 Stack의 변화를 설명할 수 있다.</li>
</ol>
<ul>
<li>main()이 시작되면 main의 Stack Frame이 생성되고 a와 b가 저장됨.
 fun() 호출 시 fun의 Stack Frame이 추가됨.
 fun()이 종료되면 해당 Frame이 제거되고 main으로 돌아오며,
 main 종료 후 프로그램이 종료됨.</li>
</ul>
<ol start="6">
<li>32-bit 프로그램일 때와 64-bit 프로그램일 때 Stack 값들의 차이점을 설명할 수 있다.</li>
</ol>
<ul>
<li>32-bit에서는 포인터와 Return Address가 일반적으로 4바이트이고
 함수 인자가 Stack을 통해 전달되는 경우가 많음.
 64-bit에서는 포인터와 Return Address가 일반적으로 8바이트이고 함수 인자의 일부가 Register를 통해 전달됨.</li>
</ul>
<ol start="7">
<li>fun()의 취약한 부분이 무엇인지 찾을 수 있다.</li>
</ol>
<ul>
<li>char buf[100]에 대해 read(0, buf, y)를 수행하는데
 y=300이므로 최대 300바이트를 입력받을 수 있다는 것이 취약점임.
 즉 100바이트를 초과하는 입력에 의해 Stack Buffer Overflow가 발생함.</li>
</ul>
<ol start="8">
<li>fun()의 취약점으로 인해 32-bit와 64-bit환경에서 x의 출력값이 어떻게 달라지는지 설명할 수 있다.</li>
</ol>
<ul>
<li>32-bit에서는 함수 인자가 Stack에 존재할 가능성이 높아 overflow에 의해 x가 덮어써질 가능성이 있음.
64-bit에서는 x가 Register를 통해 전달되므로 동일한 overflow가 x에 영향을 주는 방식이 달라짐.
정확한 출력값은 컴파일러와 컴파일 옵션에 따라 달라짐.</li>
</ul>
<ol start="9">
<li>x가 아닌 z를 출력하는 경우, 32-bit와 64-bit환경에서 z의 출력값이 어떻게 달라지는지 설명할 수 있다.</li>
</ol>
<ul>
<li>z는 read()보다 먼저 x의 값을 복사함.
 따라서 overflow가 z가 저장된 영역을 덮으면 z도 변경될 수 있고, 그렇지 않으면 z는 30을 유지함.
 32-bit와 64-bit에서 Stack 배치가 다르므로 결과도 달라질 수 있음.</li>
</ul>
<ol start="10">
<li>Figure 1을 컴파일한 바이너리가 주어졌을 때, 이를 익스플로잇하며 셸(Shell)을 획득하는 공격코드를 작성할 수 있다.</li>
</ol>
<ul>
<li>buf에 100바이트보다 많은 데이터를 입력하여 Stack의 제어 데이터를 덮어쓰고 함수 반환 시 실행 흐름을 변경하는 것이 기본적인 공격 원리임.
  실제 성공 여부는 Return Address 위치, Stack Canary, NX, ASLR, PIE 등의 보호기법과 바이너리 구조에 따라 결정됨.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/huijeong211/post/f33a3475-c5f5-42cf-bdc2-ba5980afaec7/image.jpg" /></p>