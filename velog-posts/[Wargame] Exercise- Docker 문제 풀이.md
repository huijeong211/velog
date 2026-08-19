<h2 id="1-문제-개요">1. 문제 개요</h2>
<ul>
<li>학습일: 2026.08.18</li>
<li>문제명: Exercise: Docker</li>
<li>링크: <a href="https://dreamhack.io/wargame/challenges/876">https://dreamhack.io/wargame/challenges/876</a></li>
<li>핵심 키워드: Docker, Dockerfile, docker build, docker run, Interactive Container Shell</li>
</ul>
<hr />
<h2 id="2-문제-분석">2. 문제 분석</h2>
<p>주어진 Dockerfile 분석을 통해 문제 서버의 가상 환경 구축 방식과 권한 설정 상태를 확인했다.</p>
<p>해당 문제는 플래그를 찾는 것이 목표가 아니라 Dockerfile로 직접 이미지를 빌드하고, 컨테이너를 실행해 보기 위한 문제이다.</p>
<hr />
<h2 id="3-문제-해결-과정-터미널-실습">3. 문제 해결 과정 (터미널 실습)</h2>
<p>가장 먼저, 문제 파일을 다운로드하고, 해당 Dockerfile이 있는 곳에서 터미널을 실행시켜, docker build .를 입력하였다.</p>
<p>```user@user-VirtualBox:~/Downloads/7728c510-c1f0-4806-8eca-776ee59d04a3$ docker build .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            <a href="https://docs.docker.com/go/buildx/">https://docs.docker.com/go/buildx/</a></p>
<p>~</p>
<p>Successfully built 2e1a00556281</p>
<pre><code>굉장히 길게 나왔지만, 중요한 부분은 빌드가 완료된 값인 2e1a00556281이다. 빌드된 이미지의 ID를 찾았기에, 2e1a00556281 이미지로부터 컨테이너를 생성 및 실행해봤다.
</code></pre><p>  user@user-VirtualBox:<del>/Downloads/7728c510-c1f0-4806-8eca-776ee59d04a3$ docker run -it 2e1a00556281 /bin/bash
chall@5d8605c7cd85:</del>$ ls
chall  flag
chall@5d8605c7cd85:<del>$ ./chall
Hello Beginners!
chall@5d8605c7cd85:</del>$ cat flag
DH{docker_exercise}</p>
<pre><code>
*주의
docker run 명령어 실행 시 -it 옵션을 주어야 컨테이너 내부의 표준 입출력(STDOUT/STDIN)이 현재 터미널과 연결되어 대화형(Interactive) 셸 모드로 진입할 수 있다.

---

## 4. 문제 풀이 및 코드 분석 (Line-by-Line)

Dockerfile의 주요 명령어 동작 및 권한 구조는 다음과 같다.

**RUN adduser $user &amp; USER $user:** 
   * root 권한 대신 chall이라는 일반 사용자 계정을 생성하고, 최종 동작 사용자를 chall로 지정했다.
---

## 5. 배운 점 및 회고
* **Dockerfile을 통한 컨테이너 구축:** docker build 명령으로 명세서(Dockerfile)를 읽어 독립된 가상화 이미지를 생성하는 기본 흐름을 체득했다.
* **-it 옵션을 활용한 디버깅:** Docker 컨테이너 실행 시 -it 옵션을 부여하여 이미지 내부 셸에 진입하고, 파일 시스템 구조와 권한 상태를 직접 점검하는 방법을 익혔다.
* **Docker 컨테이너 상태 파악:** docker ps -a 명령어로 종료된 컨테이너의 상태(Exited (0)) 및 컨테이너 ID를 확인하는 실습을 진행했다.

![](https://velog.velcdn.com/images/huijeong211/post/e07aa49b-bafb-4125-bcff-022b01b9bae8/image.jpg)
![](https://velog.velcdn.com/images/huijeong211/post/ddb417d8-d9d8-4306-a3b9-5630c989e0c4/image.jpg)
![](https://velog.velcdn.com/images/huijeong211/post/52528fa2-c91d-47f5-a946-2d15fec1d477/image.jpg)![](https://velog.velcdn.com/images/huijeong211/post/95cfab0f-4f58-4ccf-a419-7ee25c244efe/image.jpg)
</code></pre>