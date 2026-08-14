<p>학습일: 2026.08.13
링크: <a href="https://learn.dreamhack.io/455#2">https://learn.dreamhack.io/455#2</a>
Dream Biginner - 드림핵의 주요 학습 카테고리 소개 - Cryptography - 강의 수강에 필요한 사전 지식</p>
<h4 id="python으로-작성된-간단한-소스코드">python으로 작성된 간단한 소스코드</h4>
<pre><code>import random


def bit_quiz1():
    print(&quot;bit operation quiz1&quot;)
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    print(f&quot;{a = }&quot;)
    print(f&quot;{b = }&quot;)

    if int(input(&quot;a ^ b = &quot;)) != a ^ b:
        exit(&quot;Wrong!&quot;)
    if int(input(&quot;a &amp; b = &quot;)) != a &amp; b:
        exit(&quot;Wrong!&quot;)
    if int(input(&quot;a | b = &quot;)) != a | b:
        exit(&quot;Wrong!&quot;)

    print(&quot;Good Job!&quot;)


def bit_quiz2():
    print(&quot;bit operation quiz2&quot;)
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    target = a * 256 + b
    i = int(input())
    if (a &lt;&lt; i) ^ b != target:
        exit(&quot;Wrong!&quot;)

    print(&quot;Good Job!&quot;)


def modulo_quiz1():
    print(&quot;modulo quiz1&quot;)
    p = 0x10001
    a = random.randint(1, p)
    b = random.randint(1, p)
    print(f&quot;{a = }&quot;)
    print(f&quot;{b = }&quot;)

    if int(input(&quot;a + b = ? (mod p) &gt; &quot;)) != (a + b) % p:
        exit(&quot;Wrong!&quot;)
    if int(input(&quot;a - b = ? (mod p) &gt; &quot;)) != (a - b) % p:
        exit(&quot;Wrong!&quot;)
    if int(input(&quot;a * b = ? (mod p) &gt; &quot;)) != (a * b) % p:
        exit(&quot;Wrong!&quot;)

    print(&quot;Good Job!&quot;)


def modulo_quiz2():
    print(&quot;modulo quiz2&quot;)
    p = 15260339158265275051  # 64bit prime
    a = random.randint(1, p)
    b = random.randint(1, p)
    print(f&quot;{a = }&quot;)
    print(f&quot;{b = }&quot;)

    d = int(input(&quot;a / b = ? (mod p) &gt; &quot;))
    if (d * b - a) % p != 0:
        exit(&quot;Wrong!&quot;)

    print(&quot;Good Job!&quot;)


def modulo_quiz3():
    print(&quot;modulo quiz3&quot;)
    p = 15260339158265275051  # 64bit prime
    a = random.randint(1, p)
    b = random.randint(1, p)
    print(f&quot;{a = }&quot;)
    print(f&quot;{b = }&quot;)

    if int(input(&quot;a**b = ? (mod p) &gt; &quot;)) != pow(a, b, p):
        exit(&quot;Wrong!&quot;)

    print(&quot;Good Job!&quot;)


if __name__ == &quot;__main__&quot;:
    bit_quiz1()
    bit_quiz2()
    modulo_quiz1()
    modulo_quiz2()
    modulo_quiz3()

    flag = open(&quot;flag&quot;, &quot;rb&quot;).read()
    print(flag)</code></pre><ol>
<li><p>파이썬 코드를 보고, 프로그램이 어떤 흐름으로 실행될 지 예상할 수 있다.
bit_quiz1()
 ↓
bit_quiz2()
 ↓
modulo_quiz1()
 ↓
modulo_quiz2()
 ↓
modulo_quiz3()
 ↓
flag 파일 읽기
 ↓
