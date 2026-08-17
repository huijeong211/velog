<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li><p>학습일: 2026.08.16</p>
</li>
<li><p>문제명: Exercise: SSH</p>
</li>
<li><p>링크: <a href="https://dreamhack.io/wargame/challenges/875">https://dreamhack.io/wargame/challenges/875</a></p>
</li>
<li><p>핵심 키워드: SSH, OpenSSH, rbash (Restricted Bash), Shell Environment</p>
</li>
</ul>
<hr />
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>제공된 문제 서버 정보(host3.dreamhack.games:12306)를 확인하고 SSH를 통해 서버에 접근하는 과정과 초기 셸 환경을 분석하였다.</p>
<p><strong>C 언어 기초 동작 분석:</strong></p>
<p>nc 명령어를 통해 해당 포트가 OpenSSH(8.9p1) 서비스로 포워딩(12306/tcp → 31337/tcp)되어 있음을 확인했다.</p>
<p>SSH 클라이언트를 사용하여 chall 계정으로 서버에 접속했다.</p>
<p>접속 성공 후 rbash: command not found 메세지를 통해 현재 할당된 셸이 rbash(Restricted Bash)임을 확인했다.</p>
<hr />
<h2 id="3-문제-해결-과정-터미널-실습">3. 문제 해결 과정 (터미널 실습)</h2>
<p>nc 명령어로 대상 포트의 서비스 정보를 확인하였다.</p>
<p>```user@user-VirtualBox:~$ nc host3.dreamhack.games 12306
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
Host: host3.dreamhack.games
Port: 12306/tcp → 31337/tcp</p>
<pre><code>
SSH 명령어와 지정된 포트 옵션(-p)을 사용하여 원격 서버에 접속을 시도했다.
또 이전에 배운 cat 명령어를 사용해서 파일의 내용을 화면에 출력했다.</code></pre><p>  user@user-VirtualBox:~$ ssh <a href="mailto:chall@host3.dreamhack.games">chall@host3.dreamhack.games</a> -p 12306
<a href="mailto:chall@host3.dreamhack.games">chall@host3.dreamhack.games</a>'s password: 
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 4.19.234 x86_64)</p>
<ul>
<li>Documentation:  <a href="https://help.ubuntu.com">https://help.ubuntu.com</a></li>
<li>Management:     <a href="https://landscape.canonical.com">https://landscape.canonical.com</a></li>
<li>Support:        <a href="https://ubuntu.com/advantage">https://ubuntu.com/advantage</a></li>
</ul>
<p>This system has been minimized by removing packages and content that are
not required on a system that users do not log into.</p>
<p>To restore this content, you can run the 'unminimize' command.
Last login: Sun Aug 16 11:45:52 2026 from 39.121.198.114
rbash: groups: command not found
rbash: dircolors: command not found
chall@localhost:~$ cat flag
DH{h3110_6e9inn3rs!}</p>
<pre><code>
*주의
리눅스 터미널의 기본 보안 정책(Password Echoing Off)으로 인해 비밀번호 입력 시 화면에 아무 글자나 커서 이동이 표시되지 않는다. 이는 정상 작동이므로 문제에서 주어진 비밀번호를 입력 후 Enter를 누르면 접속된다.

---

## 4. 문제 풀이 및 코드 분석 (Line-by-Line)

소스코드의 주요 동작 원리는 다음과 같다.

1. **SSH 원격 접속 (ssh chall@host3.dreamhack.games -p 12306):** 
   * SSH 기본 포트(22번)가 아닌 문제용으로 개설된 12306 포트를 통해 원격 서버의 chall 계정으로 인증을 요청한다.

2. **rbash 제한 환경 진입:**
   * 로그인 완료 후 .bashrc 또는 프로필 실행 과정에서 기본 시스템 명령어(groups, dircolors 등)를 찾지 못하고 command not found 에러가 발생한다.
   * 이는 사용자의 셸이 rbash(Restricted Bash)로 설정되어 있어 $PATH 환경 변수 및 실행 가능한 명령어의 범위가 엄격히 제한되어 있음을 의미한다.



---

## 5. 배운 점 및 회고
* **SSH 접속 및 옵션 활용:** 비표준 포트를 사용하여 원격 접속할 때 -p 옵션을 지정하는 표준 명령 형식을 익혔다.
* **터미널 보안 동작 이해:** 리눅스 환경에서 비밀번호 입력 시 글자가 비표시되는 보안 특성을 파악하여 입력을 진행했다.
* **Restricted Shell (rbash) 개념 체득:** 로그인 직후 초기화 에러 메세지를 통해 현재 셸이 제한된 환경임을 인지하고, 일반적인 Bash 환경과의 차이점(경로 이동 제한, 특정 명령어 제한 등)을 파악하는 계기가 되었다.

![](https://velog.velcdn.com/images/huijeong211/post/06a8b6ec-a473-4877-9a47-424f0b1bc7f5/image.jpg)</code></pre>