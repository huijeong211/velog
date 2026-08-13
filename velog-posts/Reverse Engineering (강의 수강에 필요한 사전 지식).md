<p>학습일: 2026.08.12
링크:<a href="https://learn.dreamhack.io/452#2">https://learn.dreamhack.io/452#2</a>
Dream Biginner - 컴퓨터 과학 기초 - Reverse Engineering - 강의 수강에 필요한 사전 지식</p>
<h4 id="c-언어로-작성된-간단한-소스코드">C 언어로 작성된 간단한 소스코드</h4>
<pre><code>#include &lt;stdio.h&gt;

int enc[17] = {75, 104, 111, 111, 114, 35, 71, 117, 104, 100, 112, 107, 100, 102, 110, 36, 3};

int main(){

    int key = 0;
    int dec[17];

    for(int i=0; i&lt;17; i++){
        printf(&quot;%c&quot;, enc[i]);
    }

    printf(&quot;\nYour input: &quot;);
    scanf(&quot;%d&quot;, &amp;key);

    for(int i=0; i&lt;17; i++){
        dec[i] = enc[i] - key;
        printf(&quot;%c&quot;, dec[i]);
    }
    printf(&quot;\n&quot;);

    return 0;
}</code></pre><h4 id="해당-소스코드의-실행파일을-disassemble한-어셈블리-코드">해당 소스코드의 실행파일을 disassemble한 어셈블리 코드</h4>
<pre><code>Dump of assembler code for function main:
   0x00005555555551a9 &lt;+0&gt;:     endbr64 
   0x00005555555551ad &lt;+4&gt;:     push   rbp
   0x00005555555551ae &lt;+5&gt;:     mov    rbp,rsp
   0x00005555555551b1 &lt;+8&gt;:     sub    rsp,0x60
   0x00005555555551b5 &lt;+12&gt;:    mov    rax,QWORD PTR fs:0x28
   0x00005555555551be &lt;+21&gt;:    mov    QWORD PTR [rbp-0x8],rax
   0x00005555555551c2 &lt;+25&gt;:    xor    eax,eax
   0x00005555555551c4 &lt;+27&gt;:    mov    DWORD PTR [rbp-0x5c],0x0
   0x00005555555551cb &lt;+34&gt;:    mov    DWORD PTR [rbp-0x58],0x0
   0x00005555555551d2 &lt;+41&gt;:    jmp    0x5555555551f6 &lt;main+77&gt;
   0x00005555555551d4 &lt;+43&gt;:    mov    eax,DWORD PTR [rbp-0x58]
   0x00005555555551d7 &lt;+46&gt;:    cdqe   
   0x00005555555551d9 &lt;+48&gt;:    lea    rdx,[rax*4+0x0]
   0x00005555555551e1 &lt;+56&gt;:    lea    rax,[rip+0x2e38]        # 0x555555558020 &lt;enc&gt;
   0x00005555555551e8 &lt;+63&gt;:    mov    eax,DWORD PTR [rdx+rax*1]
   0x00005555555551eb &lt;+66&gt;:    mov    edi,eax
   0x00005555555551ed &lt;+68&gt;:    call   0x555555555080 &lt;putchar@plt&gt;
   0x00005555555551f2 &lt;+73&gt;:    add    DWORD PTR [rbp-0x58],0x1
   0x00005555555551f6 &lt;+77&gt;:    cmp    DWORD PTR [rbp-0x58],0x10
   0x00005555555551fa &lt;+81&gt;:    jle    0x5555555551d4 &lt;main+43&gt;
   0x00005555555551fc &lt;+83&gt;:    lea    rax,[rip+0xe01]        # 0x555555556004
   0x0000555555555203 &lt;+90&gt;:    mov    rdi,rax
   0x0000555555555206 &lt;+93&gt;:    mov    eax,0x0
   0x000055555555520b &lt;+98&gt;:    call   0x5555555550a0 &lt;printf@plt&gt;
   0x0000555555555210 &lt;+103&gt;:   lea    rax,[rbp-0x5c]
   0x0000555555555214 &lt;+107&gt;:   mov    rsi,rax
   0x0000555555555217 &lt;+110&gt;:   lea    rax,[rip+0xdf4]        # 0x555555556012
   0x000055555555521e &lt;+117&gt;:   mov    rdi,rax
   0x0000555555555221 &lt;+120&gt;:   mov    eax,0x0
   0x0000555555555226 &lt;+125&gt;:   call   0x5555555550b0 &lt;__isoc99_scanf@plt&gt;
   0x000055555555522b &lt;+130&gt;:   mov    DWORD PTR [rbp-0x54],0x0
   0x0000555555555232 &lt;+137&gt;:   jmp    0x55555555526f &lt;main+198&gt;
   0x0000555555555234 &lt;+139&gt;:   mov    eax,DWORD PTR [rbp-0x54]
   0x0000555555555237 &lt;+142&gt;:   cdqe   
   0x0000555555555239 &lt;+144&gt;:   lea    rdx,[rax*4+0x0]
   0x0000555555555241 &lt;+152&gt;:   lea    rax,[rip+0x2dd8]        # 0x555555558020 &lt;enc&gt;
   0x0000555555555248 &lt;+159&gt;:   mov    eax,DWORD PTR [rdx+rax*1]
   0x000055555555524b &lt;+162&gt;:   mov    ecx,DWORD PTR [rbp-0x5c]
   0x000055555555524e &lt;+165&gt;:   sub    eax,ecx
   0x0000555555555250 &lt;+167&gt;:   mov    edx,eax
   0x0000555555555252 &lt;+169&gt;:   mov    eax,DWORD PTR [rbp-0x54]
   0x0000555555555255 &lt;+172&gt;:   cdqe   
   0x0000555555555257 &lt;+174&gt;:   mov    DWORD PTR [rbp+rax*4-0x50],edx
   0x000055555555525b &lt;+178&gt;:   mov    eax,DWORD PTR [rbp-0x54]
   0x000055555555525e &lt;+181&gt;:   cdqe   
   0x0000555555555260 &lt;+183&gt;:   mov    eax,DWORD PTR [rbp+rax*4-0x50]
   0x0000555555555264 &lt;+187&gt;:   mov    edi,eax
   0x0000555555555266 &lt;+189&gt;:   call   0x555555555080 &lt;putchar@plt&gt;
   0x000055555555526b &lt;+194&gt;:   add    DWORD PTR [rbp-0x54],0x1
   0x000055555555526f &lt;+198&gt;:   cmp    DWORD PTR [rbp-0x54],0x10
   0x0000555555555273 &lt;+202&gt;:   jle    0x555555555234 &lt;main+139&gt;
   0x0000555555555275 &lt;+204&gt;:   mov    edi,0xa
   0x000055555555527a &lt;+209&gt;:   call   0x555555555080 &lt;putchar@plt&gt;
   0x000055555555527f &lt;+214&gt;:   mov    eax,0x0
   0x0000555555555284 &lt;+219&gt;:   mov    rdx,QWORD PTR [rbp-0x8]
   0x0000555555555288 &lt;+223&gt;:   sub    rdx,QWORD PTR fs:0x28
   0x0000555555555291 &lt;+232&gt;:   je     0x555555555298 &lt;main+239&gt;
   0x0000555555555293 &lt;+234&gt;:   call   0x555555555090 &lt;__stack_chk_fail@plt&gt;
   0x0000555555555298 &lt;+239&gt;:   leave  
   0x0000555555555299 &lt;+240&gt;:   ret    