flag 출력</p>
</li>
<li><p>비트 연산 중 AND, OR, XOR이 어떤 연산인지 설명할 수 있고, bit_quiz1을 풀 수 있다.
AND &amp; : 두 비트가 둘 다 1일 때만 1임.
OR | : 두 비트 중 하나라도 1이면 1임.
XOR ^ : 두 비트가 서로 다르면 1임.</p>
</li>
</ol>
<p>bit_quiz1 풀이:
문제에서 
a = random.randint(0, 255)
b = random.randint(0, 255)
로 랜덤한 값을 생성함.
예를 들어
a = 13 = 00001101
b = 10 = 00001010</p>
<p>XOR
00001101
00001010
→ 00000111 = 7</p>
<p>AND
00001101
00001010
→ 00001000 = 8</p>
<p>OR
00001101
00001010
→ 00001111 = 15</p>
<ol start="3">
<li>SHIFT 연산을 할때 숫자의 비트들이 어떻게 바뀌는지 설명할 수 있고, bit_quiz1을 풀 수 있다.
Shift는 비트들을 왼쪽 또는 오른쪽으로 이동시키는 연산임.
a &lt;&lt; i : 비트를 왼쪽으로 i칸 이동시킴. 오른쪽에서 0이 채워짐.
a &gt;&gt; i: 비트를 오른쪽으로 i칸 이동시킴.</li>
</ol>
<p>드림핵 해당 링크: <a href="https://learn.dreamhack.io/440#7">https://learn.dreamhack.io/440#7</a></p>
<ol start="4">
<li><p>모듈로 연산이 무엇인지 설명할 수 있다.
모듈로 연산은 나눗셈의 나머지를 구하는 연산임. a mod p</p>
</li>
<li><p>모듈로 연산에서 덧셈, 뺄셈, 곱셈이 어떻게 이뤄지는지 설명할 수 있고, modulo_quiz1을 풀 수 있다.
모듈러 연산에서는 계산한 뒤 p로 나눈 나머지를 취하면 됨.</p>
</li>
</ol>
<p>덧셈: (a + b) mod p
뺄셈: (a - b) mod p
곱셈: (a × b) mod p
modulo_quiz1: p = 0x10001, 0x10001 = 65537.
해당 값을 
(a + b) % 65537
(a - b) % 65537
(a × b) % 65537</p>
<ol start="6">
<li><p>모듈로 연산에서 곱셈 역원이 무엇이고, 나눗셈이 어떻게 이뤄지는지 설명할 수 있다.
모듈러 연산에서는 일반적인 나눗셈을 직접 하지 않음.
대신 곱셈 역원(multiplicative inverse)을 이용함.
b의 modulo p에 대한 역원 b⁻¹은 b × b⁻¹ ≡ 1 (mod p)</p>
</li>
<li><p>modulo_quiz2을 풀 수 있다
해당 코드는 </p>
<pre><code>d = int(input())
</code></pre></li>
</ol>
<p>if (d * b - a) % p != 0:
    exit(&quot;Wrong!&quot;)</p>
<pre><code>수학적으로 바꾸면 d × b - a ≡ 0 (mod p)
d × b ≡ a (mod p)
d ≡ a × b⁻¹ (mod p)
즉, pow(b, -1, p)
d = (a * pow(b, -1, p)) % p

8. 모듈로 연산에서 거듭제곱이 어떻게 이뤄지는지 설명할 수 있다.
모듈러의 거듭제곱은 a^b mod p을 계산하는 것.
중요한 것은 매번 계산 결과에 mod를 적용해도 최종 결과가 동일하다는 것임.
(a × b) mod p를 계산할 때 중간 결과가 너무 커지지 않도록 계속 % p를 적용할 수 있음.

9. 이때 지수가 매우 클 경우, 어떻게 거듭제곱을 빠르게 계산할 수 있는지 설명할 수 있고, modulo_quiz3을 풀 수 있다.

지수가 너무 크면 비효율적이다. (a를 b번 곱하면 시간복잡도: O(b))
이때 빠른 거듭제곱(Binary Exponentiation / Square-and-Multiply)을 사용함.
핵심은 지수를 이진수로 표현하는 것임.
예시)
13 = 1101₂

a^13
= a^(8+4+1)
= a^8 × a^4 × a

a
a²
a⁴
a⁸
a¹⁶
... 이 각 단계에서 %p 를 적용함.

예시)
result = 1
base = a

지수의 각 비트를 확인

비트가 1이면
    result = result × base mod p

base = base × base mod p

시간복잡도 O(log b)

modulo_quiz3 풀이
코드에서
if int(input()) != pow(a, b, p):
라고 되어있는데 pow(a, b, p) 는 a^b mod p를 효율적인 모듈러 거듭제곱 방식으로 계산해줌.
따라서 문제에서 출력된 a, b와 주어진 p를 이용해서 pow(a, b, p)를 계산한 값을 입력하면 됨.

![](https://velog.velcdn.com/images/huijeong211/post/eff55364-6492-4730-ab33-c640cadd13a9/image.jpg)</code></pre>