End of assembler dump.</code></pre><ol>
<li>프로그램이 실행 되었을 때 프로그램이 어떠한 동작을 하는지 설명할 수 있다.</li>
</ol>
<ul>
<li>스택 영역에 카나리 값을 생성, enc 배열 요소를 문자 하나씩 출력. 사용자로부터 key 정수 값을 입력받아서 각 요소에서 key를 뺀 복호화 결과(dec)를 저장하며 출력한다. 개행 문자를 출력한 뒤 카나리를 검증하고 종료</li>
</ul>
<ol start="2">
<li>위 C언어 프로그램의 enc[17]와 key가 프로세스의 메모리에 배치될 때 각각 어떠한 메모리 세그먼트에 위치할지 대략적으로 설명할 수 있다.</li>
</ol>
<ul>
<li>enc[17]은 초깃값이 존재하는 전역 변수이기 때문. 데이터(.data) 세그먼트에 위치. key는 함수 내부의 지역 변수이기 때문. 스택(Stack) 세그먼트에 위치</li>
</ul>
<ol start="3">
<li>메모리와 레지스터의 차이를 설명할 수 있다</li>
</ol>
<ul>
<li>레지스터는 CPU 내부의 저장 공간. 용량이 매우 작으나 속도가 가장 빠르다. 메모리(RAM)는 CPU 외부의 저장 공간. 용량이 크나 접근 속도가 상대적으로 늦다</li>
</ul>
<ol start="4">
<li>명령어 집합 구조 (Instuction Set Archtecture, ISA) 가 무엇인지 설명할 수 있다.</li>
</ol>
<ul>
<li>CPU가 이해하는 기계어 명령어의 집합. 하드웨어와 소프트웨어 사이의 표준 약속.</li>
</ul>
<ol start="5">
<li>C언어 소스 코드가 어떠한 과정을 거쳐서 컴파일 되는지, 그리고 컴파일 과정에서 코드가 어떻게 바뀌는지 설명할 수 있다.</li>
</ol>
<ul>
<li>전처리(주석 제거 및 텍스트 정리) ➔ 컴파일(C 코드를 어셈블리로 변환) ➔ 어셈블(어셈블리를 기계어로 변환) ➔ 링킹(라이브러리와 결합하여 실행 파일 생성).</li>
</ul>
<ol start="6">
<li>c, 어셈블리, 바이너리 코드 각각의 특징과 그 차이점에 대해 설명할 수 있다.</li>
</ol>
<ul>
<li>C 언어는 사람이 이해하기 쉬운 고급 언어. 어셈블리는 CPU 명령어와 1:1 대응되는 저급 언어. 바이너리 코드는 CPU가 직접 실행하는 0과 1의 이진 데이터.</li>
</ul>
<ol start="7">
<li>어셈블리 코드를 보고 main()의 스택 프레임(Stack Frame) 구조를 파악할 수 있다.</li>
</ol>
<ul>
<li>main() 스택 프레임 구조
[rbp-0x08]: 스택 카나리.
[rbp-0x50]: dec 배열 시작 위치.
[rbp-0x54]: 복호화 루프 변수.
[rbp-0x58]: 출력 루프 변수.
[rbp-0x5c]: key 변수 저장 위치.</li>
</ul>
<ol start="8">
<li>어셈블리 코드를 보고 메모리와 레지스터를 구분할 수 있다</li>
</ol>
<ul>
<li>rax, rdi 등 표기만 있는 경우 레지스터. 대괄호 [...]로 감싸져 있거나 주소를 가리키면 메모리.</li>
</ul>
<ol start="9">
<li>어셈블리를 보고 동일한 기능을 하는 C 코드를 작성할 수 있다.<pre><code>#include &lt;stdio.h&gt;
</code></pre></li>
</ol>
<p>int enc[17] = {75, 104, 111, 111, 114, 35, 71, 117, 104, 100, 112, 107, 100, 102, 110, 36, 3};</p>
<p>int main() {
    int key = 0, i = 0, dec[17];
    for (i = 0; i &lt;= 16; i++) putchar(enc[i]);
    printf(&quot;Your input: &quot;);
    scanf(&quot;%d&quot;, &amp;key);
    for (i = 0; i &lt;= 16; i++) {
        dec[i] = enc[i] - key;
        putchar(dec[i]);
    }
    putchar('\n');
    return 0;
}</p>
<pre><code>
10. C 언어 소스 코드에서 int형 배열이 문자로 출력될 수 있는 이유를 설명할 수 있다.
 - 컴퓨터는 숫자와 문자를 모두 이진수로 저장하기 때문. putchar() 또는 %c 출력 시 해당 정수를 ASCII 코드에 대응되는 문자로 해석하기 때문.

11. 프로그램이 &quot;Hello dreamhack!&quot;을 출력하도록 하는 key 값을 구할 수 있다.
- 첫 글자 'K'(75)를 'H'(72)로 변환해야 하기 때문. $75 - 72 = 3$. 따라서 입력할 key 값은 3.

![](https://velog.velcdn.com/images/huijeong211/post/f4b553ba-a286-485d-94c7-1e64f1c23167/image.jpg)</code></pre>